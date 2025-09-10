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

## Activity 1: Basic For Loops with Range

### Task: Simple Counting

* **PREDICT**: Look at the `count_up` function. What numbers do you think will be printed when you call `count_up(3)`? Write down your prediction.
* **RUN**: Run the code to see the actual output. Were your predictions correct?
* **INVESTIGATE**: Try `count_up(1)`, `count_up(5)`, and `count_up(0)`. What happens with each? How does `range()` work?
* **MODIFY**: Fix the `count_down` function so it counts backwards from 5 to 1.
* **MAKE**: Complete the `print_multiples` function to print the first 5 multiples of a given number.

---

## Activity 2: For Loops with Variables

### Task: Accumulating Values

* **PREDICT**: Look at the `add_up_to_n` function. What total do you think you'll get for `add_up_to_n(4)`? (Hint: 1+2+3+4 = ?)
* **RUN**: Run the code and check your prediction.
* **INVESTIGATE**: Try `add_up_to_n(1)`, `add_up_to_n(10)`, and `add_up_to_n(0)`. What patterns do you notice?
* **MODIFY**: Fix the `multiply_up_to_n` function so it calculates the product (multiplication) instead of always returning 1.
* **MAKE**: Complete the `count_down_from` function to add up numbers counting backwards (e.g., 5+4+3+2+1).

---

## Activity 3: For Loops with Simple Conditions

### Task: Counting Special Numbers

* **PREDICT**: Look at the `count_evens_up_to` function. How many even numbers are there from 1 to 6? Make your prediction.
* **RUN**: Test your prediction with `count_evens_up_to(6)`.
* **INVESTIGATE**: Try different numbers. What makes a number even? How does the `%` operator work?
* **MODIFY**: Fix the `count_odds_up_to` function to count odd numbers correctly.
* **MAKE**: Complete the `count_fives` function to count how many numbers from 1 to n are divisible by 5.

---

## Activity 4: Basic While Loops

### Task: Loops with Conditions

* **PREDICT**: Look at the `countdown_while` function. How is this different from the for loop version? What will `countdown_while(3)` print?
* **RUN**: Test your prediction and compare with the for loop version from Activity 1.
* **INVESTIGATE**: Try `countdown_while(1)` and `countdown_while(0)`. How does the while loop handle these?
* **MODIFY**: Fix the `count_up_while` function so it counts up from 1 to n instead of going forever.
* **MAKE**: Complete the `add_until_target` function that keeps adding numbers (1, then 2, then 3...) until the total reaches a target.

---

## Activity 5: Nested Loops (Simple Patterns)

### Task: Loops Inside Loops

* **PREDICT**: Look at the `print_square` function. What pattern will `print_square(3)` create? Draw it on paper first.
* **RUN**: Test your prediction. Does the output match what you drew?
* **INVESTIGATE**: Try `print_square(1)`, `print_square(2)`, and `print_square(4)`. How do the loops work together?
* **MODIFY**: Fix the `print_rectangle` function to create a rectangle of specified width and height.
* **MAKE**: Complete the `print_right_triangle` function to print a right-angled triangle pattern.

---

## Final Reflection

* **Pattern Recognition**: What are the key differences between `for` loops and `while` loops?
* **Range Function**: How does `range(start, stop)` work? What about `range(start, stop, step)`?
* **Loop Variables**: How do you use variables to accumulate totals or count things in loops?

---

## Extension Challenges

For those who finish early, try these:

* **Challenge 1**: Create a function that prints numbers from 1 to 20, but only the multiples of 3.
* **Challenge 2**: Write a function that uses a while loop to find the first number whose square is greater than 100.
* **Challenge 3**: Create a function that prints a multiplication table for any number (just that number's table, like 3x1=3, 3x2=6, etc.).