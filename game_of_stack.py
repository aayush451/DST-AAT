def twoStacks(maxSum, a, b):
    sum_so_far = 0
    max_count = 0
    i = 0

    while i < len(a) and sum_so_far + a[i] <= maxSum:
        sum_so_far += a[i]
        i += 1
    max_count = i

    j = 0
    while j < len(b):
        sum_so_far += b[j]
        j += 1
        while sum_so_far > maxSum and i > 0:
            i -= 1
            sum_so_far -= a[i]
        if sum_so_far <= maxSum:
            max_count = max(max_count, i + j)

    return max_count

maxSum = 10
a = [4, 2, 4, 6, 1]
b = [2, 1, 8, 5]

result = twoStacks(maxSum, a, b)
print(result)
