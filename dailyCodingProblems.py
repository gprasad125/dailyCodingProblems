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
# Given an array of integers,
# return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i (NO DIVISION ALLOWED!)
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

#3. (3-14-2021)
# Given an input string s, reverse the order of the words. (Remove extra spaces!)
def reverseString(input):

    if type(input) != str:
        return None

    if len(input) == 1:
        return input

    allWords = input.split()
    allWords.reverse()
    allWords = " ".join(allWords)

    return allWords

#4. (3-15-2021)
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
def findMissing(arr):

    if len(arr) == 0:
        return None

    arr = [val for val in arr if val >= 0]
    arr.sort()

    if len(arr) == 0:
        return 0

    for val in arr:
        if (val + 1) not in arr:
            return val + 1

#5. (3-16-2021)
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# Given an implementation of cons, find cdr and car
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

    #Create a function that will be passed as "f" in the cons function
def car(input):
    def findFirst(a, b):
        return a
    return input(findFirst)

def cdr(input):
    def findLast(a, b):
        return b
    return input(findLast)
