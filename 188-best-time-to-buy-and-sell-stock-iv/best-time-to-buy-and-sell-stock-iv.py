class Solution:
    def maxProfit(self, k, prices):
        if not prices or k == 0:
            return 0

        n = len(prices)
        
        # Optimization for large k
        if k >= n // 2:
            max_p = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    max_p += prices[i] - prices[i-1]
            return max_p

        # DP state initialization
        # buy[j] = max profit after j-th purchase
        # sell[j] = max profit after j-th sale
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for j in range(1, k + 1):
                # Update buying state: either stay as is or buy using profit from prev sale
                if sell[j-1] - price > buy[j]:
                    buy[j] = sell[j-1] - price
                
                # Update selling state: either stay as is or sell the current stock
                if buy[j] + price > sell[j]:
                    sell[j] = buy[j] + price

        return sell[k]
