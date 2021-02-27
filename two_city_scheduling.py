class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference = []
        for i, cost in enumerate(costs):
            costA, costB = cost
            diff = abs(costA - costB)
            difference.append((diff, i))
        difference.sort(reverse=True)
        cityA = len(costs) // 2
        cityB = cityA
        
        cost = 0
        for diff in difference:
            idx = diff[1]
            costA, costB = costs[idx]
            
            if (costA >= costB and cityB) or cityA <= 0:
                cost += costB
                cityB -= 1
            else:
                cost += costA
                cityA -= 1

        return cost