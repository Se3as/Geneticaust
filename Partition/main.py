import time
import random
from typing import List, Any
from exhaustive import PartitionEx
from dp import PartitionDP
from logger import Log

def generate_worst_case_list(n: int) -> List[int]:
    worst_list: List[int] = [3] * (n - 1) 
    worst_list.append(5)
    return worst_list

def generate_medium_case_list(n: int, max_value: int = 100) -> List[int]:
    medium_list: List[int] = [random.randint(1, max_value) for _ in range(n)]  
    if sum(medium_list) % 2 != 0:
        medium_list[-1] += 1
    return medium_list

def run_test(
    solver_instance: Any, 
    test_name: str, 
    data: List[int], 
    num_runs: int, 
    logger: Log
):
    item_count: int = len(data)  
    if "WorstCase" in test_name:
        num_runs: int = 1
    for _ in range(num_runs):
        start_time: float = time.perf_counter()  
        solver_instance.solve(data)
        end_time: float = time.perf_counter()  
        duration: float = (end_time - start_time) * 1000000  
        logger.add(test_name, duration, item_count, sum(data))

def main():
    N_ELEMENTS_WORSE: int = 26  
    NUM_RUNS: int = 2  
    NUM_RUNS_PER_LIST: int = 10  
    N_ELEMENTS_MEDIUM: int = 30  
    logger: Log = Log("partition.csv")  
    
    solvers_to_test: List[tuple] = [
        (PartitionEx(), "PartitionExhaustive"), 
        (PartitionDP(), "PartitionDP")
    ]  

    worst_case_list: List[int] = generate_worst_case_list(N_ELEMENTS_WORSE)  
    
    for solver, name in solvers_to_test:
        run_test(
            solver_instance=solver,
            test_name=f"{name}_WorstCase",
            data=worst_case_list,
            num_runs=NUM_RUNS_PER_LIST,
            logger=logger
        )
    for _ in range(NUM_RUNS):
        medium_case_list: List[int] = generate_medium_case_list(N_ELEMENTS_MEDIUM)  
        for solver, name in solvers_to_test:
            run_test(
                solver_instance=solver,
                test_name=f"{name}_MediumCase",
                data=medium_case_list,
                num_runs=NUM_RUNS_PER_LIST,
                logger=logger
            )

    logger.save()

if __name__ == "__main__":
    main()
