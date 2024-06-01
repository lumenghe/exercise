"""
K Closest Points to Origin
Solved
Medium
Topics
Companies

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

 

Constraints:

    1 <= k <= points.length <= 104
    -104 <= xi, yi <= 104

"""

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_power_2(point):
            return (point[0]) ** 2 + (point[1]) ** 2

        distance = {}
        for point in points:
            p_d = distance_power_2(point)
            distance.setdefault(p_d, [])
            distance[p_d].append(point)

        ret = []
        count = 0
        new_order = dict(sorted(distance.items()))

        for key, value in new_order.items():
            if count + len(value) <= k:
                count += len(value)
                ret.extend(value)
            else:
                ret.extend(value[: k - count])
                break

        return ret


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = -(x**2 + y**2)

            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y))
        top = heapq.nsmallest(k, heap)
        return [(x, y) for (dist, x, y) in top]
