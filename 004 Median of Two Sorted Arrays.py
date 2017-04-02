__author__ = 'yyao'

"""
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall
run time complexity should be O(log (m+n)).
"""
class Solution(object):

    def find_med(self,A,B,k):
        if not A: return B[k]
        if not B: return A[k]
        if k == 0: return min(A[0],B[0])
        m,n = len(A), len(B)
        if A[m//2] >= B[n//2]:
            if k> m//2 +n//2:
                return self.find_med(A,B[n//2+2:],k-n//2-1)
            else:
                return self.find_med(A[:m//2],B,k)
        else:
            return self.find_med(B,A,k)

    def findMedian(self,A1,B1):
        k = (len(A1)+len(B1))//2
        if (len(A1)+len(B1))% 2 == 0:
            return (self.find_med(A1,B1,k) + self.find_med(A1,B1,k-1)) / 2
        else:
            return self.find_med(A1,B1,k)






if __name__ == "__main__":
    assert Solution().findMedian([1,2],[1,2,3]) == 2
