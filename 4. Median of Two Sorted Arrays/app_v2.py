class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length1:int = len(nums1)
        length2:int = len(nums2)

        size:int = length1 + length2
        half:int = int(size / 2)

        l1:int = 0
        r1:int = len(nums1) - 1

        if half >= r1:
            m1:int = r1.
        else:
            m1:int = int(r1/2)

        l2:int = 0
        r2:int = len(nums2)-1
        m2:int = size - m1

        while True:
            if nums1[m1] < nums2[m2+1] and nums2[m2] < nums1[m1+1]:
                if size%2 == 1:
                    return min(nums2[m2+1],nums1[m1+1])
                else:
                    return ( max( nums1[m1], nums2[m2] ) + min( nums2[m2+1], nums1[m1+1] ) ) / 2
            elif nums1[m1] > nums2[m2+1]:
                r1 = m1
                m1 = r1/2
                m2 = size - m1
            elif nums2[m2] > nums1[m1+1]:
                l1 = m1 + 1
                m1 = int((r1 + l1)/2)
                m2 = size - m1