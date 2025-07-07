from typing import List, Dict, Tuple

class PartitionDPBottomUp:
    def solve(self, nums: List[int]) -> bool:
        return self.can_partition_bottom_up(nums)

    def can_partition_bottom_up(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True
            if dp[target]:
                return True

        return dp[target]
