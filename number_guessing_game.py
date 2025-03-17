import streamlit as st  
import random  

# Function to start a new game
def start_game():
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_active = False


if "random_number" not in st.session_state:
    start_game()


st.title("🎯 Number Guessing Game")
st.markdown(
    """
    <div style='text-align: center; border: 1px solid #4CAF50; background-color: #f9f9f9; border-radius: 10px; height: 50px; display: flex; align-items: center; justify-content: center;'>
        <h2 style='color: #4CAF50; margin: 0;'>Assignment 02 - Streamlit App</h2>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("Guess the random number!")

# Difficulty selection radio button
difficulty = st.radio("Select Options Below According to your choice:", ["Easy (1-100)", "Medium (1-500)", "Hard (1-1000)", "Custom"], index=0)

if difficulty == "Easy (1-100)":
    max_range = 100
elif difficulty == "Medium (1-500)":
    max_range = 500
elif difficulty == "Hard (1-1000)":
    max_range = 1000
else:
    max_range = st.number_input("Enter Custom Range:", min_value=10, max_value=10000, step=10, value=100)

# Start Game Button
if st.button("Start Game"):
    st.session_state.random_number = random.randint(1, max_range)
    st.session_state.attempts = 0
    st.session_state.game_active = True
    st.session_state.max_range = max_range

# Game logic
if st.session_state.game_active:
    user_guess = st.number_input(f"Guess a number between 1 and {st.session_state.max_range}", min_value=1, max_value=st.session_state.max_range, step=1)
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if user_guess < st.session_state.random_number:
            st.write("Too low! Try again.")
        elif user_guess > st.session_state.random_number:
            st.write("Too high! Try again.")
        else:
            st.write(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
            st.session_state.game_active = False

# Reset Button
if st.button("Reset Game"):
    start_game()
    st.write("Game reset! Try again.")
