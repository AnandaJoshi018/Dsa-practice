class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        counter = 0
        summ = 0
        
        while counter < len(nums):
            summ = summ + nums[counter]
            res.append(summ)
            counter += 1
        
        return res
        