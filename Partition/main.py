import time
from typing import List, Any
from exhaustive import PartitionEx
from dp import PartitionDP
from logger import Log

def run_tests(
    solver_instance: Any, 
    test_name: str, 
    data: List[int], 
    num_runs: int, 
    logger: Log
):
    item_count = len(data)
    
    for _ in range(num_runs):
        start_time = time.perf_counter()
        solver_instance.solve(data)
        end_time = time.perf_counter()
        duration = (end_time - start_time) * 100000
        logger.add(test_name, duration, item_count)
        

def main():
    test_nums: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num_runs: int = 15
    logger = Log("partition.csv")
    
    tests_to_run = [
        (PartitionEx(), "PartitionExhaustive"),
        (PartitionDP(), "PartitionDP")
    ]

    for solver, name in tests_to_run:
        run_tests(
            solver_instance=solver,
            test_name=name,
            data=test_nums,
            num_runs=num_runs,
            logger=logger
        )

    logger.save()

if __name__ == "__main__":
    main()