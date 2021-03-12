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
