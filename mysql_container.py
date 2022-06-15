from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine
from testcontainers.mysql import MySqlContainer


meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String(20)), 
   Column('lastname', String(30)),
)

with MySqlContainer('mysql:5.7.17') as mysql:
    engine = create_engine(mysql.get_connection_url())
    version, = engine.execute("select version()").fetchone()
    print(version)  # 5.7.17
    meta.create_all(engine)
    engine.execute("insert into students values (1, 'Joseph', 'Valenciano')")
    result = engine.execute("select name from students")
    for row in result:
        print("name:", row['name'])
    result.close()

