import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Imthi$123",database="employee")
c=mydb.cursor()
c.execute("select * from leaves")
for i in c:
    print(i)
    
