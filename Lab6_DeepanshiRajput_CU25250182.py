''' 
# 1. 3Sum Problem (-3 , 1 , 2) : 5 6 -3 8 1 9 2

arr = [5, 6, -3, 8, 1, 9, 2]
target = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):

            if arr[i] + arr[j] + arr[k] == target:
                print("Combination of Numbers :", arr[i], arr[j], arr[k]) 
'''



'''
# 2. Fibonacci Series

n = 5
a = 1
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
'''



# 3. Tower of Hanoi

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    # Move the largest disk from source to destination
    print("Move disk", n, "from", source, "to", destination)
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)
n = 4
tower_of_hanoi(n, 'A', 'B', 'C')