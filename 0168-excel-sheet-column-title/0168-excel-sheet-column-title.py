class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        hash_map = {1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E" , 6 : "F", 7 : "G" , 8 : "H", 9 : "I", 10 : "J", 11 : "K", 12 : "L", 13 : "M", 
                    14 : "N", 15 : "O", 16 : "P", 17 : "Q", 18 : "R", 19 : "S", 20 : "T", 21 : "U", 22 : "V", 23 : "W" , 24 : "X", 25 : "Y", 26 : "Z"}
        r = []
        s = ""
        if columnNumber // 27 < 1:
            return hash_map[columnNumber]
        n = 1
        while n != 0:
            _, mod = divmod(columnNumber, 26)
            if mod == 0:
                mod = 26
            n, _ = divmod(columnNumber, 27)
            r.append(int(mod))
            columnNumber = (columnNumber - mod) / 26 
            
        for i in range(len(r) - 1, -1 , -1):
            num = r[i]
            s += hash_map[num]
        return s
