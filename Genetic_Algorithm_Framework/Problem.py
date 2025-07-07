from typing import Dict, Any, List
import math
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

class SubsetSumProblem(Problem):
    def __init__(self, numbers: List[int], target: int = None):
        self.numbers: List[int] = numbers
        self.target: int = target if target is not None else sum(numbers) // 2
        self.chromo_len: int = len(numbers)

    def subset_sum_value(self, chromosome: List[int]) -> Dict[str, int]:
        selected_sum = sum(self.numbers[i] for i, gene in enumerate(chromosome) if gene == 1)
        difference = abs(self.target - selected_sum)
        return {"selected_sum": selected_sum, "difference": difference}

    def fitness(self, chromosome: List[int]) -> float:
        result = self.subset_sum_value(chromosome)
        return float(self.target - result["difference"])

    def random_ind(self) -> List[int]:
        return [random.randint(0, 1) for _ in range(self.chromo_len)]

    def heuristic_ind(self) -> List[int]:
        pass

    def get_mets(self, chromosome: List[int]) -> Dict[str, Any]:
        result = self.subset_sum_value(chromosome)
        return {
            "Subset_Sum": result["selected_sum"],
            "Target": self.target,
            "Difference": result["difference"]
        }

class MultiDimensionalKnapsackProblem(Problem):

    def __init__(self, values: List[int], weights: List[List[int]], capacities: List[int], optimal_value: float = None):
        self.values: List[int] = values
        self.weights: List[List[int]] = weights
        self.capacities: List[int] = capacities
        self.chromo_len: int = len(values)
        self.num_dims: int = len(capacities)
        self.optimal_value: float = optimal_value 

    def calculate_solution(self, chromosome: List[int]) -> Dict[str, Any]:
        total_value = 0
        total_weights = [0] * self.num_dims
        for i, gene in enumerate(chromosome):
            if gene == 1:
                total_value += self.values[i]
                for j in range(self.num_dims):
                    total_weights[j] += self.weights[i][j]
        
        is_valid = all(total_weights[j] <= self.capacities[j] for j in range(self.num_dims))
        return {
            "total_value": total_value,
            "total_weights": total_weights,
            "is_valid": is_valid
        }

    def fitness(self, chromosome: List[int]) -> float:
        result = self.calculate_solution(chromosome)

        if not result["is_valid"]:
            return 0.0
        
        return float(result["total_value"])

    def random_ind(self) -> List[int]:
        return [random.randint(0, 1) for _ in range(self.chromo_len)]

    def get_mets(self, chromosome: List[int]) -> Dict[str, Any]:
        result = self.calculate_solution(chromosome)
        final_value = result["total_value"]
        
        metrics = {
            "Final_Value": final_value,
            "Is_Valid": result["is_valid"],
        }
        
        if self.optimal_value is not None and result["is_valid"]:
            metrics["Optimal_Value"] = self.optimal_value
            
            absolute_error = self.optimal_value - final_value
            metrics["Absolute_Error"] = absolute_error
            if self.optimal_value > 0:
                relative_error = (self.optimal_value - final_value) / self.optimal_value
                metrics["Optimality_Gap_Percent"] = relative_error * 100
            else:
                metrics["Optimality_Gap_Percent"] = 0.0

        for i in range(self.num_dims):
            slack = self.capacities[i] - result["total_weights"][i]
            metrics[f"Dim{i+1}_Weight"] = result["total_weights"][i]
            metrics[f"Dim{i+1}_Capacity"] = self.capacities[i]
            metrics[f"Dim{i+1}_Slack"] = slack
        
        return metrics
class BinPackingProblem(Problem):
    def __init__(self, item_sizes: List[int], bin_capacity: int):
        self.item_sizes: List[int] = item_sizes
        self.bin_capacity: int = bin_capacity
        self.chromo_len: int = len(item_sizes)
        self.max_bins: int = len(item_sizes) 
        
        if self.bin_capacity > 0:
            total_size_sum = sum(self.item_sizes)
            self.lower_bound = math.ceil(total_size_sum / self.bin_capacity)
        else:
            self.lower_bound = float('inf')

    def calculate_packing(self, chromosome: List[int]) -> Dict[str, Any]:
        bin_loads = {}  
        for item_idx, bin_idx in enumerate(chromosome):
            if bin_idx not in bin_loads:
                bin_loads[bin_idx] = 0
            bin_loads[bin_idx] += self.item_sizes[item_idx]
        
        total_overload = sum(max(0, load - self.bin_capacity) for load in bin_loads.values())
        num_bins_used = len(bin_loads)
        
        return {
            "num_bins_used": num_bins_used,
            "total_overload": total_overload,
            "is_valid": total_overload == 0
        }

    def fitness(self, chromosome: List[int]) -> float:
        result = self.calculate_packing(chromosome)
        if result["total_overload"] > 0:
            return 1 / (1 + result["total_overload"]) 

        else:
            return float(self.max_bins + 1 - result["num_bins_used"])

    def random_ind(self) -> List[int]:
        return [random.randint(0, self.max_bins - 1) for _ in range(self.chromo_len)]

    def heuristic_ind(self) -> List[int]:
        pass

    def get_mets(self, chromosome: List[int]) -> Dict[str, Any]:
        result = self.calculate_packing(chromosome)

        metrics = {
            "Num_Bins_Used": result["num_bins_used"],
            "Is_Valid": result["is_valid"],
            "Lower_Bound": self.lower_bound,
            "Total_Overload": result["total_overload"],
            "Gap_vs_Lower_Bound": -1,  
            "Approximation_Ratio": -1.0   
        }

        if result["is_valid"] and self.lower_bound > 0:
            gap = result["num_bins_used"] - self.lower_bound
            metrics["Gap_vs_Lower_Bound"] = gap

            approx_ratio = result["num_bins_used"] / self.lower_bound
            metrics["Approximation_Ratio"] = approx_ratio

        return metrics
