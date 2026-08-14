class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        clean_text = ''.join(char for char in s if char.isalnum())
        clean_text = clean_text.lower()
        right = len(clean_text) - 1
        while left < right:
            if clean_text[left] == clean_text[right]:
                left += 1
                right -=1
            else:
                return False
        return True