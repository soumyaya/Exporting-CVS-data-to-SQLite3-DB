import sqlite3

#created a connection to the "try2" DB and opened a cursor to that connection
conn = sqlite3.connect('try2.sqlite3')
cur = conn.cursor()

#ran SQL query : SELECT job FROM info GROUP BY job
#this returned 12 rows with the type of jobs
#created a dictionary for all the types of jobs
JOB_DICT = {
    "admin." : '1',
    "blue-collar" : '2',
    "entrepreneur": '3',
    "housemaid": '4',
    "management": '5',
    "retired" : '6',
    "self-employed":'7',
    "services": '8',
    "student": '9',
    "technician": '10',
    "unemployed": '11',
    "unknown": '-1'
}

#function to change the job title to job code 
def CHANGE_JOB(job):
    job_code = None
    if job in JOB_DICT:
        job_code = JOB_DICT.get(job)
    return job_code

#counted the no. of rows
cur.execute('SELECT count(*) FROM info')
length = cur.fetchone()[0]

#rows is a list of all the rows of 'job' column 
cur.execute("SELECT job FROM info")
rows = cur.fetchall()

#now 'rows' is a list of tuples. Tuples have the job title.
# created a list of job titles.
#string_rows_list is a list of strings, unlike 'rows'
string_rows_list = list()

for row in rows:
    for item in row:
        string_rows_list.append(item)

#ran the query to get job title from info table
#saved the output of the query to variable job
#called the function and saved it's output in variable new_job
for i in range(length):
    job = string_rows_list[i]
    new_job = CHANGE_JOB(job)
    cur.execute('UPDATE OR IGNORE info SET job=? WHERE job=?',(new_job,job))

conn.commit()
conn.close()




