class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        for (int i = 0 ; i < flowerbed.size(); i ++ ) {
            bool emptyLeft = ((i == 0) || (flowerbed[i - 1] == 0));
            bool emptyRight = ((i == flowerbed.size() - 1) || (flowerbed[i + 1] == 0));
            if (emptyLeft and emptyRight and flowerbed[i] == 0) {
                flowerbed[i] = 1;
                n--;
            }
        }
    if (n <= 0 ) return true;
    else return false;
    }
};
