class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int size = nums.size();
        int w = nums[0];
        int x = nums[1];
        int y = nums[size - 2];
        int z = nums[size - 1];
        return (y * z) - (w * x);
    }
};