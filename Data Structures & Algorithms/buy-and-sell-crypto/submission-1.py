class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 10 1 5 6 7 1
        # they are asking for max_profit over a list of numbers
        # order matters, sliding window with criteria for moving the ends makes sense
        # recommended is O(n) time so sliding window is good
        # 10 - left, 1 is less, move l.point to 1 right is none
        # 1 - left, 5 is more, move right to 5, max profit 4
        # 1 - left, 6 is more, move right to 6, max profit 5
        # 1 - left, 7 is more, move right to 7, max profit 6
        # 1 = 1 so 1 is still left, max profit = 6 final

        # 10 - l right is none, max profit = 0
        # 8 - l right is none, max profit = 0
        # ..., max_profit=0

        max_profit = 0
        left = None
        right = None
        for price in prices:
            if left is None:
                left = price
                # right still none, profit 0
            else:
                # left is set, therefore check if right should be set
                if price < left:
                    left = price
                    right = None
                elif right is None or right < price:
                    right = price
                    current_max_profit = right-left
                    max_profit = current_max_profit if max_profit < current_max_profit else max_profit
                else:
                    # right is largest, do nothing
                    continue
        return max_profit
            
        