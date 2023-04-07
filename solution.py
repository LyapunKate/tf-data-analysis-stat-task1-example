import pandas as pd
import numpy as np


chat_id = 532569024 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    import math
    n = len(x)
    new_x = x - 887
    sum = 0
    for i in range(n):
      sum += math.log(new_x[i])
    a = sum/n
    return a
