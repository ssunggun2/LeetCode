class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        points = 0
        stack1 = []
        stack2 = []
        if x >= y:
            for c in s:
                if stack1 and stack1[-1] == 'a' and c == 'b':
                    stack1.pop()
                    points += x
                else:
                    stack1.append(c)
            for c in stack1:
                if stack2 and stack2[-1] == 'b' and c == 'a':
                    stack2.pop()
                    points += y
                else:
                    stack2.append(c)
        else:
            for c in s:
                if stack1 and stack1[-1] == 'b' and c == 'a':
                    stack1.pop()
                    points += y
                else:
                    stack1.append(c)
            for c in stack1:
                if stack2 and stack2[-1] == 'a' and c == 'b':
                    stack2.pop()
                    points += x
                else:
                    stack2.append(c)
        return points