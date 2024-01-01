# Python
import streamlit as st
import sqlite3

def create_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone TEXT, email TEXT, address TEXT)')
    conn.close()

def add_contact(name, phone, email, address):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)', (name, phone, email, address))
    conn.commit()
    conn.close()

def view_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts')
    data = c.fetchall()
    conn.close()
    return data

def search_contact(name):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts WHERE name = ? OR phone = ?', (name, name))
    data = c.fetchall()
    conn.close()
    return data

def update_contact(name, phone, email, address):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('UPDATE contacts SET phone = ?, email = ?, address = ? WHERE name = ?', (phone, email, address, name))
    conn.commit()
    conn.close()

def delete_contact(name):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('DELETE FROM contacts WHERE name = ?', (name,))
    conn.commit()
    conn.close()

st.title('Contact Book')

create_table()

menu = ["Add Contact", "View Contacts", "Search Contact", "Update Contact", "Delete Contact"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Contact":
    st.subheader("Add a New Contact")
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    address = st.text_input("Address")
    if st.button("Add"):
        add_contact(name, phone, email, address)
        st.success("Contact added")

elif choice == "View Contacts":
    st.subheader("View All Contacts")
    contacts_info = view_contacts()
    for contact in contacts_info:
        st.text(contact)

elif choice == "Search Contact":
    st.subheader("Search a Contact")
    name = st.text_input("Enter the Name or Phone")
    if st.button("Search"):
        contact_info = search_contact(name)
        if contact_info:
            for contact in contact_info:
                st.text(contact)
        else:
            st.error("Contact not found")

elif choice == "Update Contact":
    st.subheader("Update a Contact")
    name = st.text_input("Name")
    phone = st.text_input("New Phone")
    email = st.text_input("New Email")
    address = st.text_input("New Address")
    if st.button("Update"):
        update_contact(name, phone, email, address)
        st.success("Contact updated")

elif choice == "Delete Contact":
    st.subheader("Delete a Contact")
    name = st.text_input("Name")
    if st.button("Delete"):
        delete_contact(name)
        st.success("Contact deleted")