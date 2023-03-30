"""
Database Engine: 
        Oracle, MySQL, SQL*Server, SqlLite, ...

SQL Syntax:
    
create table product (name varchar(20) primary key, price float, qty int)

drop table product # to delete the whole table


insert into product values ('Prod1', 34.56, 23)

select * from product
select * from product where qty > 20
select price, qty from product where qty > 20

delete from product where qty=0

update product set price=price*1.25 where name='Prod3'

commit      # validate a transaction
rollback    # invalidate a transaction (the insert,delete,update done previously)

"""

import sqlite3 # compliant with the DBAPI 2

try:
    # Step 1: connection
    conn=sqlite3.connect(r"pyInt.db") 
    # Step 2: create a cursor object
    cursor=conn.cursor()
    # Step 3: using the cursor, execute SQL statements:
    cursor.execute("create table product (name varchar(20) primary key, price float, qty int)")

    cursor.close()
    conn.close()
except Exception as ex:
    print(ex)