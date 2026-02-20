import pyodbc

class Database:

    @staticmethod
    def get_connection():
        try:
            conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=KAUSTUBH\\SQLEXPRESS;"
            "Database=hostel;"
            "Trusted_Connection=yes;"
            )
            return conn

        except Exception as e:
            print("Databse Connection Error :" , e)
            return None
        

    @staticmethod
    def insert_record(data):
        conn = None
        cursor = None
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO student_fees 
            (student_name, subject, analytics, hostel, food_months, transport, total_amount)
            VALUES (?,?, ?, ?, ?, ?, ?)
            """

            cursor.execute(query, data)
            conn.commit()

        except Exception as e:
            print("Databse Connection Error :" , e)
            return None

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
