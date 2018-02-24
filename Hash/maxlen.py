# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
from collections import defaultdict


def getMaxDiff(result_dict):
    max_len = 0
    for k, v in result_dict.items():
        if v[0] > 1:
            cur_max_len = v[len(v) - 1] - v[1]
            max_len = (cur_max_len, max_len)
    return max_len


def maxLen(ar, result_dict, l):
    sum = 0
    for i in range(l):
        sum += ar[i]
        if result_dict[sum]:
            result_dict[sum][0] += 1
        else:
            result_dict[sum] = [1]
        result_dict[sum].append(i)
    return getMaxDiff(result_dict)


if __name__ == "__main__":
    ar = map(int, raw_input().strip().split(" "))
    result_dict = defaultdict(list)
    print maxLen(ar, result_dict, len(ar))
