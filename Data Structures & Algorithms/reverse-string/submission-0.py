class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # pointers on either side

        l,r = 0, len(s) - 1

        for i in range(len(s)// 2):
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        