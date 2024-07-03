class Solution:
    def reverseVowels(self, s: str) -> str:
        char_loc = []
        for i, char in enumerate(s):
            if char in ["a" ,"e", "i", "o", "u" ,"A", "E", "I", "O","U"]:
                char_loc.append(i)
        s = list(s)
        for i in range(len(char_loc) // 2):
            s[char_loc[i]] , s[char_loc[-i - 1]] = s[char_loc[-i - 1]] , s[char_loc[i]]
        s =''.join(s)
        return s