class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = []           
        anagram = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in anagram:
                anagram[key] = [word]
            else:
                anagram[key].append(word)
        for key in anagram:
            solution.append(anagram[key])
        
        return solution