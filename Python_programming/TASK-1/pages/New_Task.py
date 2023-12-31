import streamlit as st
import pandas as pd
from db_funcs import create_table, add_data, view_all_data, view_all_task_names, get_task, get_task_by_status, edit_task_data, delete_data
import streamlit_shadcn_ui as ui


def new_task():
	with st.form(key="new_task_form"):
		t_name = st.text_input("Task Name", key="tsk_name")
		t_desc = st.text_area("Task Description",key="desc")
		t_prio = st.selectbox("Task Priority", ["Low", "Medium", "High"], key="prio")
		t_status = st.selectbox("Task Status", ["New", "In Progress", "Completed"],key="status")
		t_date = st.date_input("Due Date", key="date")
		submit_btn = st.form_submit_button(label="Create Task")
		if submit_btn:
			add_data(t_name,t_desc,
            t_prio, t_status, t_date)
			st.success("Task Created Successfully")
			st.balloons()


def view_task():
	show = ui.switch(default_checked=True, label="View All")
	if show == True: 
			result = view_all_data()
			clean_df = pd.DataFrame(result,columns=["Task Name", "Task Description", "Task Priority","Task Status","Due Date"])
			st.dataframe(clean_df, use_container_width=True)


def update_task():
	st.subheader("Edit Items")
	show = ui.switch(default_checked=True, label="Update")
	if show == True:
		result = view_all_data()
		clean_df = pd.DataFrame(result,columns=["Task Name","Task Description", "Task Priority", "Task Status", "Due Date"])
		st.dataframe(clean_df)

	list = [i[0] for i in view_all_task_names()]
	selected = ui.select("Task",list)
	t_result = get_task(selected)

	if t_result:
		t_name = t_result[0][0]
		t_desc = t_result[0][1]
		t_prio = t_result[0][2]
		t_status = t_result[0][3]
		t_date = t_result[0][4]
	
	with st.form(key="update_task_form"):
		t_name1 = st.text_input("Update Name", key="tsk_name1")
		t_desc1 = st.text_area("Update Description",key="desc1")
		t_prio1 = st.selectbox("Update Priority", ["Low", "Medium", "High"], key="prio1")
		t_status1 = st.selectbox("Update Status", ["New", "In Progress", "Completed"],key="status1")
		t_date1 = st.date_input("Update Due Date", key="date1")
		submit_btn1 = st.form_submit_button(label="Update")
		if submit_btn1:
			if t_name1 and t_desc1 and t_prio1 and t_status1 and t_date1:
				edit_task_data(t_name1,t_desc1,
				t_prio1, t_status1, t_date1, t_name, t_desc, t_prio, t_status, t_date)
				st.success(f"Updated ::{t_name} ::To {t_name1}")
				st.balloons()
				st.empty()

				if ui.switch(default_checked=True, label="View Updated Tasks"):
					result = view_all_data()
					clean_df = pd.DataFrame(result,columns=["Task Name", "Task Description", "Task priority","Task Status","Due Date"])
					st.dataframe(clean_df)
			else:
				st.warning("Empty Fields Cannot Be Submitted")


def delete_task():
	st.subheader("Delete")
	show = ui.switch(default_checked=True, label="Delete")
	if show == True:
		result = view_all_data()
		clean_df = pd.DataFrame(result,columns=["Task Name","Task Description","Task Priority","Task Status","Due Date"])
		st.dataframe(clean_df)

	unique_list = [i[0] for i in view_all_task_names()]
	delete_by_task_name =  st.selectbox("Select Task",unique_list)
	if st.button("Delete"):
		delete_data(delete_by_task_name)
		st.warning("Deleted: '{}'".format(delete_by_task_name))

	if ui.switch(default_checked=False, label="View Updated Tasks"):
		result = view_all_data()
		clean_df = pd.DataFrame(result,columns=["Task Name", "Task Description","Task Priority","Task Status","Due Date"])
		st.dataframe(clean_df)


def main():
	st.set_page_config(page_title="Manage | Tasks",
					page_icon="🚀",
					layout="centered",
					menu_items=None,
					initial_sidebar_state="collapsed"
	)
	st.title("Task Planner 🚀")
	st.header("Manage Tasks with Ease")
	tabs = ui.tabs(options=["New ✏️", "View 📂", "Update 🔑", "Delete 🗑️"],
				default_value="New Task", key="tabs")
	create_table()
	if tabs == "New ✏️":
		new_task()
	elif tabs == "View 📂": 
		view_task()
	elif tabs == "Update 🔑":
		update_task()
	elif tabs == "Delete 🗑️":
		delete_task()



if __name__ == "__main__":
	main()