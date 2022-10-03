import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('sql.db')
    cur = base.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user(id INT PRIMARY KEY, name Text, age INT, \
    sex TEXT, description TEXT, img TEXT, cur_anket INT DEFAULT(0))")
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT OR REPLACE INTO user VALUES(?, ?, ?, ?, ?, ?, ?)", tuple(data.values()))
        base.commit()


def take_user_info(id):
    cur.execute(f"SELECT * FROM user WHERE id ={id}")
    info = cur.fetchall()
    return info


def delete_user(id):
    cur.execute(f"DELETE FROM user WHERE id=id")
    base.commit()


def change_description(id, description):
    cur.execute(f'UPDATE user SET description = ? WHERE id=?', (description, id))
    base.commit()


def change_photo(id, photo):
    cur.execute(f'UPDATE user SET img=? WHERE id=?', (photo, id))


def check_if_exist(id):
    cur.execute(f'SELECT * FROM user WHERE id=?', (id, ))
    info = cur.fetchall()
    return info
