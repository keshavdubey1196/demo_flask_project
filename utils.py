import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()


def create_connection():
    # Creating connection to PG db
    con = psycopg2.connect(
        host="localhost",
        port=5432,
        database="flask_api",
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )
    return con


con = create_connection()
