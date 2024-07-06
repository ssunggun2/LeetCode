class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 1
        i = 1
        for t in range(time):
            i += 1 * direction
            if i == n or i == 1:
                direction *= -1
        return i