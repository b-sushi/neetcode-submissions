class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        answer = [0] * len(temperatures)
        temps = temperatures
        for i, t in enumerate(temps):
            while stk and stk[-1][0]  < t:
                stk_t, stk_i = stk.pop()
                answer[stk_i] = i - stk_i
            stk.append((t, i))
        return answer