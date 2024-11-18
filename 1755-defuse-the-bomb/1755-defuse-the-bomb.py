class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        code = code * 2
        if k == 0:
            return [0 for i in range(length)]
        elif k > 0:
            return [sum(code[i+1 : i+1+k]) for i in range(length)]
        else:
            return [sum(code[i+k : i]) for i in range(length, length*2)]