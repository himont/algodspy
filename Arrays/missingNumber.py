'''https://practice.geeksforgeeks.org/problems/missing-number-in-array/0
Given an array of size n-1 and
given that there are numbers from 1 to n with one missing,
the missing number is to be found.'''

import random


def findMissing(ar, l):
    sum = ((l + 1) * (l + 2)) / 2
    for i in range(l):
        sum = sum - ar[i]
    return sum


def findMissingXOR(ar, l):
    def list_xor(x, y): return x ^ y
    xor1 = reduce(list_xor, range(l + 2))
    xor2 = reduce(list_xor, ar)
    return xor1 ^ xor2


if __name__ == "__main__":
    n = int(raw_input())
    missing_num = random.randint(1, n)
    print "Actual missing number is: " + str(missing_num)
    ar = range(1, missing_num) + range(missing_num + 1, n + 1)
    print "input array is: " + str(ar)
    print "As per program calculation missing number is: " + \
        str(findMissing(ar, n - 1))
    print "As per program calculation via XOR missing number is: " + \
        str(findMissingXOR(ar, n - 1))
