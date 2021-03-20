 def __init__(self):
        self.startTable = {}
        self.timeRecord = collections.defaultdict(lambda: [0, 0])
    
    def checkIn(self, id: int, stationName: str, t: int):
        self.startTable[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int):
        startStation, startT = self.startTable[id]
        total, count = self.timeRecord[(startStation, stationName)]
        total += t - startT
        count += 1
        self.timeRecord[(startStation, stationName)] = (total, count)
        del self.startTable[id]
        
    def getAverageTime(self, startStation: str, endStation: str):
        total, count = self.timeRecord[(startStation, endStation)]        
        return total / count