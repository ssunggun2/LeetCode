class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int length = code.size();
        vector<int> result;
        for (int i = 0; i < length; i++) code.push_back(code[i]);
        if (k == 0) {
            for (int i = 0; i < length; i++) {
                result.push_back(0);
            }
            return result;
        }
        else if (k > 0) {
            for (int i = 0 ; i < length; i++) {
                int sum = 0;
                for (int j = 0; j < k ; j ++ ) {
                    int index = i + j + 1;
                    sum += code[index];
                }
                result.push_back(sum);
            }
        }
        else {
            for (int i = length ; i < length * 2; i++) {
                int sum = 0;
                for (int j = k; j < 0 ; j ++ ) {
                    int index = i + j;
                    sum += code[index];
                }
                result.push_back(sum);
            }
        }
        return result;
    }
};