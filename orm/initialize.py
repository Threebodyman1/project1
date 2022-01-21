import csv
import sys
import glob
import os
from libmysql import MYSQL
import time
from multiprocessing import Process
# msyql dababase connection info
dbconn = MYSQL(
        dbhost = 'localhost', 
        dbuser = 'root', 
        dbpwd = '', 
        dbname = 'szr', 
        dbcharset = 'utf8')



def csv2dcitlist(path):
    with open(path, 'r',encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        column=[row for row in reader]
    return column


def insert_Test(file_list):
    A=file_list
    for i in A:
        (path, filename) = os.path.split(i)
        print(filename)
        dictlist=csv2dcitlist(i)
        stockid=filename.split('.')[0]
        B=[]
        k=0
        for j in dictlist:
            k=k+1
            j['id']=k
            j['date']=str(j['date'].replace("/","-"))
            j['open']=float(j['open'].replace(",",""))
            j['close']=float(j['close'].replace(",",""))
            j['high']=float(j['high'].replace(",",""))
            j['low']=float(j['low'].replace(",",""))
            j['volume']=float(j['volume'].replace(",",""))
            j['price_change']=float(j['price_change'].replace(",",""))
            j['p_change']=float(j['p_change'].replace(",",""))
            j['ma5']=float(j['ma5'].replace(",",""))
            j['ma10']=float(j['ma10'].replace(",",""))
            j['ma20']=float(j['ma20'].replace(",",""))
            j['v_ma5']=float(j['v_ma5'].replace(",",""))
            j['v_ma10']=float(j['v_ma10'].replace(",",""))
            j['v_ma20']=float(j['v_ma20'].replace(",",""))
            j['turnover']=float(j['turnover'].replace(",",""))
            B.append(j)
        print(len(B))
        dbconn.bulk_insert("stocks_253", B)
        """"""""""
        p=Process(target=dbconn.bulk_insert,args=("stocks", B))
        p.start()
        p.join()
        """""""""

if __name__=="__main__":
    A=glob.glob('/root/szr/Financial-Time-Series-master/Financial-Time-Others/data/002253.csv')
    print(A)
    start=time.time()
    insert_Test(A)
    print(time.time()-start)