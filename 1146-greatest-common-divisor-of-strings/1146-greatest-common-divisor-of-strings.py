class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        short_str = min(str1, str2)
        a = ''
        for i in range(len(short_str)):
            ans = short_str[:i+1]
            if str1.replace(ans, '') != '' or str2.replace(ans, '') != '':
                ans == ''
            else:
                a = ans[:]
        return a if a != '' else ''
                