from typing import List

class Solution:
    def mergeArrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index1:int = 0
        index2:int = 0
        newArr:List[int] = []
        if nums1 == [] and nums2 == []:
            return []
        elif nums1 == []:
            return nums2
        elif nums2 == []:
            return nums1
        while True:
            if nums1 and nums2:
                if nums1[0] > nums2[0]:
                    newArr.append(nums2.pop(0))
                elif nums1[0] < nums2[0]:
                    newArr.append(nums1.pop(0))
            elif nums1:
                newArr.append(nums1.pop(0))
            elif nums2:
                newArr.append(nums2.pop(0))
            else:
                break
        return newArr



    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged: List[int] = self.mergeArrays(nums1, nums2)
        mLength:int = len(merged)
        if mLength == 0:
            return -1
        elif mLength == 1:
            return merged[0]
        elif mLength % 2 ==1:
            return merged[int(mLength/2)]
        else:
            return (merged[int(mLength/2)] + merged[ (int(mLength/2)) - 1 ]) / 2
    
sol = Solution()

a1 = [1,3]
a2 = [2]
a3 = [1,2]
a4 = [3,4]

print(sol.findMedianSortedArrays(a1, a2))
print(sol.findMedianSortedArrays(a3, a4))