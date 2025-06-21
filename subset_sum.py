"""
per favore. testate e dimmi se su dati differenti risponde in modo giusto
please test and tell me if it responds correctly on different data 
"""
from collections import Counter

def subset_sum(numbers, target):
    counts = Counter(numbers)
    unique_values = sorted(counts.keys(), reverse=True)

    for value in unique_values:
        max_count = counts[value]
        max_possible = target // value
        usable_count = min(max_count, max_possible)
        subtotal = value * usable_count
        remainder = target - subtotal

        if remainder == 0:
            return True

        for other in unique_values:
            if other == value:
                continue            
            for count in range(1, counts[other] + 1):
                if other * count <= remainder:
                    remainder -= other*count
                if remainder ==0:
                    return True
                if other * count > remainder:
                    break
    return False
res1 =subset_sum([2, 5, 9, 10], 17)  # 2 + 5 + 10 = 17
res2 = subset_sum([1, 3, 4, 5], 7)  # 3 + 4 = 7
res3 = subset_sum([1, 2, 5], 8)  # 1 + 2 + 5 = 8
res4 = subset_sum([1, 1, 1, 1, 1, 1, 1, 1, 1], 9)  # 9 volte 1
testArray = [2,2,8,10]
res = subset_sum(testArray,17)
print(res, res1, res2, res3, res4)
