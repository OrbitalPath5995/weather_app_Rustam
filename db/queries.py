from .base import connect_db, commit_and_close


def check_user_exists(db_name, username):
    connection, cursor = connect_db(db_name)

    cursor.execute("select * from users where username = ?;", (username,))
    user = cursor.fetchone()
    return True if user else False


def add_user(db_name, username):
    connection, cursor = connect_db(db_name)
    cursor.execute("insert into users(username) values (?);", (username,))
    commit_and_close(connection)
    print('added user:', username)


def add_data(db_name, table_name, **kwargs):
    connection, cursor = connect_db(db_name)

    fields = ', '.join(list(kwargs.keys()))
    values = tuple(kwargs.values())
    signs = ', '.join(['?' for _ in range(len(values))])
    sql = f"insert into {table_name}({fields}) values ({signs})"
    cursor.execute(sql, values)
    commit_and_close(connection)


def get_user_id(username, db_name):
    connection, cursor = connect_db(db_name)
    sql = "select user_id from users where username = ?;"
    cursor.execute(sql, (username,))
    user_id = cursor.fetchone()
    return user_id[0]


def get_user_weather(db_name, user_id):
    connection, cursor = connect_db(db_name)
    sql = "select * from weather where user_id = ?;"
    cursor.execute(sql, (user_id,))
    data_ = cursor.fetchall()
    return data_
