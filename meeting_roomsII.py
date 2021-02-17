class Solution:
    '''
        example 2 => intervals = [[2,4], [7,10]]
        {1: [0, 30], 2: [5,10] [15.20]}
        meetings = [[0,30]] counter = 1
        start < 30 => counter += 1 => meetingn=[30, 20]
        
        1. sort my intervals
        2. create a new roomEndtimes(n) = []
        3. iterate through intervals(n) => compare start time(new meetings) to end time(meeting in progress)
        4. if roomEndtimes is empty, insert the end time, otherwise, we compare.Time: O(n) to O(n^2) space: O(n)
        Note: we can implement minheap to improve the time complexity
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort() 
        roomEndTimes = []
        
        for interval in intervals:
            start, end = interval #start = 7, end = 10
            if not roomEndTimes:
                roomEndTimes.append(end) # [9]
            else: 
                for i, endTime in enumerate(roomEndTimes):
                    if start >= endTime:                        
                        roomEndTimes[i] = end
                        break
                else:                     
                    roomEndTimes.append(end)
                                
        return len(roomEndTimes)
        