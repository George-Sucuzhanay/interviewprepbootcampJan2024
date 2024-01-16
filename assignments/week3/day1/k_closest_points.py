# leetcode 973 k closest points to origin
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts_minheap = []

        for i, pt in enumerate(points):
            pts_minheap.append([sqrt(pt[0]**2 + pt[1]**2), i])
            # append the distance and the index to minheap
        heapq.heapify(pts_minheap) # we will sort by the distance instead od the index

        k_pts = []

        for i in range(k):
            elem = heapq.heappop(pts_minheap)
            k_pts.append(points[elem[1]])
        return k_pts

        # time: O(n + klogn)
        # space: O(n)
