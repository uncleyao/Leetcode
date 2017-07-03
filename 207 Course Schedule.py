"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.'

"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        V = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            V[edge[0]].append(edge[1])
        visited = [False for _ in range(numCourses)]
        marked = [False for _ in range(numCourses)]
        for i in range(numCourses):
            if not visited[i]:
                if self.dfs_cycle(V,i,visited,marked):
                    return False
        return True
    
    def dfs_cycle(self, V, i, visited, marked):
        if marked[i]:
            return True
        
        marked[i] = True
        
        for neigh in V[i]:
            if not visited[neigh] and self.dfs_cycle(V,neigh,visited,marked):
                return True
        
        marked[i]= False
        visited[i] = True
        return False
    
