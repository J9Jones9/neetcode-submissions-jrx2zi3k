class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seenNums = {}
        for i in range(len(nums)):
            if nums[i] in seenNums:
                return True
            else:
                seenNums[nums[i]] = 1

        return False
        