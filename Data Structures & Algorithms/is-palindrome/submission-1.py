class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()

        al_num_str = ""
        
        for c in s:
            if c.isalnum():
                al_num_str += c

        l,r = 0, len(al_num_str) - 1

        while l < r:
            if al_num_str[l] != al_num_str[r]:
                return False
            l += 1
            r -= 1 
                
        return True 