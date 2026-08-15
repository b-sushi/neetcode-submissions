class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        k = len(s1)
        right = k
        characters = {}
        temp = {}
        for letter in s1:
            if letter in characters:
                characters[letter] +=1
            else:
                characters[letter] = 1
        while right <= len(s2):
            temp = {}
            for letter in s2[left:right]:
                if letter in temp:
                    temp[letter] += 1
                else:
                    temp[letter] = 1
            if temp == characters:
                return True
            else:
                left +=1
                right +=1
        return False                
                    

