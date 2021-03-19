courses = ['History', 'Math', 'Physics', 'CompSci']

nums = [1, 5, 2, 4, 3]

print(courses[:2])

courses.insert(0, 'Art')
print(courses)

courses.sort()
print(courses)

nums.sort(reverse=True)
print(nums)

for index, course in enumerate(courses, start=1):
    print(index, course)
 
course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
print(tuple_1)

set_1 = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(set_1)