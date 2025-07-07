
def isExhRecSubsetSum(set, element, sum):
  
  # find the sum = 0
  if sum == 0:
    return True
  
  # end of the list
  if element == 0:
    return False
  
  if (set[element - 1] > sum):
    return isExhRecSubsetSum(set, element - 1, sum)
  
  if (set[element - 1] <= sum):
    # include the last element in the subset
    # or exclude the last element in the subset
    return (isExhRecSubsetSum(set, element - 1, sum) or 
            isExhRecSubsetSum(set, element - 1, sum - set[element - 1]))

def exhRecSubsetSum(set, element, sum):
  return isExhRecSubsetSum(set, element, sum)

if __name__ == '__main__':
  # example of a list
  set = [3, 34, 4, 12, 5, 2]
  element = len(set)
  sum = 15

  if (exhRecSubsetSum(set, element, sum) == True):
    print("Found it")
  else:
    print("Not found it")

