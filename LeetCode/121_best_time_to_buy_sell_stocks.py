from typing import  List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for elem in prices[1:]:
            # print(elem, buy_price, max_profit)
            if elem < buy_price:
                buy_price = elem
            else:
                current_profit = elem - buy_price
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit
    # def maxProfit(self, prices: List[int]) -> int:
    #     buy_price = prices[0]
    #     max_profit = 0
    #     for elem in prices:
    #         print(elem, buy_price, max_profit)
    #         if elem < buy_price:
    #             buy_price = elem
    #         else:
    #             current_profit = elem - buy_price
    #             max_profit = max(max_profit, current_profit)
    #     return max_profit

my_obj = Solution()
print(my_obj.maxProfit([7,6,4,3,1]))