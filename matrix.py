    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        offset = 0
        innerSize = size
        
        while innerSize > 1:
            for i in range(innerSize - 1):
                row = offset 
                col = i + offset
                before = matrix[row][col]
                after = matrix[col][len(matrix) - row - 1]

                for j in range(4):
                    matrix[col][len(matrix) - row - 1] = before
                    row, col = col, len(matrix) - row - 1
                    before = after
                    after = matrix[col][len(matrix) - row - 1]
            innerSize -= 2
            offset += 1
                
        return matrix