# BlackJack game
# Exercise on funcitons, modules, lists, loops, and " Nested If statement"
# focus on: Programming logic and code exercises

import os, random, string, time

# User cards list
user_cards = []

# Computer cards list
computer_cards = []

# Computer hides card list
hided_card = []

# Name of balck jack game
game_name = """

████████╗░██╗░░░░░░░██╗██╗███╗░░██╗████████╗██╗░░░██╗  ░█████╗░███╗░░██╗███████╗
╚══██╔══╝░██║░░██╗░░██║██║████╗░██║╚══██╔══╝╚██╗░██╔╝  ██╔══██╗████╗░██║██╔════╝
░░░██║░░░░╚██╗████╗██╔╝██║██╔██╗██║░░░██║░░░░╚████╔╝░  ██║░░██║██╔██╗██║█████╗░░
░░░██║░░░░░████╔═████║░██║██║╚████║░░░██║░░░░░╚██╔╝░░  ██║░░██║██║╚████║██╔══╝░░
░░░██║░░░░░╚██╔╝░╚██╔╝░██║██║░╚███║░░░██║░░░░░░██║░░░  ╚█████╔╝██║░╚███║███████╗
░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚══╝╚══════╝"""

# Sleep time func
def sleep(scond):
    time.sleep(scond)

# To clear tirminal func/ Only to exercise
def clear_terminal():
    os.system('clear' if os.name == 'poix' else 'cls')

# Snake game func
def snake_game():
    "This game func is not available, because it's for exercises"

    clear_terminal()
    print('\n\nWlcome back in snake game:*****\n')
    print('Sorry this game is not available:\nTry again later!\n')
    sleep(7)

# GTA game func/ Only to exercise
def gta_game():
    "This game func is not available, because it's for exercises"

    clear_terminal()
    print('\n\nWelcome to GTA game: ***\n')
    print('Sorry this game is not available:\nTry again later!\n')
    sleep(7)

# To Showing result of black jack game func
def display_result():
    """
    It compares the cards players values and displays the final result.
    
    """

    # Return value of the first card of computer
    computer_cards[0] = hided_card[0]

    # User points collection
    user_points = sum(user_cards)

    # Computer points collection
    computer_points = sum(computer_cards)

    # Display points and cards of computer and user
    print(f"\nYour cards: {user_cards}: Score = {user_points}\n")
    print(f'\nComputer cards: {computer_cards}: score = {computer_points}\n')

    # Resulte validations
    if user_points == 21:
        print('\nYou win in BlackJack 😊 🪙 👋 🎊 🎁\n')

    elif computer_points == 21:
        print('Computer wins in BlackJack: 😞 😔 🥺 🥹\n')

    elif user_points > 21:
        print(f"\nYou're over 21, computer wins 😞 😔 🥺 🥹\n")

    elif user_points < 21 and computer_points < 21:
            
            if computer_points > user_points:
                print('\nComptuer wins 😞 😔 🥺 🥹\n')

            elif computer_points < user_points:
                print('\nYou win 😊 🪙 👋 🎊 🎁\n')

            else:
                print('\nDraw 🥺\n')
    else:
        print('\nComputer over 21, you are the big winner 😊 🪙 👋 🎊 🎁\n')


    input('\nPress enter to exit👋......')

# Generates cards func
def create_card():
    """
    Generates a card number and returns --> an int(nubmer) value
    """
    card = random.choices(string.digits, k= 1)

    # Add a one so it doesn't return a zero value
    return int(card[0]) +1

# divide cards func
def divide_cards(withdraw):
    """
    It taks a parameter of user withdrawing choice to know wihce player should has a new card.
    It deals the cards and hides the first value of the computer cards [ X ].
    
    """

    # Deal the first 2 cards of computer and user
    if len(user_cards) < 2 and len(computer_cards) < 2:

        for _ in range(2):
            user_cards.append(create_card())
            computer_cards.append(create_card())
        # Hide the first card number of computer and append it to it's list
        hided_card.append(computer_cards[0])    
        computer_cards[0] = 'X'

    # If withdrawing [y] deal user a new card
    if withdraw == 'y':

        user_cards.append(create_card())

    # If user withdrawing choice [n] deal cards to computer list until it has 18 points or more.
    if withdraw == 'n':

        # Returns the original [0] index value of computer cards
        computer_cards[0] = hided_card[0]

        # Deal cards until computer has 18 or more points
        while sum(computer_cards) < 18:
            
            # Increase a new card to computer list
            computer_cards.append(create_card())

            # Convert [1] to [11] if the sum ot computer points < 12
            if 1 in computer_cards and sum(computer_cards) < 12:

                index_1 = computer_cards.index(1)
                computer_cards[index_1] = 11

