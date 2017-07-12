"""
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].
"""

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.i = 0
        self.j = 0
        

    def next(self):
        """
        :rtype: int
        """
        ret = None
        if self.hasNext():
            ret = self.vec2d[self.i][self.j]
            self.j+=1
        return ret
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.i < len(self.vec2d) and self.j>= len(self.vec2d[self.i]):
            self.i+=1
            self.j = 0
        return self.i < len(self.vec2d) and self.j < len(self.vec2d[self.i])
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
