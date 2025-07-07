import random
import time
from functools import lru_cache

# ------------------------
# Búsqueda exhaustiva recursiva
# ------------------------
def isExhRecSubsetSum(set, element, sum):
    if sum == 0:
        return True
    if element == 0:
        return False
    if set[element - 1] > sum:
        return isExhRecSubsetSum(set, element - 1, sum)
    return (isExhRecSubsetSum(set, element - 1, sum) or 
            isExhRecSubsetSum(set, element - 1, sum - set[element - 1]))

def exhRecSubsetSum(set, element, sum):
    return isExhRecSubsetSum(set, element, sum)

# ------------------------
# Subset sum con programación dinámica (top-down)
# ------------------------
def subset_sum_dynamic_topdown(items, capacity):
    span = len(items)

    @lru_cache(maxsize=None)
    def dynamic_topdown(index, remaining):
        if index == span or remaining == 0:
            return 0
        skip_current = dynamic_topdown(index + 1, remaining)
        use_current = 0
        if items[index] <= remaining:
            use_current = items[index] + dynamic_topdown(index + 1, remaining - items[index])
        return max(use_current, skip_current)
    
    iteration_result = dynamic_topdown(0, capacity)
    dynamic_topdown.cache_clear()
    return iteration_result

# ------------------------
# Experimentos comparativos
# ------------------------
random.seed(777)
complexity = 300
items = [random.randint(1, 100) for _ in range(complexity)]
capacity = 100

subitems = []
for j in range(1, complexity + 1):
    subitems.append(items[j - 1])
    # Búsqueda Exhaustiva Recursiva
    start_time = time.perf_counter()
    found = exhRecSubsetSum(subitems, len(subitems), capacity)
    end_time = time.perf_counter()
    print(f"Exhaustivo Recursivo -> {'Encontrado' if found else 'No encontrado'}, Tiempo: {end_time - start_time:.6f} s")

    # Programación Dinámica Top-Down
    start_time = time.perf_counter()
    dp_result = subset_sum_dynamic_topdown(tuple(subitems), capacity)  # Convertir a tupla para lru_cache
    end_time = time.perf_counter()
    print(f"DP Top-Down -> Mejor suma posible: {dp_result}, Tiempo: {end_time - start_time:.6f} s")
