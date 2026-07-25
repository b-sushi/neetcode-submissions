class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for x in strs:
            encoded_string += str(len(x)) + '#' + x 
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        decoded_string = []
        L = 0
        while L < len(s):
            R = L
            while s[R] != '#':
                R += 1
            length = int(s[L:R])
            word = s[R + 1: R + 1 + length]
            decoded_string.append(word)
            L = R + 1 + length
        return decoded_string