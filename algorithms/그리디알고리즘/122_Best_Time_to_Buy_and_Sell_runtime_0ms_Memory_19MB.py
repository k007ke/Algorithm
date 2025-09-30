class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cha_list=[]
        result=0
        for i in range(0,len(prices)-1):
            cha=prices[i+1]-prices[i]
            if cha>0:
                result+=cha
        return result