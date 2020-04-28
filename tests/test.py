subjects = {
    '1': 'Math',
    '2': 'History',
    '3': 'Science',
    '4': 'Music',
    '5': 'Cartoon References',
}

# print(subjects['3'])

# for x, y in subjects.items():
#    print('{} ({})'.format(y,x))

# for x in subjects.keys():
#     print(x)

choice = '2'

# print(subjects[choice])

thing = ' h e l l o '
# print(thing.strip())

quiz = {
    'subject': '1',
    'title': 'Math Quiz',
    'author': 'bob',
    'no_choices': 3,
    'questions': [
        {
            'no': 1,
            'body': 'What is 7x9?',
            'choices': {
                'a': '54',
                'b': '64',
                'c': '63'
            },
            'answer': 'c'
        },
        {
            'no': 2,
            'body': 'What is 12/6?',
            'choices': {
                'a': '4',
                'b': '2',
                'c': '3'
            },
            'answer': 'b'
        },
        {
            'no': 3,
            'body': 'What is 95-15?',
            'choices': {
                'a': '75',
                'b': '80',
                'c': '90'
            },
            'answer': 'b'
        }
    ]
}

# Print title 
print('Quiz title: {}'.format(quiz['title']))

# Print subject
print('Subject: {}\n'.format(subjects[quiz['subject']]))

# Print questions
# 1) What is 7x9?
# a. 54
# b. 64
# c. 63
# Correct answer: c

for z in quiz['questions']:
    print('{}) {}'.format(z['no'], z['body']))

    for x, y in z['choices'].items():
        print('{}. {}'.format(x,y))

    print('Correct answer: {}\n'.format(z['answer']))
