from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
# from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv


load_dotenv()

db_user = os.environ["DB_USER"]
db_passwd = os.environ["DB_PASSWORD"]
db_host = os.environ["DB_HOST"]
db_port = os.environ["DB_PORT"]
db_name = os.environ["DB_NAME"]


def get_engine(user, passwd, host, port, name):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{name}"
    if not database_exists(url):
        create_database(url)

    engine = create_engine(url)

    return engine


def get_session():
    engine = get_engine(db_user, db_passwd, db_host, db_port, db_name)
    Session = sessionmaker(bind=engine)

    return Session
