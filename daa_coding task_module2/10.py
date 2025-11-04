# Implement Karatusba Algorithm for multiplication of 2 long integers

def karatsuba(x, y):
    # Convert to integers if input is string
    x, y = int(x), int(y)
    
    # Base case: if numbers are small, multiply directly
    if x < 10 or y < 10:
        return x * y

    # Calculate the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2  # Split position

    # Split x and y into two halves
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)

    # 3 recursive multiplications
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)

    # Combine results using Karatsuba formula
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0


# result
 
x = int(input("Enter first long integer: "))
y = int(input("Enter second long integer: "))

product = karatsuba(x, y)
print(f"\nKaratsuba Multiplication Result:\n{x} × {y} = {product}")
