# Travelling Salesman Problem (TSP) using Brute Force
# Example with 5 cities

from itertools import permutations
import math

# Step 1: Define city coordinates
cities = {
    0: (0, 0),
    1: (1.2, 3.4),
    2: (4.5, 2.2),
    3: (3.0, -1.0),
    4: (-0.5, 2.0)
}

# Step 2: Function to compute Euclidean distance
def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Step 3: Create a distance matrix
n = len(cities)
dist = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dist[i][j] = round(distance(cities[i], cities[j]), 2)

# Step 4: Brute-force search for all possible tours
start_city = 0
other_cities = [c for c in range(n) if c != start_city]

best_tour = None
best_distance = float('inf')

for perm in permutations(other_cities):
    tour = [start_city] + list(perm) + [start_city]  # return to start
    total = 0
    for i in range(len(tour) - 1):
        total += dist[tour[i]][tour[i + 1]]

    if total < best_distance:
        best_distance = total
        best_tour = tour

# Step 5: Display the result
print("Distance Matrix:")
for row in dist:
    print(row)

print("\nBest Tour:", best_tour)
print("Minimum Distance:", round(best_distance, 2))
