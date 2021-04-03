class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        onEdge = set()
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    self.dfs(board, row, col, onEdge)
                        
        return board
    
    def isEdges(self, row, col, m, n):
        return row == 0 or row == m - 1 or col == 0 or col == n - 1
    
    def isOutBounded(self, row, col, m, n):
        return row < 0 or row >= m or col < 0 or col >= n
    
    def dfs(self, board, row, col, onEdge):
        m = len(board)
        n = len(board[0])
        
        if (row, col) not in onEdge:
            if self.isEdges(row, col, m, n):  
                onEdge.add((row, col))
            else:                
                board[row][col] = "X"
            
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for pos in neighbors:
            offsetR, offsetC = pos
            newRow = row + offsetR
            newCol = col + offsetC
            if self.isOutBounded(newRow, newCol, m, n):
                continue
            if board[newRow][newCol] == "O" and (newRow, newCol) not in onEdge: 
                if (row, col) in onEdge:                   
                    onEdge.add((newRow, newCol))
                self.dfs(board, newRow, newCol, onEdge)
        