# Implementation of bottom-up dp

class DPBottomUpMultiKnapsack:
    
    def run(self, items, weight, price, capacity1, capacity2):
        return self.DPMultiKnapsack(items, weight, price, capacity1, capacity2)

    def DPMultiKnapsack(self, items, weight, price, capacity1, capacity2):
        dp = [[0 for _ in range(capacity2 + 1)] for _ in range(capacity1 + 1)]
        elements = len(items)

        for i in range(elements):
            wi = weight[i]
            pi = price[i]
            # Actualiza en orden inverso para evitar sobrescribir
            for w1 in range(capacity1, -1, -1):
                for w2 in range(capacity2, -1, -1):
                        if w1 >= wi:
                            dp[w1][w2] = max(dp[w1][w2], dp[w1 - wi][w2] + pi)
                        if w2 >= wi:
                            dp[w1][w2] = max(dp[w1][w2], dp[w1][w2 - wi] + pi)
        
        return dp[capacity1][capacity2]
'''
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

    Knapsack = DPBottomUpMultiKnapsack()
    result = Knapsack.DPMultiKnapsack(items, weight, price, capacity1, capacity2)
    print("Best price:", result)
'''
