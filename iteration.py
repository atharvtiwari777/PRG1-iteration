# ==============================================================================
# ACTIVITY 1: Basic For Loops with Range
# ==============================================================================

# Count up to a number
def count_up(n):
    for i in range(1, n + 1):
        print(i)

# Count backwards - MODIFY this function
def count_down():
    # TODO: Fix this to count from 5 down to 1
    for i in range(5, 0, -1):  # This counts up, not down!
        print(i)

# MAKE: Print multiples of a number
def print_multiples(number):
    # TODO: Print the first 5 multiples of 'number'
    # Example: print_multiples(3) should print 3, 6, 9, 12, 15
    for i in range(1, 6):
        print(number * i)
    pass

# ==============================================================================
# ACTIVITY 2: For Loops with Variables
# ==============================================================================

# Add up numbers from 1 to n
def add_up_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

# Multiply numbers - MODIFY this function
def multiply_up_to_n(n):
    product = 1
    for i in range(1, n + 1):
        # TODO: Fix this line to multiply instead of just assigning
        product *= i  # This doesn't multiply!
    return product

# MAKE: Add numbers counting backwards
def count_down_from(n):
    # TODO: Add up n + (n-1) + (n-2) + ... + 1
    # Example: count_down_from(4) should return 4+3+2+1 = 10
    total = 0
    for i in range(n, 0, -1):
        total += i
    return total

# ==============================================================================
# ACTIVITY 3: For Loops with Simple Conditions
# ==============================================================================

# Count even numbers up to n
def count_evens_up_to(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:  # % finds the remainder when dividing
            count = count + 1
    return count

# Count odd numbers - MODIFY this function
def count_odds_up_to(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:  # This condition is wrong for odd numbers!
            count = count + 1
    return count

# MAKE: Count numbers divisible by 5
def count_fives(n):
    # TODO: Count how many numbers from 1 to n are divisible by 5
    # Hint: Use % like in the even number example
    pass

# ==============================================================================
# ACTIVITY 4: Basic While Loops
# ==============================================================================

# Count down using while loop
def countdown_while(n):
    current = n
    while current > 0:
        print(current)
        current = current - 1

# Count up with while - MODIFY this function
def count_up_while(n):
    current = 1
    while current <= n:
        print(current)
        # TODO: Add the missing line to avoid infinite loop!
        pass

# MAKE: Add numbers until target reached
def add_until_target(target):
    # TODO: Keep adding 1, then 2, then 3, etc. until total >= target
    # Return how many numbers you added
    # Example: If target is 10, add 1+2+3+4 = 10, so return 4
    pass

# ==============================================================================
# ACTIVITY 5: Nested Loops (Simple Patterns)
# ==============================================================================

# Print a square of stars
def print_square(size):
    for row in range(size):
        for col in range(size):
            print("*", end="")
        print()  # New line after each row

# Print a rectangle - MODIFY this function
def print_rectangle(width, height):
    for row in range(height):
        for col in range(width):
            print("*", end="")
        print()  # This works but let's make sure you understand it

# MAKE: Print a right triangle
def print_right_triangle(height):
    # TODO: Print a triangle like this for height=4:
    # *
    # **
    # ***
    # ****
    pass

# ==============================================================================
# EXTENSION CHALLENGES
# ==============================================================================

# Challenge 1: Print multiples of 3 from 1 to 20
def print_multiples_of_three():
    # TODO: Use a loop to print 3, 6, 9, 12, 15, 18
    pass

# Challenge 2: Find first number whose square > 100
def find_first_square_over_100():
    # TODO: Use a while loop to find the answer
    # Test: 1*1=1, 2*2=4, 3*3=9, ... 10*10=100, 11*11=121
    pass

# Challenge 3: Print one times table
def print_times_table(number):
    # TODO: Print number x 1, number x 2, etc. up to number x 10
    # Example: print_times_table(7) prints "7 x 1 = 7", "7 x 2 = 14", etc.
    pass

# ==============================================================================
# TEST YOUR FUNCTIONS
# ==============================================================================

# if __name__ == "__main__":
#     print("Testing count_up(3):")
#     count_up(3)
    
#     print("\nTesting add_up_to_n(4):")
#     result = add_up_to_n(4)
#     print(f"Result: {result}")
    
#     print("\nTesting count_evens_up_to(6):")
#     result = count_evens_up_to(6)
#     print(f"Even numbers from 1 to 6: {result}")
    
#     print("\nTesting countdown_while(3):")
#     countdown_while(3)
    
#     print("\nTesting print_square(3):")
#     print_square(3)

print(count_down_from(4))