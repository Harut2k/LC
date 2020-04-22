#Time Complexity O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if(length ==0):
            return 0
        min = prices[0]
        profit = 0 
        for i in range(0,length):
            if(prices[i] < min):
                min = prices[i]
            if(prices[i]-min > profit):
                profit = prices[i]-min
        return profit
