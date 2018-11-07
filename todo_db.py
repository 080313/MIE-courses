import pyodbc
import sqlite3

#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=O:\navabzad\Documents\Drama.accdb;')
#cursor = conn.cursor()
#param="Alice"
#cursor.execute("SELECT gender FROM students WHERE student= ?",param);

#for row in cursor.fetchall():
	#print(row)
        



#class Student(Object):
	#def _init_(self,)

class Form1(object):
	def __init__(self,CourseCode,NickName,ProfName,Session,TAName,LABTUT, FinalGrade,LevelDifficulty,WorkLoad,Interesting,OverallRating):
		self.CourseCode=CourseCode
		self.NickName=NickName
		self.ProfName=ProfName
		self.Session=Session
		self.TAName=TAName
		self.LABTUT=LABTUT
		self.FinalGrade=FinalGrade
		self.LevelDifficulty=LevelDifficulty
		self.WorkLoad=WorkLoad
		self.Interesting=Interesting
		self.OverallRating=OverallRating
class Course(object):
	def __init__(self,CourseName,CorseCode,Session):
		self.CourseName=CourseName
		self.CourseCode=CorseCode
		self.Session=Session
		
		
class TA(object):
	def __init__(self,TAName,TUTLAB,CorseCode):
		self.TAName = TAName
		self.TUTLAB=CorseCode

class Student(object):
	def __init__(self,NickName,INDYMECH,Password,Email ):
		self.NickName=NickName
		self.INDYMECH=INDYMECH	
		self.Password=Password
		self.email=Email

class Prof(object):
	def __init__(self,ProfName,INDYMECH):
		self.ProfName=ProfName
		self.INDYMECH=INDYMECH
	

def initialize_db(db_path):
	conn = sqlite3.connect(db_path)
	#conn.execute(INITIALIZE_DB)
	#conn.commit()
	return conn


def get_tasks(db_conn):
	results = db_conn.execute("SELECT TAName FROM TA")

	task_list = []
	for taName in results:
		print(taName)
		current_task = TA(taName)
		
		task_list.append(current_task)

	return task_list


def add_forms(db_conn,CourseCode, NickName, ProfName, Session,TAName, LABTUT, FinalGrade, LevelDifficulty, WorkLoad, Interesting, OverallRating ):
	#if not recordC:
	#	return
	
	sqlInsert = "INSERT INTO Form (CourseCode, NickName, ProfName, Session,TAName, LABTUT, FinalGrade, LevelDifficulty, WorkLoad, Interesting, OverallRating) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(CourseCode, NickName, ProfName, Session,TAName, LABTUT, FinalGrade, LevelDifficulty, WorkLoad, Interesting, OverallRating)
	db_conn.execute(sqlInsert)
	db_conn.commit()


def get_forms(db_conn):
	results = db_conn.execute("SELECT * FROM Form")
	data=results.fetchall()
	#record_list = []
	#for CourseCode, NickName, ProfName, Session,TAName, LABTUT, FinalGrade, LevelDifficulty, WorkLoad, Interesting, OverallRating in results:
		#print(NickName)
	#	current_record = Form1(CourseCode, NickName, ProfName, Session,TAName, LABTUT, FinalGrade, LevelDifficulty, WorkLoad, Interesting, OverallRating)
		
	#	record_list.append(current_record)
	return data
	#return record_list
def add_course(db_conn,CourseName,CorseCode,Session):
	sqlInsert = "INSERT INTO Course (CourseName,CorseCode,Session) VALUES ('{}','{}','{}')".format(CourseName,CorseCode,Session)
	db_conn.execute(sqlInsert)
	db_conn.commit()
	

def get_Course(db_conn):
	results = db_conn.execute("SELECT * FROM Course")

	course_list = []
	for CourseName,CourseCode, Session in results:
		print(CourseName)
		current_course =Course(CourseName,CourseCode,Session)
		
		course_list.append(current_course)

def add_course(db_conn,CourseName,CorseCode,Session):
	sqlInsert = "INSERT INTO Course (CourseName,CorseCode,Session) VALUES ('{}','{}','{}')".format(CourseName,CorseCode,Session)
	db_conn.execute(sqlInsert)
	db_conn.commit()
	

def add_TA(db_conn,TAName,TUTLAB, CorseCode):
	sqlInsert = "INSERT INTO TA (TAName,TUTLAB, CorseCode) VALUES ('{}','{}','{}')".format(TAName,TUTLAB, CorseCode)
	db_conn.execute(sqlInsert)
	db_conn.commit()

def get_TA(db_conn):
	results = db_conn.execute("SELECT * FROM TA")

	ta_list = []
	for TAName,TUTLAB, CorseCode in results:
		print(TAName)
		current_TA=TA(TAName,TUTLAB, CorseCode)
		
		ta_list.append(current_TA)
		
def add_Student(db_conn,NickName,INDYMECH,Password,Email):
	sqlInsert = "INSERT INTO Student (NickName,INDYMECH,Password,Email) VALUES ('{}','{}','{}','{}')".format(NickName,INDYMECH,Password,Email)
	db_conn.execute(sqlInsert)
	db_conn.commit()

def get_Student(db_conn):
	results = db_conn.execute("SELECT * FROM Student")

	student_list = []
	for NickName,INDYMECH,Password,Email in results:
		print(NickName)
		current_Student=Student(NickName,INDYMECH,Password,Email )
		
		student_list.append(current_Student)
		
def add_Prof(db_conn,ProfName,INDYMECH):
	sqlInsert = "INSERT INTO Professor (ProfName,INDYMECH) VALUES ('{}','{}')".format(ProfName,INDYMECH)
	db_conn.execute(sqlInsert)
	db_conn.commit()

def get_Prof(db_conn):
	results = db_conn.execute("SELECT * FROM Professor")

	prof_list = []
	for ProfName,INDYMECH in results:
		print(ProfName)
		current_Prof=Prof(ProfName,INDYMECH)
		
		prof_list.append(current_Prof)



#def set_done(db_conn, task_id):
#	sqlUpdate = "UPDATE todo SET done=1 WHERE task_id={}".format(task_id,)
#	db_conn.execute(sqlUpdate)
#	db_conn.commit()

#def set_not_done(db_conn, task_id):
#	sqlUpdate = "UPDATE todo SET done=0 WHERE task_id={}".format(task_id)
#	db_conn.execute(sqlUpdate)
#	db_conn.commit()

#def remove_task(db_conn, task_id):
#	sqlDelete = "DELETE FROM todo WHERE task_id={}".format(task_id)
#	db_conn.execute(sqlDelete)
#	db_conn.commit()







#conn=initialize_db("data.sqlite")
#get_tasks(conn)


# add_form(conn,"MIE263","alice","Neal Kaw","W","Bob Zedd","0102",63,5,4,3,4)
#get_forms(conn)
#add_course(conn,"Simulation","MIE360","W")
#get_Course(conn)
#get_TA(conn)
#get_Student(conn)
#get_Prof(conn)