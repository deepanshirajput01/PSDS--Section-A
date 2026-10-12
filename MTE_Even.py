t = int(input())
for _ in range(t):
    n, x = input().split()
    n = int(n)
    x = int(x)
    a = [int(i) for i in input().split()]

    for i in range(n):
        for j in range(i + 1, n):
            d1 = bin(a[i] ^ x).count('1')
            d2 = bin(a[j] ^ x).count('1')

            if d1 > d2 or (d1 == d2 and a[i] > a[j]):
                a[i], a[j] = a[j], a[i]
    print(*a)
