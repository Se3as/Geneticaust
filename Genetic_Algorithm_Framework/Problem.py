from typing import Dict, Any, List
import random

class Problem:

    def fitness(self, chromosome: List[int]) -> float:
        pass
    def random_ind(self) -> List[int]:
        pass
    def heuristic_ind(self) -> List[int]:
        pass
    def get_mets(self, chromosome: List[int]) -> Dict[str, Any]:
        pass

class PartitionProblem(Problem):

    def __init__(self, numbers: List[int]):
        self.numbers: List[int] = numbers 
        self.total_sum: int = sum(numbers) 
        self.chromo_len: int = len(numbers)  

    def partition_sums(self, chromosome: List[int]) -> Dict[str, int]:
        sum1 = sum(self.numbers[i] for i, gene in enumerate(chromosome) if gene == 1)
        sum2 = self.total_sum - sum1
        difference = abs(sum1 - sum2)
        return {"sum1": sum1, "sum2": sum2, "difference": difference}

    def fitness(self, chromosome: List[int]) -> float:
        partition = self.partition_sums(chromosome)
        return float(self.total_sum - partition["difference"])

    def random_ind(self) -> List[int]:
        return [random.randint(0, 1) for _ in range(self.chromo_len)]

    def heuristic_ind(self) -> List[int]:
        pass

    def get_mets(self, chromosome: List[int]) -> Dict[str, Any]:
        partition = self.partition_sums(chromosome)
        return {
            "Partition1_Sum": partition["sum1"],
            "Partition2_Sum": partition["sum2"],
            "Partition_Difference": partition["difference"]
        }

class MultiKnapsackProblem(Problem):
    def __init__(self, items: List[int], weight: List[int], price: List[int],
                 capacity1: int, capacity2: int):
        self.items = items
        self.weight = weight
        self.price = price
        self.capacity1 = capacity1
        self.capacity2 = capacity2
        self.chromo_len = len(items)
    
    def fitness(self, chromosome: List[int]) -> float:
        weight1 = weight2 = total_price = 0
        for i, gene in enumerate(chromosome):
            if gene == 1:
                weight1 += self.weight[i]
                total_price += self.price[i]
            elif gene == 2:
                weight2 += self.weight[i]
                total_price += self.price[i]
        if weight1 > self.capacity1 or weight2 > self.capacity2:
            return 0   # exceed the capacity
        return total_price
    
    def random_ind(self) -> List[int]:
        return [random.randint(0, 2) for _ in range(self.chromo_len)]
    
    def heuristic_ind(self) -> List[int]:
        # Add first in knapsack 1 full and then knapsack 2
        chromo = [0] * self.chromo_len
        weight1 = weight2 = 0
        for i in sorted(range(self.chromo_len), key=lambda x:
                        self.price[x]/self.weight[x], reverse=True):
            if weight1 + self.weight[i] <= self.capacity1:
                chromo[i] = 1
                weight1 += self.weight[i]
            elif weight2 + self.weight[i] <= self.capacity2:
                chromo[i] = 2
                weight2 += self.weight[i]
        return chromo

    def get_mets(self, chromosome: List[int]) -> Dict[str, Any]:
        weight1 = weight2 = total_price = 0
        for i, gene in enumerate(chromosome):
            if gene == 1:
                weight1 += self.weight[i]
                total_price += self.price[i]
            elif gene == 2:
                weight2 += self.weight[i]
                total_price += self.price[i]
        return {
            "Knapsack1_Weight": weight1,
            "Knapsack2_Weight": weight2,
            "Total_Value": total_price,
            "Valid": weight1 <= self.capacity1 and weight2 <= self.capacity2
        }