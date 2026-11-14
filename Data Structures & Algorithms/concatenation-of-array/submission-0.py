class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        mans = []
        for val in nums:
            mans += [val]
        for second in nums:
            mans += [second]
        # nums of length n 
        # create ans
        # ans[i] == nums[i], ans[i+n] == nums[i]
        return mans
        