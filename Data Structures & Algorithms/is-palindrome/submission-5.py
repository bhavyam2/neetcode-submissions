class Solution:
    def isalphnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not self.isalphnum(s[left]):
                left += 1
                print(s[left])
            
            while right > left and not self.isalphnum(s[right]):
                right -= 1
                print(s[right])
            
            if s[left].lower() != s[right].lower():
                return False 

            left += 1
            right -= 1
        return True
