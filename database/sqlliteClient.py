import sqlite3 as sq


def sql_start():
    """
    иницализирует бд
     Таблицы:
        User:
            id - айди пользователя
            name - имя пользователя
            age - возраст пользователя
            sex - пол пользователя
            description - описание пользователя
            img - айди фото пользователя
            cur_anket - текущая анкета, которую пользователь просматривает( во всех анкетах)
        sympathy:
            sender_id - айди тот, кто отправил симатияю
            host_id - айди того, кому отпарвили симпатию
    """
    global base, cur
    base = sq.connect('sql.db')
    cur = base.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user(id INT PRIMARY KEY, name Text, age INT, \
    sex TEXT, description TEXT, img TEXT, cur_anket INT DEFAULT(0))")
    cur.execute("CREATE TABLE IF NOT EXISTS sympathy(sender_id INT, host_id INT)")
    base.commit()


def add_sympathy(sender_id, host_id):
    """
    Добавляет симпатию в бд
    """
    cur.execute("INSERT OR REPLACE INTO sympathy VALUES(?, ?)", (sender_id, host_id))
    base.commit()


def delete_sympathy(sender_id, host_id):
    """
    Удаляет симпатию
    """
    cur.execute("DELETE FROM sympathy WHERE sender_id=? and host_id=?", (sender_id, host_id))
    base.commit()


def take_sympathy(id):
    """
    Достает симпатию из бд
    Первое значение тот кто отправил, второе тот кто принял
    Ищет по значентю принимающего
    """
    cur.execute("SELECT * FROM user WHERE id = (SELECT sender_id FROM sympathy WHERE host_id=?)", (id, ))
    info = cur.fetchall()
    return info

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT OR REPLACE INTO user VALUES(?, ?, ?, ?, ?, ?, ?)", tuple(data.values()))
        base.commit()


def take_all_ankets(id):
    """
    Возвращает все анкеты
    """
    cur.execute("SELECT * FROM user")
    info = cur.fetchall()
    return info


def reload_ankets(id):
    """
    Выставляет 0 в анкету которую щас смотрит у определенного юзера
    """
    cur.execute(f'UPDATE user SET cur_anket=? WHERE id=?', (0, id))
    base.commit()


def increase_cur_anket(id, cur_anket):
    """
    Увеличивает на 1 анкету, которую щас смотри у определенного юзоеа
    """
    cur.execute(f'UPDATE user SET cur_anket = ? WHERE id=?', (cur_anket, id))
    base.commit()


def take_user_info(id):
    """
    Возвращает информацию о определенном юзере
    """
    cur.execute(f"SELECT * FROM user WHERE id ={id}")
    info = cur.fetchall()
    return info


def delete_user(id):
    """
    Удаляет юзера
    """
    cur.execute(f"DELETE FROM user WHERE id=id")
    base.commit()


def change_description(id, description):
    """
    Меняет описание у определенного пользователя
    """
    cur.execute(f'UPDATE user SET description = ? WHERE id=?', (description, id))
    base.commit()


def change_photo(id, photo):
    """
    Меняет фото у определенного пользователя
    """
    cur.execute(f'UPDATE user SET img=? WHERE id=?', (photo, id))


def check_if_exist(id):
    """
    Проверяет существет ли такой .юзер
    """
    cur.execute(f'SELECT * FROM user WHERE id=?', (id, ))
    info = cur.fetchall()
    return False if info else True
