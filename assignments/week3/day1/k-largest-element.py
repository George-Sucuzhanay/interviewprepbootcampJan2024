# leetcode 215 k-largest elememt in an array
import heapq # only provides minheaps
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxheap so we will negate
        nums_maxheap = []

        for num in nums:
            nums_maxheap.append(-num) # we negate vals to get maxheap
        heapq.heapify(nums_maxheap) # convert the array to a heap

        for i in range(k-1): # in order to keep k as the root
            heapq.heappop(nums_maxheap)

        return -1 * heapq.heappop(nums_maxheap)

# time: klog(n)