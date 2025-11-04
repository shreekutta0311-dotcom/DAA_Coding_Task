# 0/1 Knapsack Problem using Brute Force (Binary Representation)
# Example with 6 items

# Step 1: Define the items (weights and values)
weights = [2, 3, 4, 5, 9, 7]
values  = [3, 4, 8, 8, 10, 9]
capacity = 15  # Maximum weight the knapsack can hold

n = len(weights)

best_value = 0
best_combination = []

# Step 2: Loop through all possible combinations (0 to 2^n - 1)
for i in range(2 ** n):
    # Convert number to binary string of length n (e.g., 010101)
    combination = bin(i)[2:].zfill(n)
    
    total_weight = 0
    total_value = 0
    
    # Step 3: Evaluate this combination
    for j in range(n):
        if combination[j] == '1':  # item included
            total_weight += weights[j]
            total_value += values[j]
    
    # Step 4: Check if this is a valid and better solution
    if total_weight <= capacity and total_value > best_value:
        best_value = total_value
        best_combination = combination

# Step 5: Display results
print("Items:")
print("Index | Weight | Value")
for i in range(n):
    print(f"  {i+1}    |   {weights[i]}     |   {values[i]}")

print("\nBest Combination (binary):", best_combination)
print("Selected Items (1 = included):", [int(x) for x in best_combination])
print("Maximum Value:", best_value)

# To show which items are selected:
selected_items = [i+1 for i in range(n) if best_combination[i] == '1']
print("Items included in the sack:", selected_items)

