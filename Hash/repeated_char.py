# https://practice.geeksforgeeks.org/problems/find-first-repeated-character/0
from collections import defaultdict


def firstRepeatedChar(str1, freq_dict):
    for c in str1:
        if freq_dict[c] == 1:
            return c
        freq_dict[c] += 1
    return "No repeated character found"


if __name__ == "__main__":
    s = raw_input().strip()
    freq_dict = defaultdict(int)
    print firstRepeatedChar(s, freq_dict)
