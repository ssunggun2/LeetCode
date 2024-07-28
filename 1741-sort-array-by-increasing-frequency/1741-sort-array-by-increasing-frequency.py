class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency_dict = {}
        for i in nums:
            if not frequency_dict.get(i):
                frequency_dict[i] = 1
            else:
                frequency_dict[i] += 1
        frequency_list = sorted(frequency_dict.items(), key = lambda item: (item[1], -item[0]))
        result = []
        print(frequency_list)
        for (i, j) in frequency_list:
            for k in range(j):
                result.append(i)
        return result