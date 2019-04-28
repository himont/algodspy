'''https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
Given an array containing both negative
 and positive integers. Find the contiguous
  sub-array with maximum sum. '''


def get_max_sum(ar):
    cur_max = ar[0]
    max_till_now = ar[0]
    for val in ar[1:]:
        cur_max = max(val, cur_max + val)
        max_till_now = max(max_till_now, cur_max)
    return max_till_now


if __name__ == "__main__":
    ar = map(int, raw_input().strip().split())
    max_sum = get_max_sum(ar)
    print max_sum
