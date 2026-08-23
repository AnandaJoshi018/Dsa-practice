class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums)) # this removes duplicate elemensts in list/array
        nums.sort() # sorts in ascending order

        if len(nums) < 3 :
            return nums[-1]
        else:
            return nums[-3]

        