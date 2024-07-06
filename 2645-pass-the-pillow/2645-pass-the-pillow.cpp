class Solution {
public:
    int passThePillow(int n, int time) {
        int direction = 1;
        int index = 1;
        for (int i = 0; i < time; i++ ) {
            index += 1 * direction;
            if (index == n || index == 1) {
                direction *= -1;
            }
        }
    return index;
    }
};