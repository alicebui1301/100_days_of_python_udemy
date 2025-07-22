# Display art for a game
logo_1 = f"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/  
"""

logo_2 = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

import random
from lower_game_data import data

# Format the account data into printable format.
def format_data(account):
    """Format the account data into printable format."""
    return f"{account['name']}, a {account['description']}, from {account['country']}."

# Check if user is correct.
## Get followers and compare with the other account.
## Record their score & give user feedback on their guess.
def check_answer(guess, account_a, account_b):
    """Check if the user's guess is correct."""
    followers_a = account_a['follower_count']
    followers_b = account_b['follower_count']
    if guess == 'A':
        if followers_a > followers_b:
            return True
        else:
            return False
    elif guess == 'B':
        if followers_b > followers_a:
            return True
        else:
            return False

def lower_game():
    """Run the Lower Game."""
    should_continue = True
    score = 0
    account_b = random.choice(data)
    while should_continue == True:
        # Generate a random account from the game data. 
        # Make account at position B become the next account at position A.
        account_a = account_b
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)
        text_a = f"Compare A: {format_data(account_a)}"
        text_b = f"Against B {format_data(account_b)}"

        # Display the art and account data.
        print(logo_1)
        print(text_a)
        print(logo_2)
        print(text_b)

        # Ask the user to guess.
        guess = input(f"Who has more followers? Type 'A' or 'B': ").upper()

        # Clear the screen (optional, for better UX).
        print("\n" * 100)  # This is a simple way to clear the screen in a console.

        # Check if the user is correct.
        # If correct, increase score by 1 and continue the game.
        # If wrong, end the game and display the final score.
        is_correct = check_answer(guess, account_a, account_b)
        if is_correct == True:
            score += 1
            print(f"You guessed right! Your current score is {score}.")
        else:
            should_continue = False
            print(logo_1)
            print(f"You guessed wrong! Your final score is {score}.") 

lower_game()