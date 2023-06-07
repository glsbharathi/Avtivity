import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="c361"
)
cursor=connection.cursor()
create_table_query="""CREATE TABLE if not exists table_name1( column1 varchar(255), column2 int)"""

cursor.execute(create_table_query) 
print("Table created sucessfully")

insert_query ="insert into table_name1 (column1, column2) values (%s,%s)"

data=[("Value1",87), ("Value2",87),("Value11",87), ("Value",87), ("Valued",87), ("Value5",87)] 
cursor.executemany(insert_query, data)

connection.commit()

selectquery="select * from table_name1" 
cursor.execute(selectquery)

rows =cursor.fetchall()

for row in rows: 
    print(row)

connection.commit()

cursor.close()

connection.close()
