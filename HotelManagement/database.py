import pyodbc
class DatabaseConnection:
    
    @staticmethod
    def get_connection():
        # this function is for creating a DB connection
        try :
            conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=KAUSTUBH\SQLEXPRESS;"
                "DATABASE=hotelDB;"
                "Trusted_Connection=yes;"
            )
            return conn
        except Exception as e:
            print("Databse Connection Error :" , e)
            return None
