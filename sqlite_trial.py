import sqlite3
conn = sqlite3.connect("test.db")

cursorObj = conn.cursor()
# cursorObj.execute(
# "CREATE TABLE  employees(id integer PRIMARY KEY, name text, salary real, department text,position text ,hireDate text)")
"""cursorObj.execute(
    "INSERT INTO employees VALUES(1,'John',700,'HR','Manager','2017-01-04')")
cursorObj.execute(
    "INSERT INTO employees VALUES(2,'Mary',300,'Sales','Corporate','2015-03-24')")
cursorObj.execute(
    "INSERT INTO employees VALUES(3,'Lebron',1000,'Sport','Athlete','2010-09-14')")
cursorObj.execute(
    "INSERT INTO employees VALUES(4,'Lazo',250,'PR','Officer','2020-01-04')")
cursorObj.execute(
    "INSERT INTO employees VALUES(5,'Julia',50,'HR','Client','2019-11-24')")
cursorObj.execute(
    "INSERT INTO employees VALUES(6,'Fazilla',200,'Officer','Cleaner','2016-12-01')")
cursorObj.execute(
    "INSERT INTO employees VALUES(7,'Jon',20,'Movies','Actor','2011-01-04')")
cursorObj.execute(
    "INSERT INTO employees VALUES(8,'Leignhn',700,'Manufacturing','Supervisor','2017-05-04')")
cursorObj.execute(
    "INSERT INTO employees VALUES(9,'John',200,'HR','Manager','1976-01-04')")
cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')"""
cursorObj.execute('SELECT * FROM employees')
rows = cursorObj.fetchall();
for row in rows:
    print(row)


conn.commit()
conn.close()