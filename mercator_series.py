#!/usr/bin/env python3

"""
Mercator series: https://en.wikipedia.org/wiki/Mercator_series
Interesting infinite product converging to 2: https://www.youtube.com/watch?v=lj65p3U3So8

To profile the script: python -m cProfile ./mercato_series.py
"""
import numpy as np

index = 1
result_sum = 0.0
result_prod = 1.0
iterations=10000

print("Iteration\tSum\t\t\tExp(Sum)\t\tProduct\t\t\tProduct-Exp(Sum)")
for k in range(1,iterations+1):
    result_prod *= np.exp(1.0/index - 1.0/(index+1))
    result_sum += 1.0/index - 1.0/(index+1)
    index += 2
    print (k, '', result_sum, np.exp(result_sum), result_prod, result_prod-np.exp(result_sum),sep='\t')

