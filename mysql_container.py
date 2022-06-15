from sqlalchemy import create_engine
from testcontainers.mysql import MySqlContainer

with MySqlContainer('mysql:5.7.17') as mysql:
    engine = create_engine(mysql.get_connection_url())
    version, = engine.execute("select version()").fetchone()
    print(version)  # 5.7.17
    engine.execute("""
                    CREATE TABLE students (
                    id int,
                    name varchar(30),
                    lastname varchar(40)
                                        )
                """)
    engine.execute("insert into students values (1, 'Joseph', 'Valenciano')")
    engine.execute("insert into students values (2, 'Alejandro', 'Rojas')")
    result = engine.execute("select name from students")
    for row in result:
        print("name:", row['name'])
    result.close()

