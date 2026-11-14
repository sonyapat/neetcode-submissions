class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # sortedStr
        for word in strs:
            letList = sorted(word)
            key = "".join(letList)
            if key not in groups: 
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
        
        