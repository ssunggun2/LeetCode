class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # short_str = min(str1, str2)
        # a = ''
        # for i in range(len(short_str)):
        #     ans = short_str[:i+1]
        #     if str1.replace(ans, '') != '' or str2.replace(ans, '') != '':
        #         ans == ''
        #     else:
        #         a = ans[:]
        # return a if a != '' else ''
                
        short_str = min(str1, str2)

        for i in range(len(short_str) , 0 , -1):
            if len(str1) % i or len(str2) % i :
                continue
            n1 = len(str1) // i
            n2 = len(str2) // i
            base = str1[:i]
            if str1 == n1 * base and str2 == n2*base:
                return str1[:i]
        return ''