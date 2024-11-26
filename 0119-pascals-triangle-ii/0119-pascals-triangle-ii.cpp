#include <vector>

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row = {1};
        row[0] = 1;
        for (int i = 0; i < rowIndex; i++) {
            vector<int> temp = {1}; // 새로운 행의 시작은 항상 1
            for (int j = 0; j < row.size() - 1; j++) {
                temp.push_back(row[j] + row[j + 1]); // 이전 행의 두 값의 합
            }
            temp.push_back(1); // 새로운 행의 끝은 항상 1
            row = temp; // 현재 행을 업데이트
        }
        return row;
    }
};