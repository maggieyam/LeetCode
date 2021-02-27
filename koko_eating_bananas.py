    '''
        input = array (all piles of bananas), H: max hours that I have
          output = int (the minumn speed of K)
        
        max speed is max number in piles.
        what's the smallest range and lowest number to start with
        if the H'(10) < H(8), return false (k = 3)
            [3, 3, 3, 3] H = 8 K = 2
        start with 3:
            if 3 works, we keep decrement K by 1
            else, we increment K by 1
    
        piles = [3,6,7,11] => count the max in the pile O(n)
        range: [1, 11], 11 + 1 // 2 = 6 O(nlogm)
        if 6 works [1, 6] => [3, 6]
        else 6 doesn't work [6, 11] => 8
        time complexity O(nlog(m)) n = len(piles),  m = len(range)
        space complecity O(1) 
        
        maxi = 11 
    '''
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def canEatAll(K):          
            return sum((p-1) // K + 1 for p in piles) <= H
    
        lo, hi = 1, max(piles) # (1, 11)       
        while lo < hi: #O(nlog(w))           
            mid = (lo + hi) // 2 # 3            
            if canEatAll(mid): #O(n)
                hi = mid
            else:
                lo = mid + 1
            
        return lo

