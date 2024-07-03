class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if  flowerbed[i] == 0 :
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) -1) or (flowerbed[i + 1] == 0)
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    if count > n:
                        break
        return count >= n



        # def placing(flowerbed, n):
        #     if flowerbed[:2] == [1, 0]:
        #         flowerbed = flowerbed[2:]
        #     elif flowerbed[:3] == [0, 1, 0]:
        #         flowerbed = flowerbed[3:]
        #     elif flowerbed[:2] == [0, 0]:
        #         flowerbed = flowerbed[2:]
        #         n -= 1
        #     elif flowerbed == [0]:
        #         flowerbed = []
        #         n -= 1
        #     else:
        #         n = -1
        #     return flowerbed, n
        
        # if n == 0:
        #     return True

        # for i in range(len(flowerbed)):
        #     flowerbed, n = placing(flowerbed, n)
        #     if n == 0:
        #         return True
        #     elif n == -1:
        #         break
        # return False