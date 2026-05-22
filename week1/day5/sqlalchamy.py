from sqlalchemy import create_engine, MetaData,Table,Column,Integer,String,insert,select,ForeignKey,Float


engine=create_engine("sqlite:///my_database3.db",echo=True)

meta=MetaData()

people=Table(
    "people",
    meta,
    Column("id" ,Integer,primary_key=True),
    Column("name",String,nullable=True),
    Column("age",Integer)
)


things=Table(
    "things",
    meta,
    Column("id",Integer,primary_key=True),
    Column("item_name",String,nullable=True),
    Column("description",String),
    Column("value",Float),
    Column("owner",Integer,ForeignKey("people.id"))
    )
meta.create_all(engine)

conn=engine.connect()
insert_people=people.insert().values([
    {"name":"saikiran","age":34},
    {"name":"karthick","age":47},
    {"name":"tarun","age":56},
    {"name":"adharsh","age":78},
])
insert_things=things.insert().values([
    { "owner":1,"item_name":"keyboard","description":"for typing","value":34.2},
    {"owner":2,"item_name":"mouse","description":"for clicking","value":45.3},
    {"owner":3,"item_name":"cpu","description":"for power gen","value":5.678},
    {"owner":4,"item_name":"gpu","description":" power ","value":56.897},
    {"owner":2,"item_name":"monitor","description":"system","value":98.76}
])

joins_statement=people.outerjoin(things,people.c.id==things.c.owner)
result=select(people.c.name,things.c.item_name,things.c.value).select_from(joins_statement)
response=conn.execute(result)
for i in response:
    print(i.name,i.item_name,i.value)