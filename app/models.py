from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
Base=declarative_base()
engine = create_engine('sqlite:///database.db',echo=True)
Session = sessionmaker(bind=engine)
session=Session()
class Classroom(Base):
    __tablename__='classrooms'
    id = Column(Integer,primary_key=True)
    form = Column(String)
    stream = Column(String)
    def __repr__(self):
        return f"{self.form} {self.stream}"
class Students(Base):
    __tablename__='students'
    id = Column(Integer,primary_key=True)
    full_name=Column(String)
    index_no = Column(Integer)
    guardian = Column(String)
    dob=Column(String)
    admission_date = Column(String,default=str(datetime.now()))
    classroom = Column(String)
class Teachers(Base):
    __tablename__='teachers'
    id = Column(Integer,primary_key=True)
    full_name=Column(String)
    contacts = Column(Integer)
    location=Column(String)
    subjects = Column(String)
    date_hired = Column(String)
class Parents(Base):
    __tablename__='parents'
    id = Column(Integer,primary_key=True)
    full_name=Column(String)
    children = Column(String)
    contacts=Column(String)
    location = Column(String)
    childID = Column(Integer,ForeignKey('students.id'))
class Subjects(Base):
    __tablename__='subjects'
    id = Column(Integer,primary_key=True)
    name=Column(String)
    teacherID=Column(Integer,ForeignKey('teachers.id'))
    StudentsTakingID = Column(Integer,ForeignKey('students.id'))
class Library(Base):
    __tablename__ = 'library'
    bookId = Column(Integer,primary_key=True)
    title = Column(String)
    number = Column(Integer)
class bookTaken(Base):
    __tablename__='booktaken'
    id = Column(Integer,primary_key=True)
    title = Column(String)
    adm=Column(Integer)
    name=Column(String)
    status=Column(String)
class Fees(Base):
    __tablename__='fees'
    id = Column(Integer,primary_key=True)
    total_term1=Column(Integer)
    total_term2=Column(Integer)
    total_term3=Column(Integer)
class classteachers(Base):
    __tablename__ = 'classteachers'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    classroom = Column(String)

class fee_payed(Base):
    __tablename__='fee payed'
    id = Column(Integer,primary_key=True)
    name=Column(String)
    adm = Column(Integer)
    amount = Column(Integer)
    bal = Column(Integer)
    date = Column(String,default=datetime.now().date())
class events(Base):
    __tablename__ = 'events'
    id = Column(Integer,primary_key=True)
    title = Column(String)
    info = Column(Text)
    dueDate = Column(String)
Base.metadata.create_all(bind=engine)


