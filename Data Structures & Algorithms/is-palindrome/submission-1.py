class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        result = []
        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            if str.lower(s[right]) != str.lower(s[left]):
                return False
            left += 1
            right -= 1
        return True