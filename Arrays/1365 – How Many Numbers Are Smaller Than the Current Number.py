class Solution(object):
    def smallerNumberThanCurrrent(self, nums):
        result_list = []
        for current in nums:
            counter = 0

            for others in nums:

                if current > others :
                    counter+=1

            result_list.append(counter)

        return result_list
    
print(Solution().smallerNumberThanCurrrent([1,2,4]))
            
