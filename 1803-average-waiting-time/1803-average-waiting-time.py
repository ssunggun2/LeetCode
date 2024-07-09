class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        num_customers = len(customers)
        # 1.
        total_wait = 0
        # total_wait += duration
        # 2. end_time 
        end_time = customers[0][0]
        # end_time = end_time + start_time + duration

        for i in range(num_customers):
            print('\n', i)
            start_time = customers[i][0]
            duration = customers[i][1]
            print(start_time, duration)
            print(end_time >= start_time)
            if end_time >= start_time:
                end_time += duration
                total_wait += end_time - start_time
            else:
                end_time = start_time + duration
                total_wait += duration
            print(end_time)
            print(total_wait)
        return total_wait / num_customers