'''import heapq

# ---------------- MIN HEAP ----------------

arr = [20, 31, 11, 1, 6]

min_heap = []

for x in arr:
    heapq.heappush(min_heap, x)

print("Min Heap :", min_heap)

print("Priority Queue (Min) :")
while min_heap:
    print(heapq.heappop(min_heap), end=" ")


# ---------------- MAX HEAP ----------------

max_heap = []

for x in arr:
    heapq.heappush(max_heap, -x)

print("\n\nMax Heap :", [-x for x in max_heap])

print("Priority Queue (Max) :")
while max_heap:
    print(-heapq.heappop(max_heap), end=" ")


# ---------------- HEAP SORT ----------------

def heap_sort(arr):
    heap = []

    for x in arr:
        heapq.heappush(heap, x)

    sorted_arr = []

    while heap:
        sorted_arr.append(heapq.heappop(heap))

    return sorted_arr


arr = [22, 11, 27, 1, 31, 17]

print("\n\nOriginal Array :", arr)
print("Heap Sort :", heap_sort(arr))'''





'''def max_adjacent_difference(arr):
    arr.sort()
    n = len(arr)

    if n <= 1:
        return arr, 0

    # First arrangement
    a = []
    left = 0
    right = n - 1

    while left <= right:
        if left == right:
            a.append(arr[left])
        else:
            a.append(arr[left])
            a.append(arr[right])

        left += 1
        right -= 1

    sum1 = 0
    for i in range(1, n):
        sum1 += abs(a[i] - a[i - 1])

    # Second arrangement
    b = []
    left = 0
    right = n - 1

    while left <= right:
        if left == right:
            b.append(arr[left])
        else:
            b.append(arr[right])
            b.append(arr[left])

        left += 1
        right -= 1

    sum2 = 0
    for i in range(1, n):
        sum2 += abs(b[i] - b[i - 1])

    if sum1 >= sum2:
        return a, sum1
    else:
        return b, sum2


# Input
arr = [20, 31, 17, 11]

result, total = max_adjacent_difference(arr)

print("Rearranged Array:", result)
print("Maximum Sum:", total)'''




def smallest_subarray(arr, target):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > target:
            length = right - left + 1
            min_length = min(min_length, length)

            current_sum -= arr[left]
            left += 1

    if min_length == float('inf'):
        return -1

    return min_length


# Input
arr = [1, 4, 4, 2, 5, 1]
target = 8

answer = smallest_subarray(arr, target)

print("Array :", arr)
print("Target :", target)
print("Smallest Subarray Length :", answer)