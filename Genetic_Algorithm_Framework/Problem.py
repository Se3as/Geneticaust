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
