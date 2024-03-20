class Solution:
    def romanToInt(self, s: str) -> int:
        sums = 0
        prev_char = "A"
        for char in s[::-1]:
            if char == "I":
                if prev_char in ["X", "V"]:
                    sums -= 1
                else:
                    sums += 1
                prev_char = char
            
            elif char == "V":
                sums += 5
                prev_char = char
            
            elif char == "X":
                if prev_char in ["L", "C"]:
                    sums -= 10
                else:
                    sums += 10
                prev_char = char

            elif char == "L":
                sums += 50
                prev_char = char
            
            elif char == "C":
                if prev_char in ["D", "M"]:
                    sums -= 100
                else:
                    sums += 100
                prev_char = char

            elif char == "D":
                sums += 500
                prev_char = char
            
            else:
                sums += 1000
                prev_char = char

        return sums