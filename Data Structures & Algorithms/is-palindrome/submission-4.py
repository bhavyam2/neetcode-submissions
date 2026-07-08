class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        print(left)
        print(right)
        while (left < right):
            while (left < right) & (s[left].isalnum() == False):
                left = left + 1
            while (left < right) & (s[right].isalnum() == False):
                right = right - 1
            if s[right].lower() != s[left].lower():
                return False
            print(left)
            print(right)
            left = left + 1
            right = right - 1
        return True