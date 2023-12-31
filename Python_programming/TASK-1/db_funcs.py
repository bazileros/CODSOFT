import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table():
	"""
	Create a table called 'todo_table' if it doesn't already exist.
	The table has columns for name, description, status, and due date.
	"""
	c.execute('CREATE TABLE IF NOT EXISTS todo_table(name TEXT,desc TEXT,prio TEXT,status TEXT,due_date DATE)')


def add_data(name, desc, prio, status, due_date):
	"""
	Add data to the todo_table.

	Args:
		name (str): The name of the task.
		desc (str): The description of the task.
		status (str): The status of the task.
		due_date (date): The due date of the task.

	Returns:
		None
	"""
	c.execute('INSERT INTO todo_table(name,desc,prio, status, due_date) VALUES (?,?,?,?,?)', (name, desc,prio, status, due_date))
	conn.commit()


def view_all_data():
	"""
	Retrieve all data from the todo_table.

	Returns:
		list: A list containing all the data from the todo_table.
	"""
	c.execute('SELECT * FROM todo_table')
	data = c.fetchall()
	return data

def view_all_task_names():
	"""
	Retrieve all distinct task names from the todo_table.

	Returns:
		A list of task names.
	"""
	c.execute('SELECT DISTINCT name FROM todo_table')
	data = c.fetchall()
	return data

def get_task(name):
	"""
	Retrieve a task from the todo_table based on the given name.

	Args:
		name (str): The name of the task to retrieve.

	Returns:
		list: A list of tuples representing the retrieved task(s) from the todo_table.
	"""
	c.execute(f'SELECT * FROM todo_table WHERE name="{name}"')
	data = c.fetchall()
	return data

def get_task_by_status(status):
	"""
	Retrieve tasks from the todo_table based on the given status.

	Args:
		status (str): The status of the tasks to retrieve.

	Returns:
		list: A list of tasks matching the given status.
	"""
	c.execute(f'SELECT * FROM todo_table WHERE status="{status}"')
	data = c.fetchall()


def edit_task_data(new, n_desc, n_prio, n_status, n_date, name, desc, prio, status, due_date):
	"""
	Update the task data in the todo_table.

	Args:
		new (str): The new name for the task.
		new_status (str): The new status for the task.
		new_date (str): The new due date for the task.
		name (str): The current name of the task.
		status (str): The current status of the task.
		due_date (str): The current due date of the task.

	Returns:
		list: The updated task data.

	"""
	c.execute("UPDATE todo_table SET name=?, desc=?, prio=?, status=?, due_date=? WHERE name=? and desc=? and prio=? and status=? and due_date=?", (new, n_desc, n_prio, n_status, n_date, name, desc, prio, status, due_date))
	conn.commit()
	data = c.fetchall()
	return data


def delete_data(name):
	"""
	Delete data from the todo_table based on the given name.

	Args:
		name (str): The name of the data to be deleted.

	Returns:
		None
	"""
	c.execute(f'DELETE FROM todo_table WHERE name="{name}"')
	conn.commit()