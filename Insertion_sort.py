from randomise import randomise

print('and the name of this process is', __name__)


def insert_sort(ls):
    for i in range(1, len(ls)):
        x = i - 1
        y = i
        while ls[x] < ls[y] and x > -1:
            ls[x], ls[y] = ls[y], ls[x]
            y -= 1
            x -= 1  # make x represent the current prev element
    return ls


testcases = [randomise([1, 3, 35, 5, 10, -1, 10]) for i in range(10)]
print(testcases)
for ls in testcases:
    print(insert_sort(ls))

print('hello')

print('hello')

print('hello')

print('hello')

print('hello')
