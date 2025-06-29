import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

def deal_card():
    """
    Returns a random card from the deck.
    The deck consists of numbers 2-10, face cards (J, Q, K) all valued at 10, and Aces valued at 11.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  
    return random.choice(cards)

def calculate_score(cards):
    """
    Calculates the score of the given cards.
    - If the score is 21, it returns 0 (Blackjack).
    - If the cards contain an Ace (11) and the score exceeds 21, it converts the Ace to 1.
    - Otherwise, it returns the sum of the cards.
    - If the cards are [10, 11] or [11, 10], remove 11 and append 1 to treat it as Blackjack.
    """
    score = sum(cards)
    if score == 21 or (cards == [10, 11] or cards == [11, 10]):
        score = 0
    elif 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare_scores(user_score, computer_score):
    """
    Compares the user's score with the computer's score and returns a message indicating the result of the game.
    - If both scores are equal, it's a draw.
    - If the user has a score of 0, they win with Blackjack.
    - If the computer has a score of 0, the user loses to Blackjack.
    - If the user goes over 21, they lose.
    - If the computer goes over 21, the user wins.
    - If the user's score is greater than the computer's score, the user wins.
    - Otherwise, the user loses.
    """
    if user_score == computer_score:
        message = "It's a draw!"
    elif user_score == 0:
        message =  "Blackjack! You win!"
    elif computer_score == 0:
        message =  "Computer has Blackjack! You lose!"
    elif user_score > 21:
        message =  "You went over. You lose!"
    elif computer_score > 21:
        message =  "Computer went over. You win!"
    elif user_score > computer_score:
        message = "You win!"
    else:
        message = "You lose!"
    return message

def back_jack():
    """
    Main function to play the Blackjack game.
    - Deal cards, calculate scores.
    - Ask the user if they want to add another card. If no, then the game ends.
    - The computer will draw cards until its score is at least 17.
    - The score is re-calculated when a new card is added.
    - Compare scores and determine the winner.
    - Ask the user if they want to play again.
    """

    print("Welcome to Blackjack!")
    print("The goal is to get as close to 21 as possible without going over.\n")

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}\n")

    while not is_game_over:
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == 'n':
                is_game_over = True
            elif choice == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"Your cards: {user_cards}, current score: {user_score}")
    
        while computer_score < 17 and computer_score != 0:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
    
        print(compare_scores(user_score, computer_score))
    
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}\n")
    
    restart = input("Do you want to play again? Type 'y' or 'n': \n")
    if restart == 'y':
        back_jack()
    else:
        print("Thanks for playing! Goodbye!")

back_jack()