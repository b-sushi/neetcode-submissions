class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(len(tokens)):
            if tokens[i] in {"+", "-", "*", "/"}:
                x = stk.pop()
                y = stk.pop()
                if tokens[i] in {"+"}:
                    stk.append(x + y)
                elif tokens[i] in {"-"}:
                    stk.append(y - x)
                elif tokens[i] in {"*"}:
                    stk.append (x*y)
                elif tokens[i] in {"/"}:
                    stk.append (int(y /x))
            else:
                stk.append(int(tokens[i]))
        return stk[0]

