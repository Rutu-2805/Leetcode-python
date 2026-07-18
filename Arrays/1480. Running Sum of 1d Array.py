class Solution(object):
    def runningSum(self, nums):

# Solution 1
        sum = 0
        result = []
        for i in nums:
            sum += i 
            result.append(sum)

        return result
   

"""
:type nums: List[int]
:rtype: List[int]

"""