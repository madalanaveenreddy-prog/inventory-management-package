from sqlalchemy import create_engine,text
from sqlalchemy.orm import Session
engine=create_engine('sqlite:///my_database.db',echo=True)
conn=engine.connect()
conn.execute(text("create table if not exists Users(id int primary key,name str,age int)"))
conn.commit()
session=Session(engine)
session.execute(text("insert into Users values(1,'NAveen',30)"))
session.commit()
session.close()
conn.close()

