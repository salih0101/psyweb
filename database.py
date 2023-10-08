import sqlite3

connection = sqlite3.connect('vebinar.db')
sql = connection.cursor()


def add_user(user_id, name, phone_number):
    connection = sqlite3.connect('vebinar.db')
    sql = connection.cursor()
    sql.execute('INSERT INTO users VALUES (?,?,?);',
                (user_id, name, phone_number))
    connection.commit()

    return add_user

def check_user(user_id):
    connection = sqlite3.connect('vebinar.db')
    sql = connection.cursor()
    checker = sql.execute('SELECT user_id FROM users WHERE user_id=?;',
                          (user_id,))

    if checker.fetchone():
        return True
    else:
        return False




# sql.execute('CREATE TABLE users(user_id integer, name text, phone_number text);')

# sql.execute('CREATE TABLE cart2 (user_id INTEGER, product_name TEXT, user_number TEXT, product_price INTEGER, product_count INTEGER);')
# sql.execute('CREATE TABLE products (name INTEGER, id INTEGER, price INTEGER, description TEXT, picture TEXT, notes TEXT);')
