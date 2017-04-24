class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m -= 1
            else:
                nums1[index] = nums2[n]
                n -= 1
            index -= 1
        if m < 0:  ##dont need n<0 b/c it will stay the same 
            nums1[:n + 1] = nums2[:n + 1]


if __name__ == "__main__":
    num1 = [1, 1, 2, 2, 4, 0, 0, 0, 0]
    num2 = [0, 0, 2, 3]
    Solution().merge(num1, 5, num2, 4)
    assert num1 == [0, 0, 1, 1, 2, 2, 2, 3, 4]
