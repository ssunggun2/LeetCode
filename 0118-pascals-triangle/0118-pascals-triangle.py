class Solution:
    def generate(self, numRows: int):
        self.current_row = [1,1]
        self.result = [[1] , self.current_row]
        if numRows == 1:
            return [[1]]        
        elif numRows == 2:
            return self.result
        for i in range(3, numRows+1):
            self.current_row = self.get_row(self.current_row)
            self.result.append(self.current_row)
        return self.result

    def get_row(self, before_row : list):
        current_row = []
        for i in range(len(before_row) - 1):
            current_row.append(before_row[i] + before_row[i+1])
        return [1] + current_row + [1]
    