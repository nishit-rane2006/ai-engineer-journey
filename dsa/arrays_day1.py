
#Leetcode 1920
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return[nums[nums[i]] for i in range(len(nums))]
    

#Leetcode 1480
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums