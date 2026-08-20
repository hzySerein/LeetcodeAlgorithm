class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        len1 = len(nums1)
        len2 = len(nums2)

        p1 = len1 - 1
        p2 = len2 - 1
        p3 = p1 - len2 

        while p2 >= 0 and p3 >=0:
            if nums1[p3] < nums2[p2]:
                nums1[p1] = nums2[p2]
                p2 -= 1
            else:
                nums1[p1] = nums1[p3]
                p3 -= 1
            p1 -= 1

        while p2 >= 0:
            nums1[p1] = nums2[p2]
            p2 -= 1
            p1 -= 1
            


