
def findExhaustiveRec(current, items, elements,
                      weight, volume, price, capacity_w, capacity_v):

  # Base case: no more items to consider
  if current == elements:
    return 0 
  
  # Case 1: skip the current item
  skipResult = findExhaustiveRec(current + 1, items, elements,
                                weight, volume, price, capacity_w, capacity_v)

  # Case 2: include the current item in the first knapsack if it fits
  takeInFirst = 0
  if weight[current] <= capacity_w and volume[current] <= capacity_v:
    takeInFirst = price[current] + findExhaustiveRec(
        current + 1, items, elements, 
        weight, volume, price,
        capacity_w - weight[current], capacity_v - volume[current])
    
  # Return the maximum value obtained from all cases
  return max(skipResult, takeInFirst)

def ExhRecMultiKnapsack(items, weight, volume, price, capacity_w, capacity_v):
  elements = len(items)
  current = 0  # start from the first item
  best_result = findExhaustiveRec(current, items, elements, 
                                  weight, volume, price,
                                  capacity_w, capacity_v)
  return best_result

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
  capacity_w = 10
  capacity_v = 10

  result = ExhRecMultiKnapsack(items, weight, volume, price, capacity_w, capacity_v)
  print("Best price:", result)
