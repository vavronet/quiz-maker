import config

def run():
    print('You have chosen to create a quiz.\n') 
  
    #Ask for subject
    subject_key = get_subject()
    
    #Ask for title
    title = get_title()
    
    #Add questions and answers

    #Save

def get_subject():
    input_text = 'Please choose the subject you want your quiz to fall under:\n'
    
    for x, y in config.subjects.items():
            input_text = input_text + ' - Type {} for {}\n'.format(x,y)

    valid_subject = False

    while valid_subject == False: 
        subject_key = input(input_text)

        if subject_key in config.subjects.keys():
            print('Your SUBJECT is {}\n'.format(config.subjects[subject_key]))
            valid_subject = True
        else:
            print('This is not one of the options, try again.\n')

    return subject_key
    
def get_title():
    valid_title = False

    while valid_title == False: 
        title = input('Enter the title of your test below\n')

        if len(title.strip()) >= config.min_title:
            print('The TITLE of you test is {}\n'.format(title))
            valid_title = True
        else:
            print('Your title is invalid, try again.\n')
    
    return title

    