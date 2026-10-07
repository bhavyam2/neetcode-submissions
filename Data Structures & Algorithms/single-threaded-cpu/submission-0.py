import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ordered_tasks = []

        for index, (enqueue_time, processing_time) in enumerate(tasks):
            ordered_tasks.append((enqueue_time, processing_time, index))
        
        ordered_tasks.sort(key=lambda task: [task[0]])

        available = []
        result = []
        current_time = 0
        next_task = 0

        n = len(ordered_tasks)

        while next_task < n or available:
            if not available:
                current_time = max(current_time, ordered_tasks[next_task][0])
            
            while next_task < n and ordered_tasks[next_task][0] <= current_time:
                enqueue_time, processing_time, index = ordered_tasks[next_task]
                
                
                heapq.heappush(available, (processing_time, index))
                next_task += 1
            
            processing_time, index = heapq.heappop(available)

            result.append(index)
            current_time += processing_time

        return result
