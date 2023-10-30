from itertools import combinations

def find_subset(numbers, target):
    for r in range(1, len(numbers) + 1):
        for subset in combinations(numbers, r):
            if sum(subset) == target:
                return subset
    return None

# Replace these values with the output from knapsack.py
choices = [19728964, 30673077, 137289540, 195938621, 207242611, 237735979, 298141799, 302597011, 387047012, 405520686, 424852916, 461998372, 463977415, 528505766, 557896298, 603269308, 613528675, 621228168, 654758801, 670668388, 741571487, 753993381, 763314787, 770263388, 806543382, 864409584, 875042623, 875651556, 918697500, 946831967]
target = 7627676296

winners = find_subset(choices, target)
flag = "UDCTF{%s}" % ("_".join(map(str,sorted(winners))))
print(flag)
