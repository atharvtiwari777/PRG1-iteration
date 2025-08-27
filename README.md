# Learning Loops with PRIMM

## Why PRIMM Matters

This session uses the **PRIMM methodology** to help you learn programming loops effectively. PRIMM stands for:

- **PREDICT**: Before running code, think about what it will do. This builds your mental model.
- **RUN**: Execute the code to see if your predictions were correct.
- **INVESTIGATE**: Experiment with different inputs to understand how the code behaves.
- **MODIFY**: Make small changes to existing code to fix problems or add features.
- **MAKE**: Create new code from scratch using what you've learnt.

**Follow each step in order** - don't skip ahead! Each stage builds your understanding and confidence with loops.

---

## Activity 1: Simple Counting Loops

### Task: Count Up and Down

* **PREDICT**: Look at the `count_to_number` function. What do you think the output will be for `count_to_number(5)`? Write down your prediction.
* **RUN**: Run the code to see the actual output. Were your predictions correct?
* **INVESTIGATE**: Examine what happens when you use different inputs. Try `count_to_number(0)`, `count_to_number(1)`, and `count_to_number(3)`. How does the `range()` function handle these inputs?
* **MODIFY**: Find the `count_down_from_number` function. The current code doesn't count down properly. Change the `range()` parameters so the function counts down from a given number `n` to 1.
* **MAKE**: Complete the `times_table(number, up_to)` function. This function should use a `for` loop to generate a list containing a times table for a given `number` up to a specified `up_to` value. For example, `times_table(3, 4)` should return `[3, 6, 9, 12]`.

---
## Activity 2: Working with Lists

### Task: Process Lists of Numbers

* **PREDICT**: Look at the `sum_numbers` function. What do you think the output will be for `sum_numbers([1, 2, 3, 4])`? Write down your prediction.
* **RUN**: Run the code to see the actual output. Were your predictions correct?
* **INVESTIGATE**: Test the `sum_numbers` function with different inputs. Try `sum_numbers([])`, `sum_numbers([5])`, and `sum_numbers([1, -2, 3])`. How does the function handle these cases?
* **MODIFY**: Find the `find_largest` function. There's a problem with how it initialises the `largest` variable. Fix it so it works correctly with negative numbers too.
* **MAKE**: Complete the `count_evens` function. This function should count how many even numbers are in a list. For example, `count_evens([1, 2, 3, 4, 5])` should return `2`.

---
## Activity 3: Simple String Processing

### Task: Work with Text and Characters

* **PREDICT**: Look at the `count_vowels` function. What do you think the output will be for `count_vowels("hello")`? Write down your prediction.
* **RUN**: Run the code to see the actual output. Were your predictions correct?
* **INVESTIGATE**: Test the `count_vowels` function with different inputs. Try `count_vowels("HELLO")`, `count_vowels("xyz")`, and `count_vowels("")`. How does the function handle these cases?
* **MODIFY**: Find the `reverse_string` function. The current code doesn't reverse the string properly. Fix the loop so it builds the reversed string correctly.
* **MAKE**: Complete the `count_words` function. This function should count how many words are in a sentence. For example, `count_words("Hello world")` should return `2`.

---
## Activity 4: Basic Nested Loops

### Task: Loops Inside Loops

* **PREDICT**: Look at the `multiplication_table` function. What do you think the output will be for `multiplication_table(3)`? Write down your prediction.
* **RUN**: Run the code to see the actual output. Were your predictions correct?
* **INVESTIGATE**: Test the `multiplication_table` function with different inputs. Try `multiplication_table(1)` and `multiplication_table(5)`. How does the nested loop create the table?
* **MODIFY**: Find the `find_pairs_that_sum` function. The current code finds duplicate pairs (like both (1,4) and (4,1)). Fix the inner loop range so it only finds unique pairs.
* **MAKE**: Complete the `print_triangle` function. This function should print a triangle pattern of stars. For example, `print_triangle(3)` should print:
```
*
**
***
```

---
## Activity 5: Basic While Loops

### Task: Condition-Based Loops

* **PREDICT**: Look at the `countdown_while` function. How is this different from using a for loop? What do you think the output will be for `countdown_while(3)`?
* **RUN**: Run the code to see the actual output. Compare this with the for loop version from Activity 1.
* **INVESTIGATE**: Test the `countdown_while` function with different inputs. Try `countdown_while(0)` and `countdown_while(1)`. How does the while loop handle these cases?
* **MODIFY**: Find the `get_positive_number` function. There's a problem with the while condition that will cause issues. Fix it so it properly keeps asking until a positive number is entered.
* **MAKE**: Complete the `simple_guessing_game(target)` function. This should keep asking the user for guesses until they get the target number correct, and return how many attempts it took.

---
## Final Reflection

* **Pattern Recognition**: Reflect on the activities and identify common looping patterns you've used: **counting** (using range), **accumulation** (building a total), **searching** (finding items), and **processing** (working through lists or strings).
* **When to Use What**: Think about when you'd use simple loops versus nested loops, and how the `range()` function can be used in different ways.

---
## Extension Challenges

For those who finish early, try these additional challenges:

* **Challenge 1**: The `find_longest_word` function is already complete. Test it and understand how it works.
* **Challenge 2**: Complete the `calculate_average` function to find the average of numbers in a list.
* **Challenge 3**: Complete the `remove_duplicates` function to create a new list with no repeated items.