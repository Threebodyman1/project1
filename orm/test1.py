from multiprocessing import Process
import time
import os
import csv
import sys
import glob
import os
from libmysql import MYSQL

# msyql dababase connection info
dbconn = MYSQL(
        dbhost = 'localhost', 
        dbuser = 'root', 
        dbpwd = '', 
        dbname = 'yebase', 
        dbcharset = 'utf8')

A=glob.glob('../data/*.csv')
print(A)

def csv2dcitlist(path):
    with open(path, 'r',encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        column=[row for row in reader]
    return column

for i in A:
    (path, filename) = os.path.split(i)
    print(filename)
    dictlist=csv2dcitlist(i)
    stockid=filename.split('.')[0]
    for j in dictlist:
        j['stock_code']=stockid
        j['close']=float(j['close'].replace(",",""))
        j['open']=float(j['open'].replace(",",""))
        j['high_day']=float(j['high_day'].replace(",",""))
        j['low_day']=float(j['low_day'].replace(",",""))
        if j['volume']=='-':
            j['volume']=0
        else:
            if j['volume'][-1]=='K':
                j['volume']=float(j['volume'][:-2])*0.001
            else:
                j['volume']=float(j['volume'].replace(",",""))
        j['amplitude']=float(j['amplitude'].replace(",",""))
        print(j)
        dbconn.insert(table="stocks", data=j)

def f():
    lock = redis_lock.Lock(conn, "A")
    count=0
    if lock.acquire(blocking=True):
        print("Got the lock.")
        time.sleep(0.1)
        lock.release()
        conn.incr("A")
        print(conn.get("A"))
        print(os.getpid())
        print("end")
    else:
        count+=1
            

if __name__ == '__main__':
    global conn
    conn = redis.StrictRedis(host='localhost', port=6379, db=0)
    conn.set("A",1)
    for num in range(10):
        p=Process(target=f, args=())
        p.start()
        p.join()
    print("NED")