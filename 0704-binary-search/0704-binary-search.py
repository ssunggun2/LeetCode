class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.result = 0
        self.nums = nums[:]
        self.target = target
        while self.nums:
            self.recursion()
        return self.result

    def recursion(self):
        half = int(len(self.nums) / 2)
        if self.nums:
            if len(self.nums) == 1:
                if self.target == self.nums[0]:
                    self.result = 0    
                else:
                    self.result = -1
                self.nums = None

            elif self.target == self.nums[half]:
                self.result += half
                self.nums = None
            elif self.target > self.nums[half]:
                self.result += half
                self.nums = self.nums[half:]
            else:
                self.nums = self.nums[:half]