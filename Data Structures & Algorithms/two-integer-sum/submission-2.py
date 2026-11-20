class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        values = {nums[0]: 0}

        for i in range(1, len(nums)):
            if target - nums[i] in values:
                return [values[target-nums[i]], i]

            values[nums[i]] = i
        