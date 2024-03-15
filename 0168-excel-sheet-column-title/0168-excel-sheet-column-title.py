class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r = []
        while columnNumber:
            columnNumber, mod = divmod(columnNumber - 1, 26)
            r.append(chr(65+mod))
            
        return ''.join(reversed(r))
