1. It is said that a recursive algorithm has more overhead than an iterative algorithm. 
What does this mean?

A recursive algorithm requires multiple method calls. Each method call 
requires several actions to be performed by the JVM. These actions include 
allocating memory for parameters and local variables and storing the address 
of the program location where control returns after the method terminates. 
All these actions are known as overhead. In an iterative algorithm, which 
uses a loop, such overhead is unnecessary.

2. What is a base case?
initial conditio that stop the recursive call
3. What is a recursive case?
condition under wich recursive occurs
4. What causes a recursive algorithm to stop calling itself?
base case
5. What is direct recursion? What is indirect recursion?
function that directly called him self is direct
indirect , This occurs when function A calls function B, which in turn 
calls function A. 