## Flow Control



**Boolean Values**

	- True
	- False



**Comparison Operators**

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | equal                    |
| !=       | Not equal                |
| <        | less than                |
| >        | greater than             |
| <=       | less than or equal to    |
| >=       | greater than or equal to |



**Boolean Operators**

| Expression      | Evaluates to.. |
| --------------- | -------------- |
| True and True   | True           |
| True and False  | False          |
| False and True  | False          |
| False and False | False          |
| True or True    | True           |
| True or False   | True           |
| False or True   | True           |
| False or False  | False          |
| not True        | False          |
| not False       | True           |



**Mixing Boolean and Comparison Operators**

...



---



#### Elements of Flow Control

- Conditions
- Blocks of Code



**Flow Control Statements**

- if statements

  ```python
  if name == 'Alice': print('Hi, Alice.')
      pass
  ```

- else statements

  ```python
  else:
  	print('Hello, stranger.')
  ```

- elif statements

  ```python
  if name == 'Alice': 
      print('Hi, Alice.')
  elif age < 12:
  	  print('You are not Alice, kiddo.')
  ```

  

- while Loop Statements

  ```python
  spam = 0
  while spam < 5:
  		print('Hello, world.') 
      spam = spam + 1
  ```

  

- break Statements

  ```python
  while True:
  		print('Please type your name.')
  		name = input()
  		if name == 'your name':
      		break 
  print('Thank you!')
  ```

  

- continue statements

  ```python
  while True:
  		print('Who are you?') name = input()
  		if name != 'Joe':
  				continue
  		print('Hello, Joe. What is the password? (It is a fish.)') 
      password = input()
  		if password == 'swordfish':
  				break 
  print('Access granted.')
  ```

  

- for loops and range() Function

  ```python
  print('My name is') 
  for i in range(5):
  		print('Jimmy Five Times (' + str(i) + ')')
  ```

  

- The starting, stopping, and stepping arguments to range()

  ```python
  for i in range(12, 16):
      print(i)
      
  >>>12
  >>>13
  >>>14
  >>>15
  ```

  

  ```python
  for i in range(0, 10, 2):
      print(i)
      
  0
  2
  4
  6
  8
  
  ```

  

  ```python
  for i in range(5, -1, -1): print(i)
  
  5
  4
  3
  2
  1
  0
  
  ```

---

#### Importing Modules

```python
import random
for i in range(5):
		print(random.randint(1, 10))
    
4
1
8
2
2
5
```



**Ending a program early with sys.exit()**

```python
import sys
while True:
		print('Type exit to exit.') response = input()
		if response == 'exit':
				sys.exit()
		print('You typed ' + response + '.')
```

