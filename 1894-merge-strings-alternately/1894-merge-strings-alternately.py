class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ''
        for i in range(0, len(word1)):
            answer += word1[i]
            for j in range(i, len(word2)):
                answer += word2[j]
                break
        if len(word2) > len(word1):
            answer += word2[len(word1):]
        return answer
            