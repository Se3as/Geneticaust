from typing import List
import random

class Problem:

    def fitness(self, chromosome: List[int]) -> float:
        pass
    def random_ind(self) -> List[int]:
        pass
    def heuristic_ind(self) -> List[int]:
        pass

class PartitionProblem(Problem):

    def __init__(self, numbers: List[int]):
        self.numbers: List[int] = numbers 
        self.total_sum: int = sum(numbers) 
        self.chromo_len: int = len(numbers)  

    def fitness(self, chromosome: List[int]) -> float:
        subset1_sum: int = sum(self.numbers[i] for i, gene in enumerate(chromosome) if gene == 1)
        subset2_sum: int = self.total_sum - subset1_sum
        difference: int = abs(subset1_sum - subset2_sum)
        return float(self.total_sum - difference)  

    def random_ind(self) -> List[int]:
        return [random.randint(0, 1) for _ in range(self.chromo_len)]

    def heuristic_ind(self) -> List[int]:
        pass