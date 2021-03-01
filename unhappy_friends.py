class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
               
        def createPreferenceDict(preferences, friendsTable, n):
            for i, preference in enumerate(preferences):
                friends = [None] * n
                for j, person in enumerate(preference):
                    friends[person] = j
                friendsTable[i] = friends                                        
        
        def createPairsDict(pairs, pairsTable):
            for pair in pairs:
                first, second = pair
                pairsTable[first] = second
                pairsTable[second] = first
        
        def isUnhappy(first, rank, preferences, friendTable, pairTable):
            for friend in preferences[first][:rank]:
                partner = pairTable[friend]
                if friendTable[friend][first] < friendTable[friend][partner]:
                    return True
            return False
        
        
        count = 0
        friendsTable = {}
        pairsTable = {}
        createPreferenceDict(preferences, friendsTable, n)
        createPairsDict(pairs, pairsTable)
        
        for pair in pairs:
            for i in range(2):               
                first = pair[i]
                second = pair[(i + 1) % 2]

                # check partner ranking
                rank = friendsTable[first][second] 
                if rank != 0 and isUnhappy(first, rank, preferences, friendsTable, pairsTable):
                    count += 1
        
               
                        
        return count
            