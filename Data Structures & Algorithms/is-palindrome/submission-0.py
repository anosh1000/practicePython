class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        for i in range(len(s)):
            left = s[i]
            right = s[-1-i]
            if left != right:
                return False
        
        return True