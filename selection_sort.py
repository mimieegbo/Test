# from randomise import gen_random

def select_sort(ls):
    lse = []
    ls = ls.copy()

    while ls:
        minimum, index = mini(ls)
        lse.append(minimum)
        del(ls[index])

    return lse

def mini(ls):
    min = ls[0], 0
    for i in range(1, len(ls)):
        curr_value = ls[i]
        if curr_value < min[0]:
            min = curr_value, i

    return min


print(select_sort([10, -1, 1, 3, 35, 10, 5]))