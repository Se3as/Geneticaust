import time
import random
from typing import List, Any
from exhaustive import PartitionEx
from dp import PartitionDP
from dp_bu import PartitionDPBottomUp
from logger import Log

def generate_worst_case_list(n: int) -> List[int]:
    worst_list: List[int] = [3] * (n - 1) 
    worst_list.append(5)
    return worst_list

def generate_medium_case_list(n: int, max_value: int = 1000) -> List[int]:
    medium_list: List[int] = [random.randint(1, max_value) for _ in range(n)]  
    if sum(medium_list) % 2 != 0:
        medium_list[-1] += 1
    return medium_list

def run_test(
    method_test: Any, 
    name: str, 
    total_sum: List[int], 
    logger: Log
):
    count: int = len(total_sum)  
    start_time: float = time.perf_counter()  
    method_test.solve(total_sum)
    end_time: float = time.perf_counter()  
    duration: float = (end_time - start_time) * 1000  
    logger.add(name, duration, count, sum(total_sum))

if __name__ == "__main__":
    random.seed(777)
    N_ELEMENTS_WORSE: int = 26  
    N_ELEMENTS_MEDIUM: int = 26 
    logger: Log = Log("partition.csv")  
    
    methods: List[tuple] = [
        (PartitionEx(),"PartitionExhaustive"), 
        (PartitionDP(),"PartitionDP_TopDown"),
        (PartitionDPBottomUp(),"PartitionDP_BottomUp"),
    ]  

    worst_case_list: List[int]  = generate_worst_case_list(N_ELEMENTS_WORSE)  
    medium_case_list_og: List[int] = generate_medium_case_list(N_ELEMENTS_MEDIUM)  
    
    for method, name in methods:
        run_test(
            method_test=method,
            name=f"{name}_WorstCase",
            total_sum=worst_case_list,
            logger=logger
        )

    for method, name in methods:
        if "PartitionExhaustive" in name and N_ELEMENTS_MEDIUM < 51:
            run_test(
                method_test=method,
                name=f"{name}_MediumCase",
                total_sum=medium_case_list_og,
                logger=logger
            )
        elif "PartitionDP" in name:  
            run_test(
                method_test=method,
                name=f"{name}_MediumCase",
                total_sum=medium_case_list_og,
                logger=logger
            )

    logger.save()


