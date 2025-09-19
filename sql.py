import sqlite3

connection=sqlite3.connect("student.db")

# create a cursor to insert and retrive and create table
cursor=connection.cursor()


table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

#insert some more records

cursor.execute('''Insert Into STUDENT values("Mayank","Data Science", "A", 90)''')
cursor.execute('''Insert Into STUDENT values("Shubh","computer Science", "B", 100)''')
cursor.execute('''Insert Into STUDENT values("kanika","Data analysis", "A", 80)''')
cursor.execute('''Insert Into STUDENT values("Pragya"," Science", "C", 70)''')
cursor.execute('''Insert Into STUDENT values("Siddhant","Social Science", "C", 98)''')

##Display the table 
print("The inserteed data is : ")
data= cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)
connection.commit()
connection.close()