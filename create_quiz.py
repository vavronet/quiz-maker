import subjects

def run():
    print('You have chosen to create a quiz.\n') 

    input_text = 'Please choose the subject you want your quiz to fall under:\n'
    
    for x, y in subjects.subjects.items():
        input_text = input_text + ' - Type {} for {}\n'.format(x,y)

    subject = input(input_text)


    #Ask for subject

    #Ask for title

    #Add questions and answers

    #Save