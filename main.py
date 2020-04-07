import game_intro
import create_quiz
import take_quiz

# Game intro - welcome screen and description
game_intro.run()

# User registration
name = input('Please enter your name: \n')
print('Hello, '+name+'!\n')
    
is_quit = False

while is_quit == False:
    #Make a choice
    choice = input('\nSelect your choice: \n - Type 1 to create a quiz \n - Type 2 to take a quiz\n - Type anything else to quit\n\n')

    if choice == '1':
        create_quiz.run()
    elif choice == '2':
        take_quiz.run()
    else:
        is_quit = True
        print('Goodbye!')


    
