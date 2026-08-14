class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        lookup = {')': '(', '}': '{', ']': '['}
        for val in s:
            if val in lookup.values():
                stk.append(val)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if lookup[val] == popped:
                        continue
                    else:
                        return False
        
        if not stk: return True
        else: return False
