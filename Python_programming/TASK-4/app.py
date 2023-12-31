import streamlit as st
import random
import time

# Define the choices
choices = ['rock', 'paper', 'scissors']

# Initialize scores
if 'scores' not in st.session_state:
    st.session_state['scores'] = {'user': 0, 'computer': 0}

# Game logic
def game_logic(user_choice, computer_choice):
	"""
	Determines the winner of a rock-paper-scissors game.

	Args:
		user_choice (str): The user's choice ('rock', 'paper', or 'scissors').
		computer_choice (str): The computer's choice ('rock', 'paper', or 'scissors').

	Returns:
		str: The winner of the game ('user', 'computer', or 'tie').
	"""
	if user_choice == computer_choice:
		return 'tie'
	elif (user_choice == 'rock' and computer_choice == 'scissors') or \
		 (user_choice == 'scissors' and computer_choice == 'paper') or \
		 (user_choice == 'paper' and computer_choice == 'rock'):
		return 'user'
	else:
		return 'computer'

# Streamlit app
st.title('Rock-Paper-Scissors Game')

user_choice = st.selectbox('Choose rock, paper, or scissors:', choices, key="user_choice_selectbox")
computer_choice = random.choice(choices)
result = game_logic(user_choice, computer_choice)

if st.button('Play', key="play_button"):
	with st.spinner('Playing...'):
		time.sleep(4)
		# st.empty()

	if result == 'user':
		st.session_state['scores']['user'] += 1
		st.success(f'You chose {user_choice}, computer chose {computer_choice}. You win!')
		st.balloons()
	elif result == 'computer':
		st.session_state['scores']['computer'] += 1
		st.error(f'You chose {user_choice}, computer chose {computer_choice}. You lose!')
	else:
		st.info(f'You chose {user_choice}, computer chose {computer_choice}. You tied!')