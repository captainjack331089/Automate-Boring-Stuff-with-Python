## Dictionary Data Type

```python
>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur.' 'My cat has gray fur.'
```



**Dictionaries vs. Lists**

There is no "first" item in a dictionary. While the order o items matters for determining whether two lists are the same, it doews not matter in what order the key-value pairs are typed in a dictionary.

```python
>>> spam = ['cats', 'dogs', 'moose'] 
>>> bacon = ['dogs', 'moose', 'cats'] 
>>> spam == bacon
False

>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'} 
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'} 
>>> eggs == ham
True
```

Dictionaries are not ordered, so they can't be sliced like lists.



**The Keys(), values(), and items() Methods**

- Values()

  ```python
  >>> spam = {'color': 'red', 'age': 42}
  >>> for v in spam.values():
  print(v)
  red 42
  ```

- Keys()

  ```python
  >>> for k in spam.keys(): 
  				print(k)
  color
  age
  ```

  *passing list-like return value of keys()*

  ```python
  >>> spam = {'color': 'red', 'age': 42} >>> spam.keys()
  dict_keys(['color', 'age'])
  >>> list(spam.keys())
  ['color', 'age']
  ```

- Items():

  ```python
  >>> for i in spam.items():
  print(i)
  ('color', 'red') ('age', 42)
  ```

  *Use the multiple assignment trick in a for loop to assign the key and value to separate variables.*

  ```python
  >>> spam = {'color': 'red', 'age': 42} >>> for k, v in spam.items():
  print('Key: ' + k + ' Value: ' + str(v))
  Key: age Value: 42
  Key: color Value: red
  ```

- Get()

  ```python
  >>> picnicItems = {'apples': 5, 'cups': 2}
  >>> 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.' 'I am bringing 2 cups.'
  >>> 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.' 'I am bringing 0 eggs.'
  ```

  *if there is no such key or the index of value, the default value 0 is returened by the get() method.*

- Setdefault()

  ```python
  >>> spam = {'name': 'Pooka', 'age': 5}
  >>> spam.setdefault('color', 'black') 'black'
  >>> spam
  {'color': 'black', 'age': 5, 'name': 'Pooka'} 
  >>> spam.setdefault('color', 'white')
  'black'
  >>> spam
  {'color': 'black', 'age': 5, 'name': 'Pooka'}
  ```

  Setdefault() method is a nice shortcut to ensure that a key exists.

  eg.

  ```python
  message = 'It was a bright cold day in April, and the clocks were striking thirteen.' 
  count = {}
  for character in message: 				    
  		count.setdefault(character, 0) 
  		count[character] = count[character] + 1
  print(count)
  
  {' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2, 'i': 6, 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}
  ```

- PRetty Printing

  A cleaner display of the items in a dictionary than what print() provides:

  ```python
  import pprint
  message = 'It was a bright cold day in April, and the clocks were striking thirteen.' 
  count = {}
  for character in message: 				    
  		count.setdefault(character, 0) 
  		count[character] = count[character] + 1
  pprint.pprint(count)
  
  {' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'b': 1, 'c': 3, 'd': 3, 'e': 5, 'g': 2, 'h': 3, 'i': 6,'k': 2, 'l': 3, 'n': 4, 'o': 2, 'p': 1, 'r': 5, 's': 3, 't': 6, 'w': 2, 'y': 1}
  
  ```

  It's helpful when the dictionary itself contains nested lists or dictionaries.