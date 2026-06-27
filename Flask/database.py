import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE = "prediction.db"




def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        applicant_name TEXT,

        gender TEXT,

        married TEXT,

        dependents TEXT,

        education TEXT,

        self_employed TEXT,

        applicant_income REAL,

        coapplicant_income REAL,

        loan_amount REAL,

        loan_term REAL,

        credit_history TEXT,

        property_area TEXT,

        prediction TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()
    conn.close()


def save_prediction(data):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO predictions(

applicant_name,

gender,

married,

dependents,

education,

self_employed,

applicant_income,

coapplicant_income,

loan_amount,

loan_term,

credit_history,

property_area,

prediction

)

   VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)

    """, data)

    conn.commit()

    conn.close()
def register_user(fullname, email, password):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    hashed_password = generate_password_hash(password)

    try:
        cursor.execute("""
            INSERT INTO users(fullname, email, password)
            VALUES (?, ?, ?)
        """, (fullname, email, hashed_password))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()
def login_user(email, password):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, fullname, email, password
        FROM users
        WHERE email = ?
    """, (email,))

    user = cursor.fetchone()

    conn.close()

    if user and check_password_hash(user[3], password):
        return user

    return None
def login_user(email, password):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, fullname, email, password
        FROM users
        WHERE email = ?
    """, (email,))

    user = cursor.fetchone()

    conn.close()

    if user and check_password_hash(user[3], password):
        return user

    return None        


def get_predictions():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM predictions

    ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data

def get_all_predictions():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

        applicant_name,

        applicant_income,

        loan_amount,

        credit_history,

        prediction,

        created_at

        FROM predictions

        ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data
def get_total_predictions():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM predictions")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_approved():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT COUNT(*)

    FROM predictions

    WHERE prediction LIKE '%Approved%'

    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_rejected():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT COUNT(*)

    FROM predictions

    WHERE prediction LIKE '%Rejected%'

    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total
def create_users_table():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        fullname TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()

    conn.close()
def get_user(user_id):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, fullname, email
        FROM users
        WHERE id = ?
    """, (user_id,))

    user = cursor.fetchone()

    conn.close()

    return user
def email_exists(email):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id
        FROM users
        WHERE email = ?
    """, (email,))

    user = cursor.fetchone()

    conn.close()

    return user is not None
def get_user(user_id):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, fullname, email
        FROM users
        WHERE id = ?
    """, (user_id,))

    user = cursor.fetchone()

    conn.close()

    return user