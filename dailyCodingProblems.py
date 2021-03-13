#1. (3-12-2021)
# Given a list of integers, and an integer k, find if any 2 values in the list add up to k
def equal(lst, k):

    if (len(lst) == 0) or (type(k) != int):
        return False

    lst = list(set(lst))
    dict = {val:lst.count(k-val) for val in lst}

    if 1 in list(dict.values()):
        return True
    else:
        return False

#2. (3-13-2021)
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i (NO DIVISION ALLOWED!)
def multiplyList(lst):

    if len(lst) == 0:
        return 0

    def recursiveMultiply(lst):
        if len(lst) == 1:
            return lst[0]

        firstTerm = lst[0]
        rest = lst[1:]

        return firstTerm * recursiveMultiply(rest)

    totalProduct = recursiveMultiply(lst)
    answer = [int(totalProduct * (term ** -1)) for term in lst]

    return answer
