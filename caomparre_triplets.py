
def compareTriplets(a, b):
    # Write your code here
    score = [0, 0]
    for x, n in zip(a, b):
        if x > n:
            score[0] += 1
        elif x < n:
            score[1] += 1
    return score


alice = [17, 28, 30]
bob = [99, 16, 8]
print(compareTriplets(alice, bob))
