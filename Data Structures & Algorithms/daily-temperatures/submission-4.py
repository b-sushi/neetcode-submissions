class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        answer = [0] * len(temperatures)
        for i, val  in enumerate(temperatures):
            if not stk or val <= stk[-1][0]:
                stk.append((val, i))
            else:
                while stk and val > temperatures[stk[-1][1]]:
                    _, day = stk.pop()
                    answer[day] = i - day
                stk.append((val, i))
        return answer


        