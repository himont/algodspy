from collections import deque


def maxInWindow(arr, n, k):
    q = deque()
    for i in range(k):
        while q and arr[i] > arr[q[-1]]:
            q.pop()
        q.append(i)
    for i in range(k, n):
        print arr[q[0]]
        while q[0] <= i - k:
            q.popleft()
        while q and arr[i] > arr[q[-1]]:
            q.pop()
        q.append(i)
    print arr[q[0]]


if __name__ == "__main__":
    arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    n = len(arr)
    maxInWindow(arr, n, 4)
