"""

Course Schedule

You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.

Example 1:

Input: numCourses = 2, prerequisites = [[0,1]]

Output: true

Explanation: First take course 0 (no prerequisites) and then take course 1.

Example 2:

Input: numCourses = 2, prerequisites = [[0,1],[1,0]]

Output: false

Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.

Constraints:

    1 <= numCourses <= 1000
    0 <= prerequisites.length <= 1000
    All prerequisite pairs are unique.
"""

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        ans = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            ans.append(current)

            for next_course in adj[current]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return len(ans) == numCourses


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graphs = [[] for _ in range(numCourses)]
        a = [0] * numCourses

        for des, source in prerequisites:
            graphs[source].append(des)
            a[des] += 1

        queue = []
        for i in range(numCourses):
            if a[i] == 0:
                queue.append(i)
        ans = []
        while queue:
            current = queue.pop(0)
            ans.append(current)

            for next_node in graphs[current]:
                a[next_node] -= 1
                if a[next_node] == 0:
                    queue.append(next_node)

        return len(ans) == numCourses


import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        pre_graph = {i: set() for i in range(numCourses)}

        for dest, source in prerequisites:
            graph[source].add(dest)
            pre_graph[dest].add(source)
        queue = []

        for dest, source in pre_graph.items():
            if len(source) == 0:
                queue.append(dest)

        visited = []
        while queue:
            current = queue.pop(0)
            visited.append(current)
            if len(visited) == numCourses:
                return True
            for nextt in graph[current]:
                pre_graph[nextt].remove(current)
                if not pre_graph[nextt]:
                    queue.append(nextt)

        return False
