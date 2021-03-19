li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li)
print('Sorted variable:\t', s_li)
print('Original variable:\t', li)

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print('Tuple:\t', s_tup)

di = {'name': 'Lucas', 'job': 'student', 'age': None, 'os': 'Mint'}
s_di = sorted(di)
print('Dict:\t', s_di)

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '{},{},${}'.format(self.name, self.age, self.salary)


e1 = Employee('Lucas', 23, 3000)
e2 = Employee('Pedro', 24, 2000)
e3 = Employee('Joao', 35, 5000)

employees = [e1, e2, e3]

s_employees = sorted(employees, key=lambda e: e.name)

print(s_employees)
