import csv
from tkinter import filedialog
import mysql.connector
import json

with open('../Const/config.json') as i:
    json_const = json.load(i)

filez = filedialog.askopenfilename()
print(filez)
conn = mysql.connector.connect(host=json_const['Server'], user=json_const['db_Username'], passwd=json_const['DB_Password'], \
                                 database=json_const['Database_name'])
c = conn.cursor()
with open(filez) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            cat_id = ''
            if row[0]:
               print('select q_cat_id from ques_category where cat_name="'+row[0]+'"')
               catResult = c.execute('select q_cat_id from ques_category where cat_name="'+row[0]+'"')
               cat_id = c.fetchone()
               if not cat_id:
                   c.execute("INSERT INTO ques_category(cat_name, description, status) \
                                          VALUES (%s,%s,%s)", (row[0], row[7], 1))
                   conn.commit()
                   cat_id = c.lastrowid
               else:
                   cat_id = cat_id[0]
               if cat_id and row[1]:
                    print(row[1] + "    question")
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
                        question = [cat_id,row[1],q_type,1]

                        c.execute("INSERT INTO questions(q_cat_id,name, qus_type, status) VALUES (%s,%s,%s,%s)", question)
                        conn.commit()
                        q_id = c.lastrowid
                        if ans_name:
                            answes.append([ans_name, q_id, 1])
                        if row[3]:
                            answes.append([row[3],q_id,1])
                        if row[4]:
                            answes.append([row[4], q_id, 1])
                        if row[5]:
                            answes.append([row[5], q_id, 1])
                        if row[6]:
                            answes.append([row[6], q_id, 1])
                        c.executemany("INSERT INTO ques_answers(name,q_id,status) VALUES (%s,%s,%s)", answes)
                        conn.commit()
                        #print(answes)
            line_count += 1
    print(f'Processed {line_count} lines.')

