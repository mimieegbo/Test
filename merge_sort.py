from randomise import gen_random_list
from math import inf

def merge_sort(ls):
    if len(ls) == 1:
        return ls

    part1 = merge_sort(ls[:len(ls)//2])
    part2 = merge_sort(ls[len(ls)//2:])
    merge_list = []

    i = 0
    j = 0

    while i < len(part1) or j < len(part2):
        part1val = part1[i] if i < len(part1) else inf
        part2val = part2[j] if j < len(part2) else inf

        if part1val < part2val:
            merge_list.append(part1[i])
            i += 1
        else:
            merge_list.append(part2[j])
            j += 1

    return merge_list


if __name__ != "__main__":
    pass
else:
    testcases = [gen_random_list(6) for i in range(10)]

    for test in testcases:
        print(test, 'is sorted to become --->', merge_sort(test))


