def solve():
    n = int(input("Enter N (size of array): "))
    A = list(map(int, input("Enter array elements: ").split()))
    if n == 1:
        print("Minimum operations:", abs(A[0]))
        return
    for x in A:
        if x != A[0]:
            print("Minimum operations: -1")
            return
    print("Minimum operations:", abs(A[0]))
T = int(input("Enter number of test cases: "))
for _ in range(T):
    solve()