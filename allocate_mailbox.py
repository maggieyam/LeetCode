class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        
        @lru_cache(None)
        def dp(i, j, k):
            if k == 1: 
                total_distance = 0
                while i < j:
                    total_distance += houses[j] - houses[i]
                    i += 1
                    j -= 1
                return total_distance
            
            return min(dp(i,m,k-1) + dp(m+1,j,1) for m in range(i+k-2, j))
        
        return dp(0, len(houses)-1, k)