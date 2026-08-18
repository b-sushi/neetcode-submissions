import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(enqueue, proc, i) for i, (enqueue, proc) in enumerate(tasks)])
        min_heap = []
        res = []
        time = 0
        i = 0
        while i < len(tasks) or min_heap:
            if not min_heap and time < tasks[i][0]:
                time = tasks[i][0]
            while i< len(tasks) and tasks[i][0] <= time:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i +=1
            proc_time, idx = heapq.heappop(min_heap)
            time += proc_time
            res.append(idx)
        return res


'''
plan:

we obviously need a heap
we need one loop that will add tasks to our heap based on the time. we use this loop to initialise our heap and we also will need to run this every time 'time' increases to add the new avaliable tasks
afterwards we check our heap and find the one with the shortest processing time (i thinks amllest index will be handles automatically)
afterwards we can increment the time by the processing time (i think it'll be minus 1 since we will also auto increment the time) 
once this task is finished processing, we will add our new tasks. 
we can keep an array of the index of the task that we have processed, i guess we'd have to make a tuple with three values, the avaliable time, the processing time and the index?

edge cases:
if tasks is empty we need to return an empty array

'''