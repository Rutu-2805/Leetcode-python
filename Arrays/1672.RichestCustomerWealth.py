class Solution(object):
    def maximumWealth(self, accounts):

        max_wealth = 0
        for i in accounts:
            total_wealth = 0
            
            for amount in i :
                total_wealth += amount
            
            if(total_wealth > max_wealth):
                max_wealth = total_wealth

        return max_wealth