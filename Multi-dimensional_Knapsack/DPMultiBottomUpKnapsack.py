# Implementation of bottom-up dp

class DPBottomUpKnapsack:
    
    def run(self, items, weight, price, capacity1, capacity2):
        return self.DPMultiKnapsack(items, weight, price, capacity1, capacity2)

    def DPMultiKnapsack(self, items, weight, price, capacity1, capacity2):
        elements = len(items)
        # dp[i][w1][w2]: máximo valor usando los primeros i ítems con capacidades w1 y w2
        dp = [[[0 for _ in range(capacity2 + 1)] for _ in range(capacity1 + 1)] for _ in range(elements + 1)]

        for i in range(1, elements + 1):
            wi = weight[i - 1]
            pi = price[i - 1]
            for w1 in range(capacity1 + 1):
                for w2 in range(capacity2 + 1):
                    # No meter el ítem
                    dp[i][w1][w2] = dp[i - 1][w1][w2]
                    # Meter en mochila 1 si cabe
                    if w1 >= wi:
                        dp[i][w1][w2] = max(dp[i][w1][w2], dp[i - 1][w1 - wi][w2] + pi)
                    # Meter en mochila 2 si cabe
                    if w2 >= wi:
                        dp[i][w1][w2] = max(dp[i][w1][w2], dp[i - 1][w1][w2 - wi] + pi)
        return dp[elements][capacity1][capacity2]

if __name__ == "__main__":
    # items to be placed in the knapsacks
    items = [1, 2, 3, 4, 5]
    # restrictions
    # weight of items
    weight = [5, 2, 6, 10, 7]
    # capacities
    capacity1= 10
    capacity2 = 15
    # price of items
    price = [20, 10, 30, 50, 40]

    Knapsack = DPBottomUpKnapsack()
    result = Knapsack.DPMultiKnapsack(items, weight, price, capacity1, capacity2)
    print("Best price:", result)
