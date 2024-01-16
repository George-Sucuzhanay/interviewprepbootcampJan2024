# leetcode 1046 last stone weight

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_maxheap = []

        stones_maxheap = [-stone for stone in stones]
       
        heapq.heapify(stones_maxheap)

        while len(stones_maxheap) > 1:
            y =  heapq.heappop(stones_maxheap)
            x =  heapq.heappop(stones_maxheap)
            if y!= x:
               heapq.heappush(stones_maxheap, y-x)
               
        return -1 * heapq.heappop(stonesmaxheap) if stones_heap else 0