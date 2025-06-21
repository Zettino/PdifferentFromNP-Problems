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
                if other * count == remainder:
                    return True
                if other * count > remainder:
                    break
    return False
testArray = [5,5,5,3,5]
res = subset_sum(testArray,9)
print(res)
