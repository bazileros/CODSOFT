import streamlit as st

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Error! Division by zero'

st.set_page_config(page_title="Simple :red[Calculator]", page_icon=":iphone:", layout="centered")
st.title("Simple Calculator 📲")

# Create a form
with st.form(key='my_form'):
    # Input numbers
    num1 = st.number_input("Enter first number", value=0)
    num2 = st.number_input("Enter second number", value=0)

    # Choose operation
    operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Calculate button
    submit_button = st.form_submit_button(label='Calculate')

if submit_button:
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    st.success(f"The result is {result}")