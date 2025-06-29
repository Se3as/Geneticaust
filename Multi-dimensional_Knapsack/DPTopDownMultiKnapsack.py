# Implementation of top-down dp

class DPTopDownMultiKnapsack:
    def run(self, items, weight, price, capacity1, capacity2):
        return self.DPTopDownMultiKnapsack(items, weight, price, capacity1, capacity2)

    def DPTopDownMultiKnapsack(self, items, weight, price, capacity1, capacity2):
        elements = len(items)
        current = 0  # start from the first items
        memo = [[-1 for _ in range(capacity2 + 1)] for _ in range(capacity1 + 1)]
        return self.findTopDown(current, items, elements, weight, price,
                                    capacity1, capacity2, memo)

    def findTopDown(self, current, items, elements,
                  weight, price, capacity1, capacity2, memo):
        # Base case: if all items have been considered
        if current == elements:
            return 0
        
        if memo[capacity1][capacity2] != -1:
            return memo[capacity1][capacity2]
    
        # Case 1: skip the current item
        skip_value = self.findTopDown(current + 1, items, elements,
                                    weight, price, capacity1, capacity2, memo)

        # Case 2: include the current item in the first knapsack if it fits
        take_in_first = 0
        if weight[current] <= capacity1:
            take_in_first = price[current] + self.findTopDown(
                current + 1, items, elements, weight, price,
                capacity1 - weight[current], capacity2, memo)

        # Case 3: include the current item in the second knapsack if it fits
        take_in_second = 0
        if weight[current] <= capacity2:
            take_in_second = price[current] + self.findTopDown(
                current + 1, items, elements, weight, price,
                capacity1, capacity2 - weight[current], memo)

        memo[capacity1][capacity2] = max(skip_value, take_in_first, take_in_second)

        # Return the maximum value obtained from all cases
        return memo[capacity1][capacity2]

if __name__ == "__main__":
  # items to be placed in the knapsacks
  items = [1, 2, 3, 4, 5]
  # restrictions
  # weight of items
  weight = [5, 2, 6, 10, 7]
  # capacities of knapsacks
  capacity1 = 10
  capacity2 = 15

  # price of items
  price = [20, 10, 30, 50, 40]

  Knapsack = DPTopDownMultiKnapsack()
  best_price = Knapsack.run(items, weight, price, capacity1, capacity2)
  print("Total best price:", best_price)

