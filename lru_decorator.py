from timeit import repeat
from functools import lru_cache

# Function deocrator lru_cache 'memorizes' functions calls
def factorial(n):
    return n * factorial(n-1) if n else 1



# @lru_cache
# def factorial(n):
#     return n * factorial(n-1) if n else 1





setup_code = "from __main__ import factorial"
stmt = "factorial(30)"
times = repeat(setup=setup_code, stmt=stmt, repeat=30, number=10)
print(f"Minimum execution time: {min(times)}")




