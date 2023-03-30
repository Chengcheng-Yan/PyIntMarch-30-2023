"""
SQL Syntax:
    
create table product (name varchar(20) primary key, price float, qty int)

drop table product # to delete the whole table

drop table if exists product # to delete the whole table

insert into product values ('Prod1', 34.56, 23)

select * from product

select name, price from product

select * from product where qty > 20

delete from product where qty=0

update product set price=price*1.25 where name='Prod3'

commit # validate a transaction
rollback # invalidate the transaction (the insert,delete,update done previously)

alter 

grant

"""
import sqlite3

try:
    # Step 1: connection
    conn=sqlite3.connect(r"pyInt.db")
    # Step 2: create a cursor object
    cursor=conn.cursor()
    # Step 3: using the cursor, execute SQL statements:
    cursor.execute("drop table if exists temperatures")   
    cursor.execute("create table temperatures (id integer primary key autoincrement, city varchar(20), currenttime time, currentdate date, temp float)")
    
    with open("measures.txt") as fic:
        fic.readline() # to ignore the first line
        for line in fic:
            city,time,date,temp=line.split(";")
            # or
            # import re
            # city,time,date,temp=re.split(";", line)
            
            cursor.execute(f"insert into temperatures (city, currenttime ,currentdate,temp) values ('{city}', '{time}', '{date}', {temp})")
    
    cursor.execute("commit")
    
    cursor.execute("select city, currentdate, currenttime, temp from temperatures where city = 'Geneva'")
     
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print(row)


    cursor.close()
    conn.close()
except Exception as ex:
    print(ex)