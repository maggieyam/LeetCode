class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ans = []
        pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(schedule)]
        heapq.heapify(pq)
        anchor = pq[0][0]

        while pq:
            t, i, j = heapq.heappop(pq)
            if anchor < t:
                ans.append(Interval(anchor, t))
            anchor = max(anchor, schedule[i][j].end)
            if j + 1 < len(schedule[i]):
                heapq.heappush(pq, (schedule[i][j + 1].start, i, j + 1))

        return ans