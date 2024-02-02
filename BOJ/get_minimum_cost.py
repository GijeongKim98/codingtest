# 최소비용 구하기 2
'''https://www.acmicpc.net/problem/11779'''

import sys
import heapq as hq

INF = 100000000

DIST, PRE_NODE = 0, 1

def dijkstra(s):
    node_info[s][DIST] = 0
    heap = [(0,s)]

    while heap:
        pop_cost, pop_node = hq.heappop(heap)

        if node_info[pop_node][DIST] < pop_cost:
            continue

        for new_node, new_cost in graph[pop_node].items():
            cost = pop_cost + new_cost
            if cost < node_info[new_node][DIST]:
                node_info[new_node][DIST], node_info[new_node][PRE_NODE] = cost, pop_node
                hq.heappush(heap, (cost, new_node))


if __name__ == "__main__":
    try:
        n, m = int(sys.stdin.readline()), int(sys.stdin.readline())

        graph = {i:{} for i in range(1,n+1)}

        for _ in range(m):
            x, y, cost = map(int, sys.stdin.readline().split(" "))
            if y in graph[x]:
                graph[x][y] = min(graph[x][y], cost)
            else:
                graph[x][y] = cost

        start, end = map(int, sys.stdin.readline().split(" "))

        node_info = [[INF, 0] for _ in range(n+1)]

        dijkstra(start)

        minimum_cost = node_info[end][DIST]

        minimum_path = [end]

        while True:
            pre = node_info[minimum_path[-1]][PRE_NODE]
            minimum_path.append(pre)
            if pre == start:
                break

        minimum_path.reverse()

        print(minimum_cost, len(minimum_path), sep="\n")
        print(*minimum_path, sep=" ")

    except ValueError or IndexError as e:
        print(e)