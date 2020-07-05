def knapsack_rec(n, weights, values, cap):
    if n == 0 or cap == 0:
        return 0
    elif weights[n-1] > cap:
        return knapsack_rec(n-1, weights, values, cap)
    else:
        return max(values[n-1] + knapsack_rec(n-1, weights, values, cap - weights[n-1]),
                   knapsack_rec(n - 1, weights, values, cap))


def knapsack_rec_opt(n, weights, values, cap, track_dict):
    val = track_dict.get((n, cap), None)
    if val:
        return val
    elif n == 0 or cap == 0:
        track_dict[(n, cap)] = 0
    elif weights[n-1] > cap:
        track_dict[(n, cap)] = knapsack_rec_opt(n-1, weights, values, cap, track_dict)
    else:
        track_dict[(n, cap)] = max(values[n-1] + knapsack_rec_opt(n-1, weights, values, cap - weights[n-1], track_dict),
                                   knapsack_rec_opt(n - 1, weights, values, cap, track_dict))
    return track_dict[(n, cap)]


if __name__ == "__main__":
    print("Enter weights:")
    weights = [int(i) for i in input().strip().split()]
    print("Enter values:")
    values = [int(i) for i in input().strip().split()]
    print("Enter knapsack weight capacity:")
    capacity = int(input())
    track_dict = dict()
    if len(values) == len(weights):
        n = len(values)
        max_val1 = knapsack_rec(n, weights, values, capacity)
        max_val2 = knapsack_rec_opt(n, weights, values, capacity, track_dict)
        print("Max possible Value of knapsack from basic recursion algo is %d" %(max_val1))
        print("Max possible Value of knapsack from optimised recursion algo is %d" %(max_val2))
    else:
        print("Number of elements of values and weights do not match")