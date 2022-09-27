

with open("c:/Python/programming.txt", 'r') as rf:
    with open("test_copy.txt", 'w') as wf:
        for line in rf:
            wf.write(line)
            