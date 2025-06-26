
def findExhaustiveRec(current, items, elements, 
                      weight, volume, price, capacity1, capacity2):

  # Base case: no more items to consider
  if current == elements:
    return 0 
  
  # Case 1: skip the current item
  skipResult = findExhaustiveRec(current + 1, items, elements,
                                weight, volume, price, capacity1, capacity2)

  # Case 2: include the current item in the first knapsack if it fits
  takeInFirst = 0
  if weight[current] <= capacity1 and volume[current] <= capacity1:
    takeInFirst = price[current] + findExhaustiveRec(
        current + 1, items, elements, 
        weight, volume, price, capacity1 - weight[current], capacity2)

  # Case 3: include the current item in the second knapsack if it fits
  takeInSecond = 0
  if weight[current] <= capacity2 and volume[current] <= capacity2:
    takeInSecond = price[current] + findExhaustiveRec(
        current + 1, items, elements, 
        weight, volume, price, capacity1, capacity2 - volume[current])

  # Return the maximum value obtained from all cases
  result = max(skipResult, takeInFirst, takeInSecond)
  return result

def ExhRecMultiKnapsack(items, weight, volume, price, capacity1, capacity2):
  elements = len(items)
  current = 0  # start from the first item
  best_result = findExhaustiveRec(current, items, elements, 
                                  weight, volume, price, capacity1, capacity2)
  return best_result

if __name__ == "__main__":
  # items to be placed in the knapsacks
  items = [1, 2, 3, 4, 5]
  # restrictions for both knapsacks
  # weights of items
  weight = [5, 2, 6, 10, 7]
  # volumes of items
  volume = [3, 1, 5, 7, 6]
  # price of items
  price = [20, 10, 30, 50, 40]
  # capacities of the two knapsacks
  capacity1 = 10
  capacity2 = 15
  result = ExhRecMultiKnapsack(items, weight, volume, price, capacity1, capacity2)
  print("Best result:", result)
