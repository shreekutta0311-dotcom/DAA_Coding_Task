import math

# Function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# A brute force function for small subproblems (<=3 points)
def brute_force(points):
    min_dist = float('inf')
    pair = (None, None)
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return min_dist, pair

# Find the smallest distance in the strip area
def strip_closest(strip, d_min):
    min_dist = d_min
    pair = (None, None)
    n = len(strip)
    
    # Compare each point with next 6 points (as per theory)
    for i in range(n):
        for j in range(i + 1, min(i + 7, n)):
            d = distance(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
                pair = (strip[i], strip[j])
    return min_dist, pair

# Recursive divide and conquer function
def closest_pair_rec(points_sorted_x, points_sorted_y):
    n = len(points_sorted_x)
    
    # Base case: use brute force if small
    if n <= 3:
        return brute_force(points_sorted_x)
    
    mid = n // 2
    midpoint = points_sorted_x[mid]
    
    # Divide into left and right halves
    left_x = points_sorted_x[:mid]
    right_x = points_sorted_x[mid:]
    
    midpoint_x = midpoint[0]
    left_y = [p for p in points_sorted_y if p[0] <= midpoint_x]
    right_y = [p for p in points_sorted_y if p[0] > midpoint_x]
    
    # Recursively find smallest distances in left and right halves
    d_left, pair_left = closest_pair_rec(left_x, left_y)
    d_right, pair_right = closest_pair_rec(right_x, right_y)
    
    # Choose the smaller of the two distances
    if d_left < d_right:
        d_min = d_left
        min_pair = pair_left
    else:
        d_min = d_right
        min_pair = pair_right
    
    # Build a strip around the dividing line
    strip = [p for p in points_sorted_y if abs(p[0] - midpoint_x) < d_min]
    
    d_strip, pair_strip = strip_closest(strip, d_min)
    
    if d_strip < d_min:
        return d_strip, pair_strip
    else:
        return d_min, min_pair

# Main function
def closest_pair(points):
    points_sorted_x = sorted(points, key=lambda x: x[0])
    points_sorted_y = sorted(points, key=lambda x: x[1])
    return closest_pair_rec(points_sorted_x, points_sorted_y)

# Example points
points = [(2.1, 3.2), (12.0, 30.5), (40.1, 50.0), (5.0, 1.0),
          (12.5, 10.2), (3.0, 4.0), (7.2, 2.8)]

# Run the algorithm
min_distance, closest_points = closest_pair(points)

# Output results
print("Points:", points)
print("\nClosest Pair:", closest_points)
print("Minimum Distance:", round(min_distance, 4))
