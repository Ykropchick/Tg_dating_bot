import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('sql.db')
    cur = base.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user(id INT PRIMARY KEY, name Text, age INT, \
    sex TEXT, description TEXT, img TEXT, cur_anket INT DEFAULT(0))")
    cur.execute("CREATE TABLE IF NOT EXISTS sympathy(sender_id INT PRIMARY KEY, host_id INT )")
    base.commit()


def add_sympathy(sender_id, host_id):
    cur.execute("INSERT OR REPLACE INTO sympathy VALUES(sender_id, host_id)", (sender_id, host_id))
    base.commit()


def delete_sympathy(sender_id, host_id):
    cur.execute("DELETE FROM sympathy WHERE sender_id=?, host_id=?", (sender_id, host_id))
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT OR REPLACE INTO user VALUES(?, ?, ?, ?, ?, ?, ?)", tuple(data.values()))
        base.commit()


def take_all_ankets(id):
    cur.execute("SELECT * FROM user EXCEPT SELECT * FROM user WHERE id=?", (id, ))
    info = cur.fetchall()
    return info


def reload_ankets(id):
    cur.execute(f'UPDATE user SET cur_anket = ? WHERE id=?', (0, id))
    base.commit()


def increase_cur_anket(id, cur_anket):
    cur.execute(f'UPDATE user SET cur_anket = ? WHERE id=?', (cur_anket, id))
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
