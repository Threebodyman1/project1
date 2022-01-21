#!/usr/bin/env python
# encoding: utf-8
"""""""""
CREATE TABLE `stocks` (
	`stock_code` varchar(12) NOT NULL,
	`stock_date` varchar(255) COLLATE utf8_bin NOT NULL,
	`close` float NOT NULL,
	`open` float NOT NULL default 0,
	`high_day` float NOT NULL default 0,
	`low_day` float NOT NULL default 0,
	`volume` float NOT NULL default 0,
	`amplitude` float NOT NULL default 0,
	PRIMARY KEY (`stock_code`)
)ENGINE=INNODB DEFAULT CHARSET=utf8;

"""""""""""
from libmysql import MYSQL

# msyql dababase connection info
dbconn = MYSQL(
        dbhost = 'localhost', 
        dbuser = 'root', 
        dbpwd = '', 
        dbname = 'ye_teach', 
        dbcharset = 'utf8')

# insert data, 插入数据
user = {'stock_code': '60000', 'stock_date':'123123',
	'close':1.23,'open':3.2,
	'high_day':3.3,
	'low_day':2.2,
	'volume':1.2,
	'amplitude':1.2,}
dbconn.insert(table='stocks', data=user)
""""""""""
# change user dict, 修改用户信息提交
user['email'] = 'ringzero@wooyun.org'
user['password'] = '123456'
dbconn.insert(table='users', data=user)

# update 更新用户信息
user = {'email': 'newringzero@0x557.org', 'password': '888888'}
cond = {'email': 'ringzero@0x557.org'}
rows = dbconn.update(table='users', data=user, condition=cond)
print('update {} records success..'.format(rows))

# delete data, 删除数据, limit参数为删除少条
cond = {'email': 'ringzero@0x557.org'}
rows = dbconn.delete(table='users', condition=cond, limit='1')
print('deleted {} records success..'.format(rows))

# 统计数据库记录条数
cond = {'email': 'ringzero@wooyun.org'}
cnt = dbconn.count(
                table='users', 
                condition=cond)
print(cnt)

# select 查询信息
fields = ('id', 'email')
cond = {'email': 'ringzero@wooyun.org'}
rows = dbconn.fetch_rows(
                    table='users', 
                    fields=fields, 
                    condition=cond, 
                    order='id asc', 
                    limit='0,5')

for row in rows:
    print(row)

# 不指定 fields 字段, 将返回所有*字段, 
# 不指定 order, 将不进行排序
# 不指定 limit, 将返回所有记录

rows = dbconn.fetch_rows(
                    table='users', 
                    condition=cond,
                    limit='0,5')
for row in rows:
    print(row)

# query 执行自定义SQL语句
sql = 'select * from users limit 0, 5'
rows = dbconn.query(sql)
for row in rows:
    print(row)

"""""""""