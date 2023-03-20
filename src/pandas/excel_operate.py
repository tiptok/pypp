import  pandas as pd
import time

def get_time(f):

    def inner(*arg,**kwarg):
        s_time = time.time()
        res = f(*arg,**kwarg)
        e_time = time.time()
        print('耗时：{}秒'.format(e_time - s_time))
        return res
    return inner

records = pd.DataFrame()

@get_time
def read_xlsx_file(filename):
    global records
    records = pd.read_excel(filename,engine='openpyxl')
    print("file:",filename)
    print(records.head())
    print(records.info())

@get_time
def read_xls_file(filename):
    global records
    records = pd.read_excel(filename,engine='xlrd')
    print("file:",filename)
    print(records.head())
    print(records.info())

@get_time
def read_csv_file(filename):
    global records
    records = pd.read_csv(filename, encoding = "ISO-8859-1")
    print("file:",filename)
    print(records.head())
    print(records.info())

@get_time
def operate_in():
    global records
    fetch_46_48 = records[records['device_id'].isin([46,47,8])]
    print(fetch_46_48.head(2))

@get_time
def operate_to_lower():
    global records
    # records.apply(lambda x: x.lower(),axis=1,index=['device_code'])
    records['device_code'] = records['device_code'].str.lower()
    to_lower_tail = records[['device_id','device_code']].tail(10)
    print(to_lower_tail)

@get_time
def operate_write(filename):
    global records
    records.to_excel("tmp\\"+filename, sheet_name="Sheet1", index=False)

@get_time
def operate_xls_write(filename):
    global records
    records.to_excel("tmp\\"+filename, sheet_name="Sheet1", index=False,engine='xlwt')

@get_time
def operate_csv_write(filename):
    global records
    records.to_csv("tmp\\"+filename,index=False)

### 普通测试
# read_xlsx_file('device_running_record.xlsx')
# print("end read file")
#
# operate_in()
# print("end operate_in")
#
# operate_to_lower()
# print("end operate_to_lower")
#
# operate_write('device_running_record.xls')
# print("end operate_write")


### 测试读取 excel
# read_xlsx_file('device_running_record_5w.xlsx')
# operate_write('device_running_record_5w.xlsx')
# read_xlsx_file('device_running_record_20w.xlsx')
# operate_write('device_running_record_20w.xlsx')
# read_xlsx_file('device_running_record.xlsx')


### 测试读取 csv
# read_csv_file('device_running_record_5w.csv')
# operate_csv_write('device_running_record_5w.csv')
#
# read_csv_file('device_running_record_20w.csv')
# operate_csv_write('device_running_record_20w.csv')
#
# read_csv_file('device_running_record.csv')
# operate_csv_write('device_running_record.csv')

### 测试读取 xls
read_xls_file('device_running_record_1w.xls')
operate_xls_write('device_running_record_1w.xls')