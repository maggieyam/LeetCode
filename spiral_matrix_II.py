class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for i in range(n)]         
        layer = 0
        count = 0
        while n > 1:
            print(layer)
            print(res)
            for col in range(layer, n - 1 + layer):
                count += 1
                res[layer][col] = count
                
            for row in range(layer, n - 1 + layer):
                count += 1
                res[row][n - 1 + layer] = count
                
            for col in range(n - 1 + layer, layer, -1):
                count += 1 
                res[n - 1 + layer][col] = count
                              
            for row in range(n - 1 + layer, layer, -1):
                count += 1
                res[row][layer] = count                
                
            n -= 2
            layer += 1
        if n == 1:
            res[layer][layer] = count + 1
        return res