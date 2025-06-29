import os
import time
import random
from typing import List, Any
from ExhRecMultiKnapsack import ExhRecMultiKnapsack
from DPTopDownMultiKnapsack import DPTopDownMultiKnapsack
# from DPBottomUpMultiKnapsack import DPBottomUpMultiKnapsack
from logger import Log

def generate_worst_case_data(n: int) -> tuple:
    items = list(range(1, n + 1))
    weight = [3 * random.randint(1, 5) for _ in range(n)]
    price = [random.randint(1, 100) for _ in range(n)]
    return items, weight, price

def generate_medium_case_data(n: int, max_value: int = 100) -> tuple:
    items = list(range(1, n + 1))
    weight = [random.randint(1, max_value) for _ in range(n)]
    price = [random.randint(1, max_value) for _ in range(n)]
    return items, weight, price

def run_test(method_test: Any, name: str, items: List[int], weight: List[int], price: List[int],
             capacity1: int, capacity2: int, logger: Log):
    start_time = time.perf_counter()
    result = method_test.run(items, weight, price, capacity1, capacity2)
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000000
    logger.add(name, duration, len(items), result)
    print(f"{name} result: {result}")

def main():
    random.seed(777)
    N_ELEMENTS_WORST = 16
    N_ELEMENTS_MEDIUM = 25
    CAPACITY_1 = 50
    CAPACITY_2 = 50

    csv_path = os.path.join(os.path.dirname(__file__), "multidimensional_knapsack.csv")
    logger = Log(csv_path)

    methods = [
        (ExhRecMultiKnapsack(), "ExhaustiveRec"),
        (DPTopDownMultiKnapsack(), "TopDownDP"),
        # (DPBottomUpMultiKnapsack(), "BottomUpDP")
    ]

    # Worst Case
    items_w, weights_w, prices_w = generate_worst_case_data(N_ELEMENTS_WORST)
    for method, name in methods:
        run_test(method, f"{name}_WorstCase", items_w, weights_w, prices_w, CAPACITY_1, CAPACITY_2, logger)

    # Medium Cases (increasing subset)
    items_m, weights_m, prices_m = generate_medium_case_data(N_ELEMENTS_MEDIUM)
    for i in range(1, N_ELEMENTS_MEDIUM + 1):
        subset_items = items_m[:i]
        subset_weights = weights_m[:i]
        subset_prices = prices_m[:i]
        for method, name in methods:
            run_test(method, f"{name}_MediumCase_{i}", subset_items, subset_weights, subset_prices,
                     CAPACITY_1, CAPACITY_2, logger)

    logger.save()

if __name__ == "__main__":
    main()
