contacts = {
    'number': 4,
    'students':
        [
            {'name':'Martina Balestrin', 'email':'martina@example.com'},
            {'name':'Kang Seulgi', 'email':'seulgi@example.com'},
            {'name':'Oh Haewon', 'email':'haewon@example.com'}
        ]
}

print("Student emails:")
for student in contacts['students']:
    print(student['email'])