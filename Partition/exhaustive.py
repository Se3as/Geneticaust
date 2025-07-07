from typing import List

class PartitionEx:

    def solve(self, nums: List[int]) -> bool:
        return self.can_partition(nums)

    def can_partition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        return self.partition(nums, 0, 0, 0)

    def partition(self, nums: List[int], index: int, sum1: int, sum2: int) -> bool:
        if index == len(nums):
            return sum1 == sum2 and sum1 > 0
        
        current_element: int = nums[index]

        if self.partition(nums, index + 1, sum1 + current_element, sum2):
            return True
        
        return self.partition(nums, index + 1, sum1, sum2 + current_element)