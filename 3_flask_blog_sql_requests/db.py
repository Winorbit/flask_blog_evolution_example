import psycopg2
dev_db_settings = {"dbname":'testdatabase', 
               "user":'dev_user', 
               "password":'qwerty', 
               "host":'31.131.28.206'}

def connect_to_db(db_settings):
    conn = psycopg2.connect(**db_settings)
    return conn
    pass
     
def get_all_posts():
    conn = connect_to_db(dev_db_settings)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM articles")
    result = list(cursor.fetchall())

    cursor.close()
    conn.close()
    return result

def write_new_user(email, password):
    conn = connect_to_db(dev_db_settings)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users(email, password) VALUES('{email}', '{password}')")
    conn.commit()

    cursor.close()
    conn.close()
    return True

def write_new_post(title, text):
    conn = connect_to_db(dev_db_settings)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO articles(title, text) VALUES('{title}', '{text}')")
    conn.commit()

    cursor.close()
    conn.close()
    return True


def check_user_exist(email, password):
    conn = connect_to_db(dev_db_settings)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    #print(result, len(result))
    if len(result) > 0:
        return True
    else:
        return False
