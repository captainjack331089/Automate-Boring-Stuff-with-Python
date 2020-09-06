## Manipulating Strings



**Escape Characters**

| escape character | Prints as            |
| ---------------- | -------------------- |
| \'               | Single quote         |
| \''              | Double quote         |
| \t               | Tab                  |
| \n               | Newline (line break) |
| \\               | BackSlash            |



**Raw Strings**

place an *r* before the beginning quotation mark of a string to make it a raw string.

```python
>>> print(r'That is Carol\'s cat.') 
That is Carol\'s cat.
```



Multiline Strings with triple quotes

```python
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely, 
Bob''')

Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob
```



##### Useful String Methods

- Upper()
- Lower()

```python
>>> spam = 'Hello world!' 
>>> spam = spam.upper() 
>>> spam
'HELLO WORLD!'
>>> spam = spam.lower() 
>>> spam
'hello world!'
```



- isuppler()
- islower()

```python
>>> spam = 'Hello world!' >>> spam.islower()
False
>>> spam.isupper()
False
>>> 'HELLO'.isupper() True
>>> 'abc12345'.islower() True
>>> '12345'.islower() False
>>> '12345'.isupper() False
```



- Isalpha()
- Isalnum()
- Isdecimal()
- Isspace()
- Istitle()

```python
>>> 'hello'.isalpha() 
True
>>> 'hello123'.isalpha() 
False
>>> 'hello123'.isalnum() 
True
>>> 'hello'.isalnum() 
True
>>> '123'.isdecimal() 
True
>>> ' '.isspace() 
True
>>> 'This Is Title Case'.istitle()
True
>>> 'This Is Title Case 123'.istitle()
True
>>> 'This Is not Title Case'.istitle()
False
>>> 'This Is NOT Title Case Either'.istitle() False

```



- Startswith()
- Endswith()

```python
>>> 'Hello world!'.startswith('Hello') 
True
>>> 'Hello world!'.endswith('world!') 
True
>>> 'abc123'.startswith('abcdef') 
False
>>> 'abc123'.endswith('12')
False
>>> 'Hello world!'.startswith('Hello world!') True
>>> 'Hello world!'.endswith('Hello world!') 
True
```



- Join()

```python
>>> ', '.join(['cats', 'rats', 'bats']) 
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon']) 
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon']) 'MyABCnameABCisABCSimon'
```



- Split()

```python
>>> 'My name is Simon'.split() 
['My', 'name', 'is', 'Simon']

>>> 'MyABCnameABCisABCSimon'.split('ABC') 
['My', 'name', 'is', 'Simon']

>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
```

```python
>>> spam = '''Dear Alice,
How have you been? I am fine. There is a container in the fridge that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
>>> spam.split('\n')
['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.', 'Sincerely,', 'Bob']
```



- Just()
- Ljust()
- Center()

```python
>>> 'Hello'.rjust(10)
'			Hello'
>>> 'Hello'.rjust(20)
' 							Hello'
>>> 'Hello World'.rjust(20) 
' 							Hello World'
>>> 'Hello'.ljust(10) 
'Hello 

>>> 'Hello'.rjust(20, '*') 
'***************Hello'
>>> 'Hello'.ljust(20, '-') 
'Hello---------------'

>>> 'Hello'.center(20)
' Hello '
>>> 'Hello'.center(20, '=') '=======Hello========'
```



- strip()
- lstrip()
- rstrip()

```python
>>> spam = ' Hello World ' 
>>> spam.strip()
'Hello World'
>>> spam.lstrip()
'Hello World ' 
>>> spam.rstrip() 
' Hello World'

>>> spam = 'SpamSpamBaconSpamEggsSpamSpam' 
>>> spam.strip('ampS')
'BaconSpamEggs'
```



##### copying and pasting strings with the pyperclip module

```python
>>> import pyperclip
>>> pyperclip.copy('Hello world!') 
>>> pyperclip.paste()
'Hello world!'
```

