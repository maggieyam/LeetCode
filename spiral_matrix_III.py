class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)            
            for row in matrix:
                if not row:
                    return res
                res.append(row.pop(-1))
            if not matrix:
                return res
            res += matrix.pop(-1)[::-1]            
            for row in reversed(matrix):
                if not row:
                    return res
                res.append(row.pop(0))
        return res