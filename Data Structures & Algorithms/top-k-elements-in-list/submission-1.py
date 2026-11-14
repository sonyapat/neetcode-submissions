class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums: 
            if num not in frequencies: 
                frequencies[num] = 1
            else: 
                frequencies[num] += 1
        sortedFreqs = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))
        return list(sortedFreqs.keys())[0:k]
        