class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        for i in range(len(s)):
            target = s[i]
            print(s,t)
            for j in range(len(t)):
                if target == t[j]:
                    k += 1
                    t = t[j + 1 : ]
                    break
                if j == len(t) - 1:
                    return False
        return k == len(s)