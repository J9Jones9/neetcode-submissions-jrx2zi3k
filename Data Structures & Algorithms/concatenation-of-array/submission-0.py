class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])

        finalAns = ans + ans

        return finalAns
        