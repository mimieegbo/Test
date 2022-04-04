from random import choice, randint


def randomise(ls):
    """
    :param ls: list type
    :return: and returns a randomised version
    """
    lse = []
    ls = ls.copy()

    while ls:
        ch = choice(ls)
        lse.append(ch)
        ls.remove(ch)

    return lse


def gen_random_list(length_of_ls=None):
    ls = []

    if length_of_ls == None:
        length_of_ls = randint(0, 10)
    for i in range(length_of_ls):
        ls += [randint(-100, 100)]
    return ls


if __name__ == "__main__":
    ls = (1, 3, 5, 5, 5)
    print(randomise(ls))
    print(ls)
    gen_random_list()

print('name of the randomise python process is', __name__)
