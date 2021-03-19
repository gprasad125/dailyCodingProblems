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
# return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i
# (NO DIVISION ALLOWED!)
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

#6. (3-17-2021)
# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
# Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
class Node:
    def __init__(self, element):
        self.element = element
        self.both = None

class XORList:
    def __init__(self):
        self.head = None

    #def calculateXOR(self, a, b):
    #    self.xor = a

    def add(element):
        toAdd = Node(element)
        #toAdd. = toAdd.calculateXOR(element, b)

# HMM this is hard

#7. (3-18-2021)
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

mapping = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabet)):
    mapping[alphabet[i]] = i + 1

def decode(input):

    n = len(input)

    if n <= 1:
        return 1

    currentCount = 0
    if input[n-1] > "0":
        currentCount = decode(input[0:n-1])
    if input[n-2] + input[n-1] < "26":
        currentCount += decode(input[0:n-2])

    return currentCount
