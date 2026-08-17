class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        l = 0
        while l < len(path):
            while l < len(path) and path[l] == '/':
                l += 1
            string = ""
            if l == len(path):
                break
            while l< len(path) and path[l] != '/':
                string += path[l]
                l += 1
            if string == '.':
                continue
            elif string == '..':
                if stk:
                    stk.pop()
                else:
                    continue
            else:
                stk.append(string)
        if not stk:
            return '/'
        else:
            return "/" + "/".join(stk)

'''
think about what i might do here:
current plan:
have a point l
when we hit a /, we move l forwards until the next character isnt a slash
then we add these new characters to a string
we keep going until we hit a slash
then we make a few checks, is the character just a single .?
if so we disregard everything and start the process again
is it two dots? in that case we can remove the last string from our stack
otherwise we add to the stack
at the very end we merge everything in the stack together into one long string

edge cases:
if we start with a .., it should not do anything
if we end without a slash i.e l gets to the end we shouldn't malfunction
if we end without anything, we should just return /
'''
