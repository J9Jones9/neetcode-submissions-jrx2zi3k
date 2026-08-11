class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        curMax = 0

        for num in nums:
            if num == 1:
                curMax += 1
                maxOnes = max(curMax, maxOnes)
            else: curMax = 0

        return maxOnes