from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:1995@localhost:5432/QA"
db = create_engine(db_connection_string)


#добавление предмета. insert
def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("""insert into subject(\"subject_id\", \"subject_title\") values (:new_id, :new_title)""")
    connection.execute(sql, {"new_id": 17, "new_title": "Robotech"})

    transaction.commit()
    connection.close()


#обновление предмета. update
def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE subject SET subject_title = :update_title WHERE subject_id = :sub_id")
    connection.execute(sql, {"sub_id": 17, "update_title": 'Robotechnology'})

    transaction.commit()
    connection.close()


#удаление предмета. delete
def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM subject WHERE subject_id = :sub_id")
    connection.execute(sql, {"sub_id": 17})

    transaction.commit()
    connection.close()


#получение списка таблиц
def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'subject'


#получение строк из таблицы
def test_select():
    connection = db.connect() #Создаём соединение
    result = connection.execute(text("select * from subject"))
    rows = result.mappings().all() #Получаем результат в виде словарей
    row1 = rows[1]

    assert row1["subject_id"] == 3
    assert row1["subject_title"] == "Physics"


#получение строки по одному фильтру
def test_select_1_row():
    connection = db.connect()
    sql_statement = text("select * from subject where subject_id = :sub_id")
    result = connection.execute(sql_statement, {"sub_id": 3})
    rows = result.mappings().all()

    assert len(rows) == 1
    assert rows[0]["subject_title"] == "Physics"

    connection.close()


#получение строки по двум фильтрам
def test_select_1_row_with_two_filters():
    connection = db.connect()

    sql_statement = text("select * from subject where subject_id <= :sub_id OR subject_title = :sub_name")
    result = connection.execute(sql_statement, {"sub_name": "Physics", "sub_id": 2})
    rows = result.mappings().all()

    assert len(rows) == 3

    connection.close()
