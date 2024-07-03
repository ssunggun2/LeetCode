class Solution:
    def reverseVowels(self, s: str) -> str:
        char_loc = []
        for i, char in enumerate(s):
            if char in ["a" ,"e", "i", "o", "u" ,"A", "E", "I", "O","U"]:
                char_loc.append(i)
        # print(char_loc)
        s = list(s)
        # print(s)
        for i in range(len(char_loc) // 2):
            # print(i)
            # print(char_loc[i])
            # print(char_loc[-i - 1])
            # print(s[char_loc[i]])
            # print(s[char_loc[-i - 1]])
            s[char_loc[i]] , s[char_loc[-i - 1]] = s[char_loc[-i - 1]] , s[char_loc[i]]
            # print(s)
        s =''.join(s)
        # print(s)
        return s