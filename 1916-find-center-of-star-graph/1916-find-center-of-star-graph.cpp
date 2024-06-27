class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        int u = edges[0][0];
        int v = edges[0][1];
        int s = edges[1][0];
        int t = edges[1][1];
        if (s == u || t == u) {
            return u;
        }
        else {
            return v;
        }

    }
};