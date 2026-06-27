import sqlite3

DATABASE = "prediction.db"


def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

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

    VALUES(?,?,?,?,?,?,?,?,?,?,?,?)

    """, data)

    conn.commit()

    conn.close()


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