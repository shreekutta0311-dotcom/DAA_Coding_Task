def generate_permutations(A, n):
    """
    Generates all permutations of list A using the recursive Heap's algorithm.

    :param A: The list of elements to permute (can be any data type).
    :param n: The size of the current prefix to permute (starts as len(A)).
    """
    # Base Case: When n = 1, we have a complete permutation
    if n == 1:
        # Since A is modified in place, we print/store a copy
        print(A)
        return

    # Recursive Step: Generate permutations for the prefix of size n-1
    for i in range(n):
        generate_permutations(A, n - 1)

        # Determine the swap based on the parity of n (k in pseudocode)
        if n % 2 == 0:
            # If n is even, swap the i-th element with the last element (n-1)
            A[i], A[n - 1] = A[n - 1], A[i]
        else:
            # If n is odd, swap the first element (0) with the last element (n-1)
            A[0], A[n - 1] = A[n - 1], A[0]

# --- Example Usage for Permutations ---
print("--- Permutations (Heap's Algorithm) ---")
data = [1, 'a', 3]
# Note: We pass a mutable copy to allow in-place swaps
# The list is printed within the recursive function
generate_permutations(data, len(data))