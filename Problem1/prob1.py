# this is the code for problem 1, solve using priority queue
# input: nums = [1,1,1,2,2,3], k = 2
# output: [1,2]

import heapq


def topMostKFrequent(nums: list[int], k: int) -> list[int]:
    # create a map to store the frequency of each element
    map = dict()

    # iterate through the list and store the frequency of each element
    for num in nums:
        map[num] = map.get(num, 0) + 1

    # create a heap
    heap = []

    # now iterate through map and store the frequency in the heap
    for key, value in map.items():
        heapq.heappush(heap, (value, key))
        # if the size of the heap is greater than k, pop the smallest element
        if len(heap) > k:
            heapq.heappop(heap)

    # take the keys from the heap and then return them
    return [key for value, key in heap]


# testing
nums = [1, 1, 1, 2, 2, 3]
k = 2
print("Example 1: nums = [1, 1, 1, 2, 2, 3], k = 2  Output:", topMostKFrequent(nums, k))

nums = [1]
k = 1
print("Example 2: nums = [1], k = 1  Output:", topMostKFrequent(nums, k))

nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5]
k = 3
print(
    "Example 3: nums = [1,1,1,2,2,3,4,4,4,4,5,5,5], k = 3  Output:",
    topMostKFrequent(nums, k),
)
