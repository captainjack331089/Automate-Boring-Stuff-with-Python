#### FIle and FIle Paths

- os.path.join(): will return a string with a file path using the correct path separators.

  ```python
  import os
  print(os.path.join('usr','bin','spam'))
  
  usr/bin/spam
  ```

  

  It is helpful if you need to create strings for filenames. These string will be passed to several of the file-related functions.

  The following example joins names from a list fo filenames to the end of a folder's name:

  ```python
  myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
  
  for file in myFiles:
      print(os.path.join('usr', 'bin', 'test', file))
      
  usr/bin/test/accounts.txt
  usr/bin/test/details.csv
  usr/bin/test/invite.docx
  ```

  

####  Current Working Directory

- os.getcwd(): get the current working directory
- os.chdir(): change the current working directory

```python
current_path = os.getcwd()
print(current_path)

/Users/captainjack33/Automate Boring Stuff with Python/Automation Tasks/Practice


current_path = os.getcwd()
os.chdir('/usr/bin/')
current_path = os.getcwd()
print(current_path)

/usr/bin
```



---



#### os.path Module

```python
>>> os.path.abspath('.')
'C:\\Python34'
>>> os.path.abspath('.\\Scripts') 
'C:\\Python34\\Scripts'
>>> os.path.isabs('.')
False
>>> os.path.isabs(os.path.abspath('.')) 
True

>>> os.path.relpath('C:\\Windows', 'C:\\')
'Windows'
>>> os.path.relpath('C:\\Windows', 'C:\\spam\\eggs') '..\\..\\Windows'
>>> os.getcwd()
'C:\\Python34'
```



- os.path.dirname(path)

  ```python
  >>> path = 'C:\\Windows\\System32\\calc.exe' 
  >>> os.path.basename(path)
  'calc.exe'
  >>> os.path.dirname(path) 
  'C:\\Windows\\System32'
  ```

- os.path.split()

  ```python
  >>> calcFilePath = 'C:\\Windows\\System32\\calc.exe' 
  >>> os.path.split(calcFilePath) 
  ('C:\\Windows\\System32', 'calc.exe')
  ```



#### Finding File Sizes and Folder Contents

- os.path.getsize(path) will return the size in bytes of the file in the path argument.

  ```python
  >>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
  776192
  ```

  

- os.listdir(path) will return a list of filename strings for each file in the path argument.

  ```python
  >>> os.listdir('C:\\Windows\\System32')
  ['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll', --snip--
  'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']
  ```

  

- os.path.exists(path) return if the path or folder referred to in the argements exists.



- os.path.isfile(path) return if the path argument exists and is a file.



-  os.path.isdir(path) return if the path argument exists and is a folder.



---



#### The file reading/writing Process



***Reading***

- open()
- read()
  - Readlines()
- close()



***writing***

- write()



##### Saving variables with the shelve Module

save raiables in python programs to binary shelf files using the shelve module.

```python
>>> import shelve
>>> shelfFile = shelve.open('mydata') 
>>> cats = ['Zophie', 'Pooka', 'Simon'] 
>>> shelfFile['cats'] = cats
>>> shelfFile.close()

#open the shelf files to check that data was stored correctly
>>> shelfFile = shelve.open('mydata') 
>>> list(shelfFile.keys())
['cats']
>>> list(shelfFile.values()) 
[['Zophie', 'Pooka', 'Simon']]
>>> shelfFile.close()
```



##### Saving variables with the pprint.pformat() function

```python
>>> import pprint
>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}] 
>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
>>> fileObj = open('myCats.py', 'w')
>>> fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
83
>>> fileObj.close()

#then open myCats.py  and read the file.
>>> import myCats
>>> myCats.cats
[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}] >>> myCats.cats[0]
{'name': 'Zophie', 'desc': 'chubby'}
>>> myCats.cats[0]['name']
'Zophie'
```

