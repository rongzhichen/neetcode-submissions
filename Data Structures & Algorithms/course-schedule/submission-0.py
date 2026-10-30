from collections import deque
from typing import List

class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        finished = 0

        while queue:
            course = queue.popleft()
            finished += 1

            for dependent in adj[course]:
                indegree[dependent] -= 1

                if indegree[dependent] == 0:
                    queue.append(dependent)

        return finished == numCourses
        
        