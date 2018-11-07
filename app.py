# imports
from flask import Flask, render_template, request, redirect, g
import todo_db


# Define a path for the database
DATABASE_PATH = "data.db"

# create a Flask app
app = Flask(__name__)

def get_db_conn():
	if not hasattr(g, "_db_conn"):
		g._db_conn = todo_db.initialize_db("data.db")
	return g._db_conn

# Welcome page. Accessible at <server-address>/
@app.route('/')
def welcome_page():
    return render_template('main.html')

# Todo list page. Accessible at <server-address>/todo
@app.route('/IndyCourses')
def todo_list():
	#db_conn = get_db_conn()
	#task_list = todo_db.get_tasks(db_conn)
	return render_template('indyCourses.html')

@app.route('/thirdYearCourse')
def thirsYearCourse():
	#db_conn = get_db_conn()
	#task_list = todo_db.get_forms(db_conn)
	return render_template('thirdYearCourse.html')

@app.route('/form')
def form():
	#db_conn = get_db_conn()
	#task_list = todo_db.get_tasks(db_conn)
	return render_template('form.html')

# Handles add task request. The task details are submitted by a HTML form with an action="/add".
# This function extract the form field "title" and callls the app function add_task
@app.route('/add', methods=['GET'])
def add_form():
	CourseCode = request.args.get('CourseCode')
	NickName = request.args.get('NickName')
	ProfName = request.args.get('ProfName')
	Session = request.args.get('Session')
	TAName = request.args.get('TA Name')
	LabTut = request.args.get('Lab/Tut')
	FinalGrade = request.args.get('Final Grade')
	LoD = request.args.get('Level of Difficulty')
	workload = request.args.get('workload')
	interesting = request.args.get('interesting')
	OverallRating = request.args.get('Overall Rating')
	db_conn = get_db_conn()
	todo_db.add_forms(db_conn,CourseCode,NickName, ProfName,Session,TAName,LabTut,FinalGrade,LoD,workload,interesting,OverallRating)
	return redirect("/reviews", code=307)

@app.route('/reviews')
def display():
	db_conn = get_db_conn()
	review_list = todo_db.get_forms(db_conn)
	
	return  render_template('reviews.html', review_list=review_list)


# Handles requests to mark task as done.
# The task id of the task to be marked as done is passed using the URL, e.g., /set_done/123 is a request to mark task 123 as done.
# After the database is updated, we redirect the user back to the (updated) todo page
@app.route('/set_done/<task_id>')
def done(task_id):
	db_conn = get_db_conn()
	todo_db.set_done(db_conn, task_id)
	return redirect("/todo", code=307)

# Handles requests to mark task as not done.
# The task id of the task to be marked as not done is passed using the URL, e.g., /set_not_done/123 is a request to mark task 123 as not done.
# After the database is updated, we redirect the user back to the (updated) todo page
@app.route('/set_not_done/<task_id>')
def not_done(task_id):
	db_conn = get_db_conn()
	todo_db.set_not_done(db_conn, task_id)
	return redirect("/todo", code=307)

# Handles remove task request.
# The task id of the task to be removed is passed using the URL, e.g., /remove_task/123 is a request to remove task 123.
# After the task is removed from the database, we redirect the user back to the (updated) todo page
@app.route('/remove_task/<task_id>')
def remove_task(task_id):
	db_conn = get_db_conn()
	todo_db.remove_task(db_conn, task_id)
	return redirect("/todo", code=307)


if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
	
	
