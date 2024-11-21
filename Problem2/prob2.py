from collections import defaultdict
import heapq


def network(times, n, k):
    # times = source node, destination node, time taken to travel
    # n = number of nodes
    # k = starting node
    heap = []

    heapq.heappush(heap, [0, k])

    graph = defaultdict(list)
    # puts all nodes in an adjacency list
    for u, v, w in times:
        graph[u].append((v, w))
    # creates a set to keep track of visited nodes
    visited = set()
    # while the heap is not empty
    while heap:
        # get current node and time from heap
        current_node_time, node = heapq.heappop(heap)
        # if node is not in visited, add it to visited
        if node not in visited:
            visited.add(node)
            # if all nodes are visited return time
            if len(visited) == n:
                return current_node_time
            # check neighbors of current node and add their time to the heap
            for neighbor, neighbor_time in graph[node]:
                heapq.heappush(heap, [current_node_time + neighbor_time, neighbor])
    # return -1 if not all nodes can be reached
    return -1


print(
    "Example 1 [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2  Output: ",
    network([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2),
)
print("Example 2 [[1,2,1]], n = 2, k = 1  Output: ", network([[1, 2, 1]], 2, 1))
print("Example 3 [[1,2,1]], n = 2, k = 2  Output: ", network([[1, 2, 1]], 2, 2))
print(
    "Example 4 [[1,3,1],[1,2,4],[4,2,1],[3,4,1]], n = 4, k = 1  Output: ",
    network([[1, 3, 1], [1, 2, 4], [4, 2, 1], [3, 4, 1]], 4, 1),
)
