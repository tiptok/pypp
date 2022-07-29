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
def read_file():
    global records
    records = pd.read_excel('device_running_record.xlsx',engine='openpyxl')
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
def operate_write():
    global records
    records.to_excel("device_running_record_tmp_.xlsx", sheet_name="Sheet1", index=False)

read_file()
print("end read file")

operate_in()
print("end operate_in")

operate_to_lower()
print("end operate_to_lower")

operate_write()
print("end operate_write")

