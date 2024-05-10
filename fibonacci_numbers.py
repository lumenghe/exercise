"""
The Fibonacci Series

The Fibonacci sequence begins with
and

. These are the first and second terms, respectively. After this, every element is the sum of the preceding elements:

Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)  

Task
Given the starter code, complete the Fibonacci function to return the

term.

We start counting from Fibonacci
. This might differ from some other notations that treats Fibonacci

.

The overall equation is:

             = 0 , n = 1
Fibonacci(n) = 1 , n = 2
               Fibonacci(n-1) + Fibonacci(n-2)  , n > 2

Input Format

One line of input, the integer

.

Constraints

Output Format

Output one integer, the

Fibonacci number.

Sample Input

3  

Sample Output

1  

Function Prototype
The starter code is provided for Scala. The code for accepting the input and displaying the output is provided. You will be provided the input parameter
, and you need to return the

Fibonacci term.

Sample Input and Output Values for the Fibonacci Series

fibonacci(3) = (0+1) = 1  
fibonacci(4) = (1+1) = 2  
fibonacci(5) = (1+2) = 3  

Requirements
Simple test cases can be cleared with a purely recursive function exponentially. To clear the more challenging test cases without violating the principles of functional programming, you might benefit from learning about the accumulator technique.
"""


def fibonacci(n):
    """0, 1, 1, 2, 3, 5, 8"""
    if n == 1:
        return 0
    if n == 2:
        return 1
    a = 0
    b = 1
    for index in range(1, n):
        tmp = b
        b += a
        a = tmp

    return a


if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
