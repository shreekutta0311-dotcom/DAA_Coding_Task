import random

def integer_to_binary_and_check_bit(number):
    """
    Converts an integer to binary, selects a random bit position,
    and checks if the bit at that position is '0' or '1'.
    """

    # --- 1. Convert Integer to Binary Equivalent (Manual) ---
    if number == 0:
        binary_string = "0"
    else:
        temp_num = abs(number)  # Work with the absolute value
        binary_digits = []

        # Use the modulus and division method
        while temp_num > 0:
            remainder = temp_num % 2
            binary_digits.append(str(remainder))
            temp_num //= 2

        # Binary is built in reverse order, so we reverse the list
        binary_string = "".join(binary_digits[::-1])

        # Handle negative numbers (optional, often skipped for simple binary tasks)
        if number < 0:
            # Note: True representation of negative numbers (2's complement) is complex,
            # for this simple task, we'll just prepend a sign, though typically not done for pure binary.
            # We will proceed with the positive representation for bit checking accuracy.
            pass
    
    print(f"Original Number: {number}")
    print(f"Binary Equivalent: {binary_string}")
    
    # --- 2. Take a Random Position ---
    binary_length = len(binary_string)
    
    # Randomly select an index (position) within the binary string
    # range is inclusive (0 to length - 1)
    random_index = random.randrange(0, binary_length)
    
    # Note: Indices are counted from the left (most significant bit is index 0)
    print(f"Random Position (Index): {random_index}")
    
    # --- 3. Check the Bit and Print True/False ---
    selected_bit = binary_string[random_index]
    
    is_one = selected_bit == '1'
    is_zero = selected_bit == '0'
    
    print(f"Bit at Position {random_index}: {selected_bit}")
    
    # The requirement is to check and print True/False accordingly.
    if is_one:
        # The bit is '1', which is True for the 'is_one' check.
        print(f"Is the bit '1'? --> {True}")
    elif is_zero:
        # The bit is '0', which is True for the 'is_zero' check.
        # We can structure the output to answer a specific question, e.g., "Is the bit '1'?"
        print(f"Is the bit '1'? --> {False}")
    else:
        # Should not happen if conversion is correct
        print(f"Invalid character found: {False}")

# --- Execution ---

# Example 1: Large number
input_val_1 = 205
print("\n--- Running Example 1 ---")
integer_to_binary_and_check_bit(input_val_1)
# Binary for 205 is 11001101 (length 8)

# Example 2: Small number
input_val_2 = 13
print("\n--- Running Example 2 ---")
integer_to_binary_and_check_bit(input_val_2)
# Binary for 13 is 1101 (length 4)

# Example 3: Zero
input_val_3 = 0
print("\n--- Running Example 3 ---")
integer_to_binary_and_check_bit(input_val_3)