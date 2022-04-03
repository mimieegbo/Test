def insert_sort(ls):
    for i in range(1, len(ls)):
        x = i - 1
        y = i
        while ls[x] < ls[y] and x > -1:
            ls[x], ls[y] = ls[y], ls[x]
            y -= 1
            x -= 1  # make x represent the current prev element
    return ls

ls = [10, 1, 11, 2, 9, 20, 2]
print(insert_sort(ls))