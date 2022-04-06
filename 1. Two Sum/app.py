class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(len(nums)-(x+1)):
                if nums[x] + nums[y+x+1] == target:
                    return [x,y+x+1]