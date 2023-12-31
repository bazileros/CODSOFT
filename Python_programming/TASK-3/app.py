import streamlit as st
import random
import string
import hashlib

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def generate_password_from_phrase(phrase):
    return hashlib.sha256(phrase.encode()).hexdigest()

st.title('Password Generator')

password_length = st.slider('Password length', min_value=8, max_value=128, value=12, step=1)
generate_button = st.button('Generate Password')

phrase = st.text_input('Enter a phrase')
generate_from_phrase_button = st.button('Generate Password from Phrase')

if generate_button:
    password = generate_password(password_length)
    st.text_input('Generated Password', value=password, type='password')

if generate_from_phrase_button:
    password = generate_password_from_phrase(phrase)
    st.text_input('Generated Password from Phrase', value=password, type='password')