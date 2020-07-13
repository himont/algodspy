from collections import deque


def is_valid(grid, ele, n, m, visited):
    return (ele[0] > -1 and ele[1] > -1 and ele[0] < n and ele[1] < m and
            not visited[ele[0]][ele[1]] and grid[ele[0]][ele[1]])


def get_shortest_path(grid, n, m, s, d):
    q = deque()
    q.append(s)
    visited = [[False for j in range(m)]for i in range(n)]
    distance = [[-1 for j in range(m)] for i in range(n)]
    distance[s[0]][s[1]] = 0
    while q:
        value = q.popleft()
        i = value[0]
        j = value[1]
        a = [[i + 1, j], [i - 1, j], [i, j + 1], [i + 1, j]]
        for ele in a:
            if is_valid(grid, ele, n, m, visited):
                visited[i][j] = True
                q.append(ele)
                distance[ele[0]][ele[1]] = distance[i][j] + 1
                if ele[0] == d[0] and ele[1] == d[1]:
                    return distance[ele[0]][ele[1]]
    return -1


if __name__ == '__main__':
    with open('shortest_distance.txt') as f:
        M = int(f.readline())
        N = int(f.readline())
        print("Size of the grid is: %d X %d"%(M,N))
        src = list(map(int, f.readline().strip().split()))
        print("Source point is: (%d, %d)" % (src[0], src[1]))
        dest = list(map(int, f.readline().strip().split()))
        print("Destination point is: (%d, %d)" % (dest[0], dest[1]))
        grid = []
        for grid_i in range(M):
            grid_temp = list(map(int, f.readline().strip().split(' ')))
            grid.append(grid_temp)
    print("Input grid is following:")
    for i in range(M):
        print(grid[i])
    print("Shortest distance between source and destination point is: %d" % get_shortest_path(grid, N, M, src, dest))