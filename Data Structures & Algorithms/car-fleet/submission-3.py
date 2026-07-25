class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Zip creates a lsit of tuples and sorted sorts them by the first element of each tuple
        cars = sorted(zip(position, speed), reverse = True)
        stk = []
        count = 1
        for i, (p,s) in enumerate(cars):
            cars[i] = (target - p) / s
        for i in cars:
            if not stk or stk[0] >= i:
                stk.append(i)
            else:
                stk = []
                stk.append(i)
                count +=1
        return count