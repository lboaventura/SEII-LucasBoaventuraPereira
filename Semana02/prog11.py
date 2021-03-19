f = open("test.txt", "r")
print(f.name)
print(f.mode)
f.close()

with open("test.txt", "r") as f:
    for line in f:
        print(line, end='')
    print()

print(f.closed)

with open("test2.txt", "w") as f:
    f.write("Test")
    f.seek(0)
    f.write("Testing")

with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)