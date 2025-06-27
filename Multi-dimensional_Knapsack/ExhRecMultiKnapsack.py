
class ExhRecMultiKnapsack:
  def run(self, items, weight, volume, price, capacity1_w, capacity1_v, capacity2_w, capacity2_v):
    return self.ExhRecMultiKnapsack(items, weight, volume, price,
                                    capacity1_w, capacity1_v, capacity2_w, capacity2_v)

  def ExhRecMultiKnapsack(self, items, weight, volume, price,
                          capacity1_w, capacity1_v, capacity2_w, capacity2_v):
    elements = len(items)
    current = 0  # start from the first item
    best_result = self.findExhaustiveRec(current, items, elements, 
                                    weight, volume, price,
                                    capacity1_w, capacity1_v, capacity2_w, capacity2_v)
    return best_result
  
  def findExhaustiveRec(self, current, items, elements,
                        weight, volume, price, capacity1_w, capacity1_v, capacity2_w, capacity2_v):
    # Base case: no more items to consider
    if current == elements:
      return 0 
    
    # Case 1: skip the current item
    skipResult = self.findExhaustiveRec(current + 1, items, elements,
                                  weight, volume, price, capacity1_w, capacity1_v, capacity2_w, capacity2_v)

    # Case 2: include the current item in the first knapsack if it fits
    takeInFirst = 0
    if weight[current] <= capacity1_w and volume[current] <= capacity1_v:
      takeInFirst = price[current] + self.findExhaustiveRec(
          current + 1, items, elements, 
          weight, volume, price,
          capacity1_w - weight[current], capacity1_v - volume[current], capacity2_w, capacity2_v)
    # Case 3: include the current item in the second knapsack if it fits
    takeInSecond = 0
    if weight[current] <= capacity2_w and volume[current] <= capacity2_v:
      takeInSecond = price[current] + self.findExhaustiveRec(
          current + 1, items, elements, 
          weight, volume, price,
          capacity1_w, capacity1_v, 
          capacity2_w - weight[current], capacity2_v - volume[current])
    # Return the maximum value obtained from all cases
    return max(skipResult, takeInFirst, takeInSecond)


if __name__ == "__main__":
  # items to be placed in the knapsacks
  items = [1, 2, 3, 4, 5]
  # restrictions
  # weight of items
  weight = [5, 2, 6, 10, 7]
  # volume of items
  volume = [3, 1, 5, 7, 6]
  # price of items
  price = [20, 10, 30, 50, 40]
  # capacities
  capacity1_w = 10
  capacity1_v = 10
  capacity2_w = 15
  capacity2_v = 15

  knapsack = ExhRecMultiKnapsack()
  result = knapsack.run(items, weight, volume, price, capacity1_w, capacity1_v, capacity2_w, capacity2_v)
  print("Best price for Knapsack 1:", result)
 

