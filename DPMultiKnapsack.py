
def DPMultiKnapsack(items, weight, volume, price, capacity_w, capacity_v):
  elements = len(items)
  dp = [[0] * (capacity_v + 1) for _ in range(capacity_w + 1)]

  # Create a 2d matrix to store the maximum price
  for i in range(elements):
    for w in range(capacity_w, weight[i] - 1, -1):
      for v in range(capacity_v, volume[i] - 1, -1):
        if w >= weight[i] and v >= volume[i]:
          dp[w][v] = max(dp[w][v], dp[w - weight[i]][v - volume[i]] + price[i])
  return dp[capacity_w][capacity_v]

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

  result = DPMultiKnapsack(items, weight, volume, price, capacity_w, capacity_v)
  print("Best result:", result)
