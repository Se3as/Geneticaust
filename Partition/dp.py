from typing import List, Dict, Tuple

class PartitionDP:

    def solve(self, nums: List[int]) -> bool:
        return self.can_partition(nums)

    def can_partition(self, nums: List[int]) -> bool:
        total_sum: int = sum(nums)
        if total_sum % 2 != 0:
            return False
        temp_results: Dict[Tuple[int, int], bool] = {}
        return self.partition(nums, 0, 0, temp_results)

    def partition(self, nums: List[int], index: int, diff: int, temp_results: Dict[Tuple[int, int], bool]) -> bool:
        state: Tuple[int, int] = (index, diff)
        if state in temp_results:
            return temp_results[state]
        if index == len(nums):
            return diff == 0
        
        current_element: int = nums[index]
        
        add_to_set1: bool = self.partition(nums, index + 1, diff + current_element, temp_results)
        add_to_set2: bool = self.partition(nums, index + 1, diff - current_element, temp_results)
        
        result: bool = add_to_set1 or add_to_set2
        temp_results[state] = result
        return result