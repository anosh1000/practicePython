class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        left = 0
        right = len(s) - 1
        while left <= right:
            if not s[left].alnum():
                left += 1
                continue
            if not s[right].alnum():
                right += 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True