# BlackJack game func
def black_jack_game():
    """
    It start the BlackJack game, When it called
    
    """

    clear_terminal()

    # Display game's name
    print('\n\nWelcome in : \n\n',game_name)
    print('\n\nGame initializing....\n\n')
    sleep(4)

    # Deal the first [2] cards to the computer and the user
    divide_cards(withdraw= "")

    # If the user cards sum smaller than 21 stay looping
    while sum(user_cards) < 21:

        clear_terminal()

        # If finding one in user cards and the total points less than 12 asks to convert 1 to [11]
        if 1 in user_cards and sum(user_cards) < 12:

            # Check if user wants to convert the one to [11] and if he enters the accepted value
            while True:
                clear_terminal()

                # Display the user and computer cards and only the sum of user points
                print(f"\nYour cards: {user_cards}\n\nComputer cards: {computer_cards}")
                print(f'\nYour total points: {sum(user_cards)} ')

                # Ask user if wants to convert 1 ot 11
                converting = input('\nConvert 1 to 11? Type [y] or [n]:  ')

                if converting.lower() == 'y':
                    
                    # get the index of 1 to convert it
                    index_of_1 = user_cards.index(1)

                    # convert one to 11
                    user_cards[index_of_1] = 11

                    break
                
                # If choosing [n] stop looping
                elif converting == 'n':
                    break
                
                # If user choice not accepted loop again
                else:
                    print(f"\nInvalid entry: {converting}\n\n")
                    sleep(2)


        clear_terminal()

        # Display the user points and cards of the user and computer
        print(f"\nYour cards: {user_cards}\n\nComputer cards: {computer_cards}")
        print(f'\nYour total points: {sum(user_cards)} ')

        # If total points of user stay < 21, Ask hem if wants to withdraw again
        if sum(user_cards) < 21:

            # Ask to withdrawing
            withdrawing = input('\nDo you want to withdraw? y/n  ').lower()

            if withdrawing == 'y':

                # Increase a new point card to the user
                divide_cards(withdraw= 'y')

            elif withdrawing == 'n':


                # Increase points to the computer until it has 18 and stop looping
                divide_cards(withdraw= 'n')

                break

                # If entry not accepted loop again
            else:
                print(f'\nInvalid entry: {withdrawing}\n\n')
                sleep(2) 

    clear_terminal()

    # Make comparing and display the results
    display_result()

# To ask user of new game when the game finish
def ask_new_game():
    """
    Asks user if wants to play agin and returns [y] or [n]. If input is incorrect it loops again until into good chooice.
    
    """
    # Stay looping until get an accepted input
    while True:

        clear_terminal()
        
        # Ask user if wants to play again
        new_game = input('\nDo you want to play again? y/n   ').lower()

        if new_game == 'y':
            return 'y'

        elif new_game == 'n':
            
            return 'n'

        else:
            print(f'\nInvalid entry: {new_game}\n')
            sleep(2)

clear_terminal()

game_on = True

# Start looping
while game_on:
    clear_terminal()

    # Show options if the game starts over or if it's currently starts
    if not user_cards:
        print('''
            1. Black jack game
            2. Snake game
            3. GTA game''')
    
    # User choice of number game
    game_choice = input('\nChoose the game number:  ')
        
    # Check if the entered value is acceptable
    if not game_choice.isdigit():
        print(f'Invalide entry: ({game_choice}) *****\n')
        print('\nReasons --> accepted [1, 2, 3] else [ false ]\n\n')
        sleep(3)
        clear_terminal()
    else:
        # Convert the game_choice to int(number)
        int_game_choice = int( game_choice ) 

        if int_game_choice == 1:
            black_jack_game()
         
        elif int_game_choice == 2:
            snake_game()
            
        elif int_game_choice == 3:
            gta_game()

        else:
            print('\nInvalide choice: Try again***\n')
            sleep(4)
            clear_terminal()
            game_choice = False

        # If choice is True then the user is already has been played a game
        if game_choice:
            
            # Ask user if want to play again
            # If returns [y]
            if ask_new_game() == 'y':

                # Empty the lists to prepare for a new game.
                user_cards = []
                computer_cards = []
                hided_card  = []

            # If reutrns [n] Stop the game
            else:
                game_on = False
                print('\nThanks for using our platform\n')
                sleep(2)

#** ( FINISHED IN 5 SEP 2024) ** 