# ==============================================================================
# ACTIVITY 1: Simple Counting Loops
# ==============================================================================

# Basic counting function
def count_to_number(n):
    result = []
    for i in range(1, n + 1):
        result.append(i)
    return result

# Count backwards - MODIFY this function
def count_down_from_number(n):
    result = []
    # TODO: Change the range parameters to count down
    for i in range(1, n + 1):  # This needs fixing!
        result.append(i)
    return result

# MAKE: Create a times table function
def times_table(number, up_to):
    # TODO: Complete this function
    pass

# ==============================================================================
# ACTIVITY 2: Working with Lists
# ==============================================================================

# Sum all numbers in a list
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Find the largest number - MODIFY this function
def find_largest(numbers):
    if not numbers:
        return None
    largest = 0  # This might not work for all cases!
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# MAKE: Count how many even numbers are in a list
def count_evens(numbers):
    # TODO: Complete this function
    pass

# ==============================================================================
# ACTIVITY 3: Simple String Processing
# ==============================================================================

# Count vowels in a word
def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count

# Reverse a string - MODIFY this function
def reverse_string(text):
    result = ""
    # TODO: Use a loop to build the reversed string
    for char in text:
        result = result + char  # This won't reverse!
    return result

# MAKE: Count words in a sentence
def count_words(sentence):
    # TODO: Complete this function
    pass

# ==============================================================================
# ACTIVITY 4: Basic Nested Loops
# ==============================================================================

# Create a simple multiplication table
def multiplication_table(size):
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            row.append(i * j)
        print(row)

# Find pairs that add to target - MODIFY this function
def find_pairs_that_sum(numbers, target):
    pairs = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):  # This will find duplicates!
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs

# MAKE: Create a pattern printer
def print_triangle(height):
    # TODO: Complete this function to print a triangle of stars
    pass

# ==============================================================================
# ACTIVITY 5: Basic While Loops
# ==============================================================================

# Count down using while loop
def countdown_while(start):
    current = start
    result = []
    while current > 0:
        result.append(current)
        current -= 1
    return result

# Keep asking for input until valid - MODIFY this function
def get_positive_number():
    number = -1
    while number <= 0:  # This condition needs fixing!
        number = int(input("Enter a positive number: "))
    return number

# MAKE: Create a guessing game function
def simple_guessing_game(target):
    # TODO: Complete this function
    # Keep asking for guesses until correct
    # Return the number of attempts
    pass

# ==============================================================================
# EXTENSION CHALLENGES
# ==============================================================================

# Challenge 1: Find the longest word
def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Challenge 2: Calculate average of a list
def calculate_average(numbers):
    # TODO: Complete this function
    pass

# Challenge 3: Remove duplicates from a list
def remove_duplicates(items):
    # TODO: Complete this function
    pass