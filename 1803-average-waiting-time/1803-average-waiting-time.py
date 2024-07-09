class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait = 0
        end_time = customers[0][0]
        for start_time, duration in customers:
            if end_time >= start_time:
                end_time += duration
            else:
                end_time = start_time + duration
            total_wait += end_time - start_time
        return total_wait / len(customers)