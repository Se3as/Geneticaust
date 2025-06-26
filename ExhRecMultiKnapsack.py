
def findExhaustiveRec(current, items, elements, 
                      weight1, weight2, capacity1, capacity2):

  # Base case: no more items to consider
  if current == elements:
    return 0 
  
  # Case 1: skip the current item
  skipResult = findExhaustiveRec(current + 1, items, elements,
                                weight1, weight2, capacity1, capacity2)

  # Case 2: include the current item in the first knapsack if it fits
  takeInFirst = 0
  if weight1[current] <= capacity1:
    takeInFirst = items[current] + findExhaustiveRec(
        current + 1, items, elements, 
        weight1, weight2, capacity1 - weight1[current], capacity2)

  # Case 3: include the current item in the second knapsack if it fits
  takeInSecond = 0
  if weight2[current] <= capacity2:
    takeInSecond = items[current] + findExhaustiveRec(
        current + 1, items, elements, 
        weight1, weight2, capacity1, capacity2 - weight2[current])

  # Return the maximum value obtained from all cases
  result = max(skipResult, takeInFirst, takeInSecond)
  return result

def ExhRecMultiKnapsack(items, weight1, weight2, capacity1, capacity2):
  elements = len(items)
  current = 0  # start from the first item
  best_result = findExhaustiveRec(current, items, elements, 
                                  weight1, weight2, capacity1, capacity2)
  return best_result

if __name__ == "__main__":
  items = [1, 2, 3, 4, 5]
  # weights for two knapsacks
  weight1 = [2, 3, 4, 5, 6]
  weight2 = [3, 4, 5, 6, 7]
  # capacities of the two knapsacks
  capacity1 = 10
  capacity2 = 15
  result = ExhRecMultiKnapsack(items, weight1, weight2, capacity1, capacity2)
  print("Best result:", result)
