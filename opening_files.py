file = open('Insertion_sort.py', 'a')

text = '\nprint(\'hello\')\n'

file.write(text)
file.close()

file = open('Insertion_sort.py', 'r')

for i in range(21):
    print(file.readline()[:-1])



