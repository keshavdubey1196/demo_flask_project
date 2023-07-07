from flask import Flask, render_template, request, make_response
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

db_user = os.environ["DB_USER"]
db_passwd = os.environ["DB_PASSWORD"]
db_host = os.environ["DB_HOST"]
db_port = os.environ["DB_PORT"]
db_name = os.environ["DB_NAME"]

url = f"postgresql://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_name}"

engine = create_engine(url)

Base = declarative_base()


# class Student(Base):
#     __tablename__ = "students"

#     stuId = Column(Integer, primary_key=True)
#     name = Column(String(100), unique=False, nullable=False)
#     marks = Column(Integer, unique=False, nullable=False)

#     def __str__(self):
#         return self.name


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    email = Column(String, unique=False, nullable=False)

    def __str__(self):
        return self.name


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


@app.route("/stuinfo", methods=["GET", "POST"])
def stuInfo():
    if request.method == "POST":
        print(request.form)
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']

        entry = User(id=id, name=name, email=email)
        session.add(entry)
        session.commit()
        session.close()
        print("User added")

    return make_response(render_template('index.html'))


if __name__ == "__main__":
    app.run()
