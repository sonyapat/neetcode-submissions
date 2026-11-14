class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in myDict:
                return [myDict[complement], index]
            myDict[value] = index


            
        