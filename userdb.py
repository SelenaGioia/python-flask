import pymysql


def check_user(username):

    sql = "SELECT id, username, password, fullname FROM users WHERE username=%s"

    conn = pymysql.connect(user='root', password='root',
                           database='wakekill', host='localhost')
    cursor = conn.cursor()
    cursor.execute(sql, (username,))

    result = cursor.fetchone()

    conn.close()

    return result


def all_alarms(user_id):
    sql = "SELECT id, hour FROM alarms WHERE user_id=%s"

    conn = pymysql.connect(user='root', password='root',
                           database='wakekill', host='localhost')
    cursor = conn.cursor()
    cursor.execute(sql, (user_id,))

    result = cursor.fetchall()

    conn.close()

    return result


if __name__=='__main__':
    print(check_user("Fulvio"))

    print(check_user("Mickey"))

    print(check_user("BadGuy"))

    print(all_alarms(1))

