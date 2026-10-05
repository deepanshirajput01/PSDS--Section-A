# Explanation:
# For every number, calculate the sum of its digits.
# Numbers having the same digit sum form a special pair.

# If a digit sum has already appeared 'count' times,
# then the current number can form 'count' new pairs.
# Therefore, we add count to the answer.

# Example:
# Digit sum 6 appears for 51 and 42.
# When 42 is processed, 51 is already present,
# so it creates 1 new pair.

def digit_sum(num):
    num = abs(num)
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def solve():
    n = int(input("Enter number of elements: "))
    nums = list(map(int, input("Enter the array elements: ").split()))
    count = {}
    pairs = 0
    for num in nums:
        s = digit_sum(num)
        if s in count:
            pairs += count[s]
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    print("Number of special pairs =", pairs)
solve() 