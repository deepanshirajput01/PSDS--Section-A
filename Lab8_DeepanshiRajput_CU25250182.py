'''
#1. Easy — Array Manipulation 
#Given an array of N integers, find the maximum sum of any contiguous subarray of size K. 

# Explanation:
# We first calculate the sum of the first K elements.
# Then we slide the window one position at a time.
# We add the new element and remove the element that leaves the window.
# This avoids calculating every window sum from scratch.

n = int(input("Enter number of elements (N): "))
k = int(input("Enter window size (K): "))
arr = list(map(int, input(f"Enter {n} array elements: ").split()))
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, n):
    window_sum += arr[i]
    window_sum -= arr[i - k]
    if window_sum > max_sum:
        max_sum = window_sum
print(f"Maximum sum of subarray of size {k} = {max_sum}")
'''




'''
#2. Medium — String/Hashing 
#Given a string S, find the length of the longest substring without repeating characters. 

# Explanation:
# We maintain a sliding window containing unique characters.
# 'left' represents the starting position of the window.
# 'right' moves through the string.
# If a character is repeated inside the current window,
# we move 'left' after its previous position.
# A dictionary stores the last position of each character.

s = input("Enter a lowercase string: ")
last_position = {}
left = 0
max_length = 0
for right in range(len(s)):
    if s[right] in last_position and last_position[s[right]] >= left:
        left = last_position[s[right]] + 1
    last_position[s[right]] = right
    current_length = right - left + 1
    if current_length > max_length:
        max_length = current_length
print("Length of longest substring without repeating characters =", max_length)
'''







#3. Hard — Graphs 
#You are given a weighted, undirected graph with N nodes and M edges.
#Find the shortest path from node 1 to node N such that the path uses at most K edges. If no such path exists, output -1. 

# Explanation:
# We use Dynamic Programming.
# dp[e][v] = minimum cost to reach node v using at most e edges.
# We start from node 1 with cost 0.
# For every allowed number of edges, we check every graph edge.
# Since the graph is undirected, we can travel in both directions.
# Finally, dp[K][N] gives the minimum cost to reach node N
# using at most K edges.

n = int(input("Enter number of nodes (N): "))
m = int(input("Enter number of edges (M): "))
k = int(input("Enter maximum number of edges allowed (K): "))
edges = []
print("Enter each edge as: source destination weight")
for i in range(m):
    u, v, w = map(int, input(f"Edge {i + 1}: ").split())
    edges.append((u, v, w))
INF = float('inf')
# dp[v] = minimum cost to reach v
# using at most the current number of edges
dp = [INF] * (n + 1)
dp[1] = 0
for e in range(k):
    new_dp = dp.copy()
    for u, v, w in edges:
        if dp[u] != INF:
            new_dp[v] = min(new_dp[v], dp[u] + w)
        if dp[v] != INF:
            new_dp[u] = min(new_dp[u], dp[v] + w)
    dp = new_dp
if dp[n] == INF:
    print("Shortest path = -1")
else:
    print("Minimum path weight =", dp[n])
