import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minvalue = math.inf
        maxvalue = 0
        for i in prices:
            if i<minvalue:
                minvalue = i
            elif maxvalue< i- minvalue:
                maxvalue = i- minvalue
        return maxvalue
        