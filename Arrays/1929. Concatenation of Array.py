class Solution(object):
    def getConcatenation(self, nums):

        # Solution 1
        ans = []
        for i in nums:
            ans.append(i)

        for i in nums:
            ans.append(i)

        return ans
    
        # Solution 2
        result = []
        for i in nums:
            result.append(i)

        return result+result
    
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        # Solution 1: Using two loops.
        # Solution 2: Using Python list concatenation (nums + nums or nums * 2).
        # Both are accepted on LeetCode.
        """

        
        
    

            