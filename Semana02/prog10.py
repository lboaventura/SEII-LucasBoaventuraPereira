import os

print(os.getcwd())

os.mkdir('Test')

print(os.stat('test.txt'))

for dirpath, dirnames, filenames in os.walk('../'):
    print("Current path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
    print()

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)