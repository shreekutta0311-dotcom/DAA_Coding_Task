def find_combinations(A, k, start_index, current_combination, result):
    """
    Recursive function to find combinations of size k.

    :param A: The full input list.
    :param k: The desired size of the combinations.
    :param start_index: The index in A to start selection from.
    :param current_combination: The combination built so far.
    :param result: The list to store all final combinations.
    """
    # Base Case 1: Combination is complete (size k reached)
    if len(current_combination) == k:
        # Store a copy of the current_combination
        result.append(list(current_combination))
        return

    # Base Case 2: We've run out of elements to select
    if start_index >= len(A):
        return

    # Recursive Step: Iterate through remaining elements
    for i in range(start_index, len(A)):
        # 1. Choose: Include the element A[i]
        current_combination.append(A[i])

        # 2. Recurse: Move to the next index (i + 1) to find the remaining elements
        # i + 1 ensures we don't pick the same element again (no duplicates)
        # and ensures the combination elements are in order.
        find_combinations(A, k, i + 1, current_combination, result)

        # 3. Unchoose (Backtrack): Remove A[i] to explore combinations without it
        current_combination.pop()


def get_combinations(A, k):
    """
    Wrapper function to initialize the combinations process.
    """
    if k < 0 or k > len(A):
        return []

    result = []
    current_combination = []
    # Start the recursive process from the beginning of the list (index 0)
    find_combinations(A, k, 0, current_combination, result)
    return result

# --- Example Usage for Combinations ---
print("\n--- Combinations (Backtracking) ---")
data = ['x', 7, 'y', 10]
k_size = 2
combos = get_combinations(data, k_size)
print(f"Combinations of size {k_size} for {data}:")
print(combos)