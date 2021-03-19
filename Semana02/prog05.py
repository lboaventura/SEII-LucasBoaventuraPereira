student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['phone'] = '555-5555'

del student['age']

for key, value in student.items():
    print(key, value)
