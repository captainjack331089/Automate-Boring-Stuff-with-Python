## Function



***Sample***

```python
def hello():
		print('Howdy!')
		print('Howdy!!!') 
		print('Hello there.')

hello() 
hello() 
hello()

>>>
Howdy!
Howdy!!!
Hello there.

Howdy!
Howdy!!!
Hello there.

Howdy!
Howdy!!!
Hello there.
```



#### Def statements with Parameters

```python
def hello(name):
		print('Hello ' + name)

hello('Alice') 
hello('Bob')

>>>
Hello Alice
Hello Bob
```



#### Return Values and return Statements

```python
import random
def getAnswer(answerNumber): 
		if answerNumber == 1:
				return 'It is certain' 
		elif answerNumber == 2:
				return 'It is decidedly so' 
		elif answerNumber == 3:
				return 'Yes'
		elif answerNumber == 4:
				return 'Reply hazy try again' 
		elif answerNumber == 5:
				return 'Ask again later' 
		elif answerNumber == 6:
				return 'Concentrate and ask again' 
		elif answerNumber == 7:
				return 'My reply is no' 
		elif answerNumber == 8:
				return 'Outlook not so good' 
		elif answerNumber == 9:
				return 'Very doubtful'
r = random.randint(1, 9) 
fortune = getAnswer(r) 
print(fortune)
```



#### The None Value

Behind the scenes, python adds return None to the end of any function definition with no return statement.

```python
>>> spam = print('Hello!') 
Hello!
>>> None == spam
True
```



#### Keyword Arguments and print()

```python
print('Hello', end='') 
print('World')

HelloWorld

print('cats', 'dogs', 'mice', sep=',') 
cats,dogs,mice
```



#### Local and Global Scope

- Code in the global scope cannot use any local variables.
- However, a local scope can access global variables.
- Code in a function’s local scope cannot use variables in any other local scope.
- You can use the same name for different variables if they are in dif- ferent scopes. That is, there can be a local variable named spam and a global variable also named spam.



#### Exception Handling

```python
def span(dividedBy):
		try:
				return 42 / dividedBy
		except ZeroDivisionError:
				print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))

>>>
21.0
3.5
Error: Invalid argument.
```

