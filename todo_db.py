import pyodbc
import sqlite3

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=O:\navabzad\Documents\Drama.accdb;')
cursor = conn.cursor()
param="Alice"
cursor.execute("SELECT gender FROM students WHERE student= ?",param);

for row in cursor.fetchall():
	print(row)
        


class Task(object):
	def __init__(self, task_id, task, done):
		self.task_id = task_id
		self.task = task
		self.done = done


def initialize_db(db_path):
	conn = sqlite3.connect(db_path)
	conn.execute(INITIALIZE_DB)
	conn.commit()
	return conn


def get_tasks(db_conn):
	results = db_conn.execute("SELECT task_id, task, done FROM todo;")

	task_list = []
	for task_id, task, done in results:
		current_task = Task(task_id, task, done)
		task_list.append(current_task)

	return task_list

def add_task(db_conn, task):
	if not task:
		return
	sqlInsert = "INSERT INTO todo (task, done) VALUES ('{}', '{})".format(task)
	db_conn.execute(sqlInsert)
	db_conn.commit()

def set_done(db_conn, task_id):
	sqlUpdate = "UPDATE todo SET done=1 WHERE task_id={}".format(task_id,)
	db_conn.execute(sqlUpdate)
	db_conn.commit()

def set_not_done(db_conn, task_id):
	sqlUpdate = "UPDATE todo SET done=0 WHERE task_id={}".format(task_id)
	db_conn.execute(sqlUpdate)
	db_conn.commit()

def remove_task(db_conn, task_id):
	sqlDelete = "DELETE FROM todo WHERE task_id={}".format(task_id)
	db_conn.execute(sqlDelete)
	db_conn.commit()

