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
        # if x >= y: first, second, first_score, second_score = 'ab', 'ba', x, y
        # else : second, first, second_score, first_score = 'ab', 'ba', x, y
        # while first in s:
        #     s = s.replace(first, '', 1)
        #     max_point += first_score
        # while second in s:
        #     s = s.replace(second, '', 1)
        #     max_point += second_score
        # return max_point