print('Welcome to Quiz Maker, a program where you can make and take quizes and tests.\n')

name = input('Please enter your name: \n')
print('Hello, '+name+'!\n')
choice = input('Select your choice: \n - Type 1 to create a quiz \n - Type 2 to take a quiz\n')

if choice == '1':
    print('You have chosen to create a quiz.')
elif choice == '2':
    print('You have chosen to take a quiz.')
else:
    print('That is not a valid option, please try again.')


    