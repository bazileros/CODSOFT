import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page


HOMEPAGE_TEXT = """
# Welcome to Task Planner

Welcome to **Task Planner**, your go-to task planner app for efficient and organized daily living! 🚀

**Task Planner** is designed to be your personal task management companion, helping you stay on top of your to-do list with ease. Say goodbye to missed deadlines and hello to productivity!

## Key Features

- 📒 **Create Tasks Quickly:** Easily add new tasks with a few simple clicks. Set due dates and priorities effortlessly.

- 📌 **View and Update Tasks:** Seamlessly manage your tasks with the ability to view and update them as needed.

- 🗑️ **Delete with Ease:** Remove completed or irrelevant tasks effortlessly with our user-friendly delete feature.

- ✏️ **Efficient CRUD Operations:** **Task Planner** focuses on the fundamental CRUD operations—Create, Read, Update, and Delete—to streamline your task management experience.

- 📲 **Sync Across Devices:** Access your tasks anywhere, anytime. **Task Planner** ensures your tasks are synchronized across all your devices for convenience.

- 🔒 **Secure and Private:** Your task data is kept secure and private. **Task Planner** prioritizes the confidentiality of your information.

Ready to simplify your task management? Hit the "Get Started" button below and start organizing your tasks with **Task Planner**! 🚀

"""

BACKGROUND = """
<style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://images.unsplash.com/photo-1544365558-35aa4afcf11f?q=80&w=1472&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: 180%;
        background_position: top left;
        background-repeat: no-repeat;
        background_attachment: local;
}}
</style>
"""

def main():
    st.set_page_config(page_title="Task Planner",
                    page_icon="🚀",
                    layout="centered",
                    menu_items=None,
                    initial_sidebar_state="collapsed")
    st.markdown(BACKGROUND, unsafe_allow_html=True)
    st.markdown(HOMEPAGE_TEXT)
    add_vertical_space(2)
    get_started_button = st.button("Get Started")
    if get_started_button:
        switch_page("New_Task")

if __name__ == "__main__":
    main()