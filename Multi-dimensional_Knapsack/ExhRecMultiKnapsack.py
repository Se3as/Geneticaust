# Implementation of exhaustive recursive

class ExhRecMultiKnapsack:
    def run(self, items, weight, price, capacity1, capacity2):
        return self.ExhRecMultiKnapsack(items, weight, price, capacity1, capacity2)

    def ExhRecMultiKnapsack(self, items, weight, price, capacity1, capacity2):
        elements = len(items)
        current = 0  # start from the first item
        return self.findExhaustiveRec(current, items, elements, weight, price,
                                            capacity1, capacity2)

    def findExhaustiveRec(self, current, items, elements, weight, price, 
                          capacity1, capacity2):
        # Base case: no more items to consider
        if current == elements:
            return 0

        # Case 1: skip the current item
        skip_value = self.findExhaustiveRec(current + 1, items, elements,
                                                      weight, price, 
                                                      capacity1, capacity2)
        take_in_first = 0
        # Case 2: include the current item in the first knapsack if it fits
        if weight[current] <= capacity1:
            take_in_first = price[current] + self.findExhaustiveRec(current + 1, items,
                                        elements, weight, price,
                                        capacity1 - weight[current], capacity2)
        take_in_second = 0 
        # Case 3: include the current item in the second knapsack if it fits
        if weight[current] <= capacity2:
            take_in_second = price[current] + self.findExhaustiveRec(current + 1, items, 
                                        elements, weight, price,
                                        capacity1, capacity2 - weight[current])

        best_value = max(skip_value, take_in_first, take_in_second)
        return best_value

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

  Knapsack = ExhRecMultiKnapsack()
  best_price = Knapsack.run(items, weight, price, capacity1, capacity2)
  
  print("Total best price:", best_price)
