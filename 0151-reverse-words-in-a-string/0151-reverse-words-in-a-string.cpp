#include <sstream>

class Solution {
public:
    string reverseWords(string s) {
        cout << s << endl;
        string find_str = "  ";
        string replace_str = " ";
        while (s.find(find_str) != string::npos) {
            s.replace(s.find(find_str), find_str.length(), replace_str);
        }
        cout << s << endl;
        istringstream iss(s);
        string buffer;
        vector<string> result;
        while (getline(iss, buffer, ' ')) {
            result.insert(result.begin(), buffer);
        }
    stringstream ss;
    for (auto it = result.begin(); it != result.end(); it++) {
        if (it != result.begin()) {
            ss << " ";
        }
        ss << *it;
    }
    string ans = ss.str();
    if (ans.back() == ' ') {
        ans.pop_back();
    }
    cout << ans << endl;
    return ans;
    }
};