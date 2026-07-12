class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevNums = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in prevNums:
                return [prevNums[complement], i]
            prevNums[nums[i]] = i

                















            221