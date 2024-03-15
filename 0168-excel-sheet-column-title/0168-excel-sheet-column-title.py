class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        hash_map = {1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E" , 6 : "F", 7 : "G" , 8 : "H", 9 : "I", 10 : "J", 11 : "K", 12 : "L", 13 : "M", 
                    14 : "N", 15 : "O", 16 : "P", 17 : "Q", 18 : "R", 19 : "S", 20 : "T", 21 : "U", 22 : "V", 23 : "W" , 24 : "X", 25 : "Y", 26 : "Z"}
        r = []
        if columnNumber // 27 < 1:
            return hash_map[columnNumber]
        while columnNumber:
            columnNumber, mod = divmod(columnNumber - 1, 26)
            r.append(hash_map[mod+1])
            
        return ''.join(reversed(r))
