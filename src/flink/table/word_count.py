import argparse
import logging
import sys

from pyflink.table import (TableEnvironment,EnvironmentSettings,DataTypes)
from pyflink.common import Row
from pyflink.table.expressions import lit, col
from pyflink.table.udf import udtf

# pip install apache-flink==1.15.1

def word_count(input_path,output_path):
    t_env = TableEnvironment.create(EnvironmentSettings.in_streaming_mode())
    t_env.get_config().set("parallelism.default", "1")
      # .set("pipeline.classpaths","D:\\java\\flink\\lib\\flink-connector-jdbc_2.11-1.13.6.jar;D:\\java\\flink\\lib\\mysql-connector-java-5.1.38.jar")
    source_ddl ="""
    create table source(
        word STRING
    ) with (
        'connector' = 'filesystem',
        'format' = 'csv',
        'path' = '{}'
    )
    """.format(input_path)

    ## 1.sink file system
    # sink_ddl = """
    # create table sink(
    #     word STRING,
    #     `count` BIGINT
    # ) with (
    #     'connector' = 'filesystem',
    #     'format' = 'canal-json',
    #     'path' = '{}'
    # )
    # """.format(output_path)

    ## 2.sink print for debug
    # sink_ddl = """
    #     create table sink(
    #         word STRING,
    #         `count` BIGINT
    #     ) with (
    #         'connector' = 'print'
    #     )
    #     """

    ## 3.sink jdbc mysql select version();
    ## 5.7.27 需要 mysql-connector-java > 8.0.0  => 8.0.20
    ## mysql-connector-java_8.0.20 => 需要jdbc版本 flink-connector-jdbc_2.12-1.14.0
    ## 需要下载的jar放在 D:\Python\Lib\site-packages\pyflink\lib 下
    # sink_ddl = """
    #         create table sink(
    #             word STRING,
    #             `count` BIGINT,
    #             PRIMARY KEY (word) NOT ENFORCED
    #         ) with (
    #            'connector' = 'jdbc',
    #            'url' = 'jdbc:mysql://localhost:3306/flink-demo?characterEncoding=utf8&useSSL=true&serverTimezone=UTC',
    #            'username' = 'root',
    #            'password' = '123456',
    #            'table-name' = 'word_count',
    #            'driver' = 'com.mysql.cj.jdbc.Driver'
    #         )
    #         """

    ## 3.sink starrocks=5.1.0  Flink版本 v1.15  flink-connector-starrocks-1.2.3_flink-1.15.jar
    # sink_ddl = """
    #         create table sink(
    #             word STRING,
    #             `count` BIGINT,
    #             PRIMARY KEY (word) NOT ENFORCED
    #         ) with (
    #            'connector' = 'jdbc',
    #            'url' = 'jdbc:mysql://118.178.239.45:9030/character_library_standard?characterEncoding=utf8&useSSL=true&serverTimezone=UTC',
    #            'username' = 'root',
    #            'password' = 'eagle1010',
    #            'table-name' = 'word_count',
    #            'driver' = 'com.mysql.cj.jdbc.Driver'
    #         )
    #         """
    sink_ddl = """
                CREATE TABLE sink(
                    word VARCHAR,
                    `count` BIGINT,
                    PRIMARY KEY (word) NOT ENFORCED
                ) with (
                   'connector' = 'starrocks',
                   'jdbc-url' = 'jdbc:mysql://220.250.41.79:9030/character_library_standard',
                   'load-url' = '220.250.41.79:8030',
                   'table-name' = 'word_count',
                   'username' = 'root',
                   'password' = 'eagle1010',
                   'database-name' = 'character_library_standard',
                   'sink.buffer-flush.interval-ms' = '5000',
                   'sink.properties.column_separator' = '\x01',
                   'sink.properties.row_delimiter' = '\x02'
                )
                """

    t_env.execute_sql(source_ddl)
    t_env.execute_sql(sink_ddl)

    # t_env.execute_sql("""insert into sink select 'a',1 """)
    tab = t_env.from_path('source')

    @udtf(result_types=[DataTypes.STRING()])
    def split(line: Row):
        for s in line[0].split():
            yield Row(s)

    # compute word count
    tab.flat_map(split).alias('word') \
        .group_by(col('word')) \
        .select(col('word'), lit(1).count) \
        .execute_insert('sink') \
        .wait(10000)

    # result =  t_env.sql_query("select * from source")
    # print(result.to_pandas().head(10))
    # t_env.execute_sql("insert into sink select word,0 from source");


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        required=False,
        help='Input file to process.')
    parser.add_argument(
        '--output',
        dest='output',
        required=False,
        help='Output file to write results to.')

    argv = sys.argv[1:]
    known_args, _ = parser.parse_known_args(argv)

    word_count(known_args.input, known_args.output)