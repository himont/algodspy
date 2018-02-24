'''https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0
The cost of a stock on each day is given in an array,
 find the max profit that you can make by buying and selling in those days.'''


def maxProfit(arr, n):
    if n < 2:
        return 0
    max_profit = 0
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            max_profit += (arr[i] - arr[i - 1])
    return max_profit


def getDays(arr, n):
    max_profit = 0
    my_list = []
    incr = 0
    i = 1
    local_start = None
    local_end = None
    while i < n:
        if arr[i - 1] <= arr[i]:
            max_profit += (arr[i] - arr[i - 1])
            if not incr:
                local_start = i - 1
                incr = 1
        elif incr:
            incr = 0
            local_end = i - 1
            my_list.append((local_start, local_end))
        i = i + 1
    if arr[i - 2] <= arr[i - 1]:
        local_end = i - 1
        my_list.append((local_start, local_end))
    print max_profit
    return my_list


if __name__ == "__main__":
    arr = map(int, raw_input().strip().split(' '))
    # print maxProfit(arr, len(arr))
    print getDays(arr, len(arr))
