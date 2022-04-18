class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) \
                 + ', ' + str(self.weight) + '>'
        return result


def value(item):
    return item.getValue()


def weightInverse(item):
    return 1.0 / item.getWeight()


def density(item):
    return item.getValue() / item.getWeight()


def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items


def getBinaryRep(n, numDigits):
    """Assumes n and numDigits are non-negative ints
    Returns a str of length numDigits that is a binary
    representation of n"""
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    if len(result) > numDigits:
        raise ValueError('not enough digits')
    for _ in range(numDigits - len(result)):
        result = '0' + result
    return result


def genPowerset(L):
    """Assumes L is a list
    Returns a list of lists that contains all possible
    combinations of the elements of L. E.g., if
    L is [1, 2] it will return a list with elements
    [], [1], [2], and [1,2]."""
    powerset = []
    for i in range(0, 2 ** len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = []
        for j in range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset


def greedy(items, maxWeight, keyFunction):
    """Assumes Items a list, maxWeight >= 0,
    keyFunction maps elements of Items to numbers"""
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalWeight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()

    return result, totalValue


def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight, keyFunction)
    print('Total value of items taken is', val)
    for item in taken:
        print('   ', item)


def testGreedys(maxWeight=20):
    items = buildItems()
    print('Use greedy by value to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, value)
    print('\nUse greedy by weight to fill knapsack of size',
          maxWeight)
    testGreedy(items, maxWeight, weightInverse)
    print('\nUse greedy by density to fill knapsack of size',
          maxWeight)
    testGreedy(items, maxWeight, density)


def Value(items):
    return sum([item.getValue() for item in items])


def Weight(items):
    return sum([item.getWeight() for item in items])


def bestValue(maxWeight=20):
    items = buildItems()
    pset = genPowerset(items)
    best = pset[0]

    for items in pset:
        if Weight(items) > maxWeight:
            continue
        elif Value(items) > Value(best):
            best = items

    print('Burglar is advised to pick', list(map(Item.getName, best)))
    print('Total value of items taken is', Value(best))

    for item in best:
        print(item)


bestValue()
