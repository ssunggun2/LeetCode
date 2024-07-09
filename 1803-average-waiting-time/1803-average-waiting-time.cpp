class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        int numCustomer = customers.size();
        double totalWait = 0;
        int endTime = customers[0][0];
        for (int i = 0; i < numCustomer; i ++) {
            int startTime = customers[i][0];
            int duration = customers[i][1];
            if (startTime <= endTime) {
                endTime += duration;
                totalWait += endTime - startTime;
            } else {
                endTime = startTime + duration;
                totalWait += duration;
            }
        }

        return totalWait / numCustomer;

    }
};