# List



**The List Data Type**:

```python
>>> [1, 2, 3]
[1, 2, 3]
>>> ['cat', 'bat', 'rat', 'elephant'] ['cat', 'bat', 'rat', 'elephant']
```



**Getting individual values in a list with indexes**

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant'] 
>>> spam[0]
'cat'
>>> spam[1]
'bat'
>>> spam[2] 'rat'
>>> spam[3] 'elephant'
```



**Negative Indexes**

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant'] 
>>> spam[-1]
'elephant'
```



**Getting Sublists with Slices**

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant'] 
>>> spam[0:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[1:3]
['bat', 'rat']
>>> spam[0:-1] ['cat', 'bat', 'rat']
```



**Getting a List's Length with Len()**

```python
>>> spam = ['cat', 'dog', 'moose'] 
>>> len(spam)
3
```



**List Concatenation and List Replication**

```python
>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z'] 
>>> spam = [1, 2, 3]
>>> spam = spam + ['A', 'B', 'C'] >>> spam
[1, 2, 3, 'A', 'B', 'C']
```



**Removing Values from Lists with del Statements**

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant'] >>> del spam[2]
>>> spam
['cat', 'bat', 'elephant']
>>> del spam[2] >>> spam ['cat', 'bat']	
```



---



**Using s struction to work with lists**

```python
catNames = [] 
while True:
		print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
		name = input() 
		if name == '':
				break
		catNames = catNames + [name] # list concatenation
print('The cat names are:') 
for name in catNames:
		print(' ' + name)
    
    
result:
  
Enter the name of cat 1 (Or enter nothing to stop.):
Zophie
Enter the name of cat 2 (Or enter nothing to stop.):
Pooka
Enter the name of cat 3 (Or enter nothing to stop.):
Simon
Enter the name of cat 4 (Or enter nothing to stop.):
Lady Macbeth
Enter the name of cat 5 (Or enter nothing to stop.):
Fat-tail
Enter the name of cat 6 (Or enter nothing to stop.):
Miss Cleo
Enter the name of cat 7 (Or enter nothing to stop.):
The cat names are:
		Zophie
		Pooka
		Simon
		Lady 	
    Macbeth 
    Fat-tail 
    Miss 
    Cleo
```



**Using For loop with lists**

```python
>>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders'] 
>>> for i in range(len(supplies)):
print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers 
Index 3 in supplies is: binders

```



**Multiple Assignment Trick**

```python
For typing this:

>>> cat = ['fat', 'black', 'loud'] 
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]

same as: 
>>> cat = ['fat', 'black', 'loud'] 
>>> size, color, disposition = cat
```



---

#### Methods

Methods belong to a single data type.

- Finding a Value in a list with **index()** method

  ```python
  >>> spam = ['hello', 'hi', 'howdy', 'heyas'] 
  >>> spam.index('hello')
  0
  >>> spam.index('heyas')
  3
  ```

  When there are duplicates of the value in the list, the index of its first appearance is returned. 

- Adding Values to Lists with the **append()** and **insert()** methods

  ```python
  >>> spam = ['cat', 'dog', 'bat'] 
  >>> spam.append('moose')
  >>> spam
  ['cat', 'dog', 'bat', 'moose']
  
  >>> spam = ['cat', 'dog', 'bat'] 
  >>> spam.insert(1, 'chicken') 
  >>> spam
  ['cat', 'chicken', 'dog', 'bat']
  ```

- Remove Values from lists with remove()

  ```python
  >>> spam = ['cat', 'bat', 'rat', 'elephant'] 
  >>> spam.remove('bat')
  >>> spam
  ['cat', 'rat', 'elephant']
  ```

  If the value appears multiple times in the list, only the first instance of the value will be removed

- Sorting the values in a list with the sort() Method

  ```python
  >>> spam = [2, 5, 3.14, 1, -7] 
  >>> spam.sort()
  >>> spam
  [-7, 1, 2, 3.14, 5]
  >>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants'] 
  >>> spam.sort()
  >>> spam
  ['ants', 'badgers', 'cats', 'dogs', 'elephants']
  ```

  ```python
  >>> spam.sort(reverse=True)
  >>> spam
  ['elephants', 'dogs', 'cats', 'badgers', 'ants']
  ```

  - the sort() methods sorts the list in place

  - can not sort lists that have both number values and string values in them.

  - Sort() uses "ASCIIbetical order" rather than actual alphabetical order for sorting strings.

    eg.

    ```
    >>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats'] 
    >>> spam.sort()
    >>> spam
    ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
    ```

    

---



### List-like Types: Strings and Tuples



##### Strings

- List value is a mutable data type
- string is immutable



The proper way to "mutate" a string is to use slicing and concatenation to build a new string by copying from parts of the old string.



##### Tuple

- tuples are typed with parentheses

- Tuples are immutable

- If you have only one value in your tuple, you can indicate this by placing a trailing comma after the value inside the parentheses.

  eg. 

  ```python
  >>> type(('hello',)) 
  <class 'tuple'>
  >>> type(('hello')) 
  <class 'str'>
  ```

- transfer between list and tuple and string

  ```
  >>> tuple(['cat', 'dog', 5]) ('cat', 'dog', 5)
  >>> list(('cat', 'dog', 5)) ['cat', 'dog', 5]
  >>> list('hello')
  ['h', 'e', 'l', 'l', 'o']
  ```

---

#### Reference

- variable change:

  ```python
  >>> spam = 42
  >>> cheese = spam
  >>> spam = 100 
  >>> spam
  100
  >>> cheese
  42
  ```

- list refer

  ```python
  >>> spam = [0, 1, 2, 3, 4, 5] 
  >>> cheese = spam
  >>> cheese[1] = 'Hello!'
  >>> spam
  [0, 'Hello!', 2, 3, 4, 5] 
  >>> cheese
  [0, 'Hello!', 2, 3, 4, 5]
  ```

  above code: 

  cheese and spam both reference to the list. so change any of the variable('cheese' or 'spam') will affect the list.



**The copy Module's copy() and deepcopy() Functions**

- Copy() can be used to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference.

  ```python
  >>> import copy
  >>> spam = ['A', 'B', 'C', 'D'] 
  >>> cheese = copy.copy(spam) 
  >>> cheese[1] = 42
  >>> spam
  ['A', 'B', 'C', 'D']
  >>> cheese
  ['A', 42, 'C', 'D']
  ```

  

- Deepcopy(): if the list you need to copy contains lists, the use the copy.deelpcopy() function instaead of copy.copy. The deepcopy() function will copy these inner lists as well.



