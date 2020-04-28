import config

# Function run
def run():
    print('You have chosen to create a quiz.\n') 
  
    #Ask for subject
    subject_key = get_subject()
    
    #Ask for title
    title = get_title()
    
    #Add questions and answers
    questions = get_questions()

    #Save

# Function get_subject
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
    
# Function get_title    
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

def get_questions():
    # initialize questions list
    questions = []
    no = 1

    # while loop for questions
        # Create question dictionary 
        question = {}
        # Add no
        question['no'] = no
        # Ask for body with validation
        question['body'] = get_body()
        
        choices = {}
        # While loop for choices
            # Get choice key using string.ascii_lowercase
            choice_key = x
            # Ask for choice body with validation
            choice_value = get_choice()
            # Append element to choices
            choices[choice_key] = choice_value
            # Increment the key
        # Append choices to question
        question['choices'] = choices
        # Ask for correct answer with validation
        question['answer'] = get_answer(choices.keys)
        # Append question to questions list
        questions.append(question)
        # inceremnt no
        no = no + 1
        
    return questions

def get_body():

    return ''

def get_choice():

    return ''

def get_answer(choices_keys):

    return ''