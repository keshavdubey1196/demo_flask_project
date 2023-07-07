# # models to store and fetch data from postgres database
# from sqlalchemy.orm import declarative_base
# from sqlalchemy import Column, Integer, String
# from db import get_session

# session = get_session()
# Base = declarative_base()


# class Student(Base):
#     __tablename__ = "students"

#     stuId = Column(Integer(), primary_key=True)
#     name = Column(String(100), unique=False, nullable=False)
#     marks = Column(Integer(), unique=False, nullable=False)

#     def __str__(self):
#         return self.name


# def create():
#     Base.metadata.create(db)


# create()
