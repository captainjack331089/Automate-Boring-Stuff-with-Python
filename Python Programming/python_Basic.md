## Basic of Python

- Expressions 

  | Operator | Operation                         | Example  | Evaluates to.. |
  | -------- | --------------------------------- | -------- | -------------- |
  | **       | Exponent                          | 2  **  3 | 8              |
  | %        | Modulus/remainder                 | 22 % 8   | 6              |
  | //       | Integer division/floored quotient | 22 // 8  | 2              |
  | /        | Division                          | 22 / 8   | 2.75           |
  | *        | Multiplication                    | 3 * 5    | 15             |
  | -        | Subtraction                       | 5 - 2    | 3              |
  | +        | Addition                          | 2 + 2    | 4              |

  

The order of operations of python math operators is similar to that of maths.

- Data Types

  - Integer
    - eg. -2, -1, 0, 1, 2, 3
  - Floating-point
    - eg. -1.25, 0.0, 0.5, 4.4
  - String
    - eg. 'a', 'aa', 'Hello1!', 'df 1cat'

- String Cancatenation and Replication

  ```python
  'Alice' + 'Bob'
  >>> 'AliceBob'
  'Alice' * 5
  >>> 'AliceAliceAliceAliceAlice'
  ```

- Storing Values in variables

  ```python
  spam = 'hello'
  span = 'goodbye'
  ```

  

## Program

```python
# THis program syas hello and asks for my name	
print('Hello,world!')
print('What is your name?') # ask for name
```



***The input() Function***

```python
 myName = input()
```



***The len() Function***

```python
myName = 'Jack'
print('The length of your name is: ')
print(len(myName))

>>>The length of your name is:
>>>4
```



***The str(), int(), float() Functions***

```
str(0) --> '0'
str(-3.14) --> '-3.14'
int('42') --> 42
int('1.25') --> 1
float('3.14') --> 3.14
float(310) --> 310.0
```

