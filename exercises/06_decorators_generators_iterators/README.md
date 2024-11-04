## 1. Python Decorator: Logging Function Calls

### Overview
In this exercise, you will learn how to create a Python decorator that logs function calls. This decorator will print the name of the function being called, its arguments, and optionally include the execution time in UTC. This technique is invaluable for debugging and understanding the flow of your program.

### Steps to Create the Logger Decorator

#### Step 1: Define the Decorator
Create a function named logger_decorator that accepts a boolean argument, print_time, which determines whether to log the execution time. Inside this function, define an inner function (the decorator) that takes the function to be decorated as an argument. Within this inner function, define a wrapper function that constructs a log message displaying the function's name and its arguments. If print_time is True, include the execution time in the log message.

#### Step 2: Try on different functions
Aside from the given add_numbers() function, try this on different other functions as well


## 2. Python Iterators & Iterables

### Step 1: Implement your own iterable class that represents an insurance portfolio.

Task:

1. Given is a class named `InsurancePortfolioIterable` that holds a collection of insurance policies (as a list).
2. Each policy is represented as a dictionary with keys such as `policy_id`, `policy_holder`, and `premium`.
3. Implement the `__iter__()` method to allow iteration over the policies in the portfolio.
4. Instantiate the InsurancePortfolio class, add some insurance policies, and iterate through them to print the details of each policy.

### Step 2: Implementing an Iterator (Claims Log)

Task:

1. Given is a class named `ClaimsLogIterator` that takes a list of claims as input. Each claim is represented as a dictionary with keys such as `claim_id`, `policy_id`, and `amount`.
2. Implement the `__iter__()` method to initialize the iterator.
3. Implement the `__next__()` method to return the next claim from the log. If there are no more claims, it should raise a StopIteration exception. Don't forget to utilize index as its internal state.
4. Instantiate the `ClaimsLogIterator` class and iterate through it to print the details of each claim.


### Step 3: Try different itertools

Task:
1. Familiarize yourself with itertools, ideally by writing some example codes: `count()`, `cycle()`, `repeat()`, `combinations()`, `permutations()`, `product()`, `chain()`
2. Also perform the same for these special iterables: `enumerate()` and `zip()`

## 3. Python Generator

#### Step 1: Understand the keyword `yield`
Write a generator function named countdown(n) that counts down from n to 0, yielding each number. Test your generator by iterating through its values and printing them.

#### Step 2: Consuming the Generator with `next()`
Create a generator to print the value yielded each time `next()` is called. Use a try block to catch the StopIteration exception when the generator is exhausted.

#### Step 3: Discarding a Generator with `close()`
Write a generator function called simple_gen() that yields the first three numbers (0, 1, 2). Consume the generator using next(), then close the generator and attempt to call next() again. Handle the exception appropriately.

#### Step 4: List Comprehension vs. Generator Comprehension

List Comprehension:

Create a list comprehension that generates the squares of numbers from 0 to 9.
Print the values yielded by the list comprehension, demonstrating that the list can be reused.

Generator Comprehension:

Similarly, create a generator comprehension that generates the squares of numbers from 0 to 9.
Also print the values yielded by the generator comprehension, attempt to reuse the generator and observe the resulting behavior.
