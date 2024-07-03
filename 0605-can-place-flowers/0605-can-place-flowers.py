class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # def place(flowerbed, n, possible_place):
        #     non_possible_place = []
        #     plant_place = list(filter(lambda x: flowerbed[x] == 1, range(len(flowerbed))))
        #     for i in plant_place:
        #         non_possible_place.append(i)
        #         if i - 1 >= 0:
        #             non_possible_place.append(i - 1)
        #         if i + 1 < len(flowerbed):
        #             non_possible_place.append(i + 1)
        #     target = list(set(possible_place) - set(non_possible_place))
        #     if target == []:
        #         return None, -1
        #     flowerbed[target[0]] = 1
        #     n -= 1
        #     return flowerbed, n
        # possible_place = [i for i in range(len(flowerbed))]
        # for i in range(n):
        #     flowerbed, n = place(flowerbed, n, possible_place)
        #     if n == -1:
        #         break

        # return True if n == 0 else False

        def placing(flowerbed, n):
            if flowerbed[:2] == [1, 0]:
                flowerbed = flowerbed[2:]
            elif flowerbed[:3] == [0, 1, 0]:
                flowerbed = flowerbed[3:]
            elif flowerbed[:2] == [0, 0]:
                flowerbed = flowerbed[2:]
                n -= 1
            elif flowerbed == [0]:
                flowerbed = []
                n -= 1
            else:
                n = -1
            return flowerbed, n
        
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            flowerbed, n = placing(flowerbed, n)
            if n == 0:
                return True
            elif n == -1:
                break
        return False