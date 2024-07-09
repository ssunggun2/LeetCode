class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        num_customers = len(customers)
        total_wait = 0
        end_time = customers[0][0]
        for i in range(num_customers):
            start_time = customers[i][0]
            duration = customers[i][1]
            if end_time >= start_time:
                end_time += duration
                total_wait += end_time - start_time
            else:
                end_time = start_time + duration
                total_wait += duration
        return total_wait / num_customers