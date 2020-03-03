import json
import mysql.connector
#import sqlalchemy as db
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from datetime import datetime
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv

with open('Const/config.json') as i:
    json_const = json.load(i)

# def sqlAlchamyData():
#     # engine = db.create_engine('dialect+driver://user:pass@host:port/db')
#     # engine = create_engine("mysql+pymysql://sylvain:passwd@localhost/db?host=localhost?port=3306")
#
#     engine = create_engine(
#         'mysql+mysqldb://TYNIH910AP:08Cm6Jrv2D@remotemysql.com/TYNIH910AP?host=remotemysql.com?port=3306')
#     connection = engine.connect()
#     # metadata = db.MetaData()
#     # census = Table('ship_registration', metadata, autoload=True, autoload_with=engine)
#     # print(census.columns.keys())
#
#     session = scoped_session(sessionmaker(bind=engine))
#     Base = declarative_base()
#
#     # The business case here is that a company can be a stakeholder in another company.
#     class QuesCat(Base):
#         __tablename__ = 'ques_category'
#         q_cat_id = Column(Integer, primary_key=True)
#         cat_name = Column(String(100), nullable=False)
#         description = Column(String(1000), nullable=True)
#         questionaries = relationship("Questions", backref="ques_category")
#
#     class Questions(Base):
#         __tablename__ = 'questions'
#         q_id = Column(Integer, primary_key=True)
#         name = Column(String(100), nullable=False)
#         q_cat_id = Column(Integer, ForeignKey('ques_category.q_cat_id'))
#         # QuesCat = relationship("QuesCat", foreign_keys=[q_cat_id])
#         ques_answers = relationship("Answers", backref="questions")
#
#     class Answers(Base):
#         __tablename__ = 'ques_answers'
#         ans_id = Column(Integer, primary_key=True)
#         q_id = Column(Integer, ForeignKey('questions.q_id'), nullable=False)
#         # Questions = relationship("Questions", foreign_keys=[q_id])
#         name = Column(String(50), nullable=False)
#
#     Base.metadata.create_all(engine)
#
#     # simple query test
#     q1 = session.query(QuesCat).all()
#     q2 = session.query(Questions).all()
#     print()
#     print(q2)
#

# conn = sqlite3.connect(json_const['DB_NAME'])
# c = conn.cursor()

# Create the connection object
try:
    conn = mysql.connector.connect(host=json_const['Server'], user=json_const['db_Username'], passwd=json_const['DB_Password'], \
                                     database=json_const['Database_name'])

    # printing the connection object
    print(conn)

    # creating the cursor object
    c = conn.cursor()
except Exception as e:
    print(e)
#print(c)


def _detailscheck(ship_username,ship_email):
    c.execute(
        "SELECT * FROM ship_registration WHERE username='"+ship_username + "' or ship_email='" +ship_email + "'")
    if len(c.fetchall()) < 1:
        return True
    else:
        return False

def _userCount():
    c.execute("SELECT * FROM ship_registration")
    if len(c.fetchall()) >= 1:
        return False
    else:
        return True

def _userregi(data):
    c.execute(
            "INSERT INTO ship_registration(ship_name, ship_email, ship_email_pwd, sys_pwd,country,call_sign, imo_number, created_at,username) \
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (data['ship_name'],\
             data['ship_email'], data['ship_email_pwd'], \
             data['lpgin_pwd'],data['ship_country'],data['call_sign'], data['imo_number'], str(datetime.now()), data['ship_username']))
    conn.commit()
    return True

def _logincheck(data):
    c.execute("SELECT * FROM ship_registration WHERE username='"+ data['ship_username'] +"' and sys_pwd='"+ data['sys_pwd'] +"'")
    if len(c.fetchall()) == 1:
        return True
    else:
        return False

def QuestionImport(file):

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        c.execute('delete from ques_answers')
        conn.commit()
        c.execute('delete from questions')
        conn.commit()
        c.execute('delete from ques_category')
        conn.commit()
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                cat_id = ''
                if row[0]:

                    c.execute('select q_cat_id from ques_category where cat_name="' + row[0] + '"')
                    cat_id = c.fetchone()
                    if not cat_id:
                        sym_type = row[8] if row[8] else 1
                        c.execute("INSERT INTO ques_category(cat_name, description, status, sym_type) \
                                                              VALUES (%s,%s,%s,%s)", (row[0], row[7], 1, sym_type))
                        conn.commit()
                        cat_id = c.lastrowid
                    else:
                        cat_id = cat_id[0]

                    if cat_id and row[1]:
                        #print(row[1] + "    question")
                        q_type = ''
                        ans_name = ''
                        answes = []
                        question = []
                        if row[2]:
                            if row[2] == 'fill_in_blank':
                                q_type = 1
                                ans_name = '---------'
                            if row[2] == 'Yes/No':
                                q_type = 2
                            if row[2] == 'Multiple':
                                q_type = 3
                        if q_type:
                            question = [cat_id, row[1], q_type, 1]

                            c.execute("INSERT INTO questions(q_cat_id,name, qus_type, status) VALUES (%s,%s,%s,%s)",
                                      question)
                            conn.commit()
                            q_id = c.lastrowid
                            if ans_name:
                                answes.append([ans_name, q_id, 1])
                            if row[3]:
                                answes.append([row[3], q_id, 1])
                            if row[4]:
                                answes.append([row[4], q_id, 1])
                            if row[5]:
                                answes.append([row[5], q_id, 1])
                            if row[6]:
                                answes.append([row[6], q_id, 1])
                            c.executemany("INSERT INTO ques_answers(name,q_id,status) VALUES (%s,%s,%s)", answes)
                            conn.commit()
                            # print(answes)
                line_count += 1

        print(f'Processed {line_count} lines.')
    return True

def readFromDB():
    c.execute("SELECT ship_name,ship_email,call_sign,imo_number,country,username FROM ship_registration")
    return c.fetchall()