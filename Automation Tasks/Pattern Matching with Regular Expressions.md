## Regular Expressions



**Finding Patterns of text without Regular. Expressions**

eg. if you want to find a phone number in a string. Like: 415-555-4242

```python
def isPhoneNumber(text): 
		if len(text) != 12:
        return False
    for i in range(0, 3):
				if not text[i].isdecimal(): 
          	return False
		if text[3] != '-': 	
      	return False
		for i in range(4, 7):
				if not text[i].isdecimal():
						return False 	
        if text[7] != '-':
        		return False
    for i in range(8, 12):
				if not text[i].isdecimal(): 
          	return False
		return True

print('415-555-4242 is a phone number:') print(isPhoneNumber('415-555-4242')) 
print('Moshi moshi is a phone number:') print(isPhoneNumber('Moshi moshi'))

415-555-4242 is a phone number: 
True
Moshi moshi is a phone number: 
False
```

To find a pattern of text in a larger sting:

```python
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
  	chunk = message[i:i+12]
    if isPhoneNumber(chunk):
      	print('Phone number found: ' + chunk)
print('DONE')

Phone number found: 415-555-1011 
Phone number found: 415-555-9999 
Done
    
```



#### Regular Expressisons



***Creating Regex Objects***

```python
import re	
```



- re.compile():

  Passing a string value representing your regular expression to re.compile() returns a Regex pattern object.

  

For to create a regex object that matches the phone number pattern:

```python
phoneNumbeRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
```



- A regex object's search():

  searches the string it is passed for any matches to the regex. The search() will return *None* if the regex pattern is not found in the string.

  If found: the search() method returns a Match object.

  - Group()

    The match objects have a group() method that will return the actual matched text from the searched string.

    ```python
    >>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
    >>> mo = phoneNumRegex.search('My number is 415-555-4242.') 
    >>> print('Phone number found: ' + mo.group())
    Phone number found: 415-555-4242
    ```



**Step to use regular expressions**

1. import the regex module with import re
2. Create a regex object with the re.compile() function.(better use raw string)
3. pass the string you want to search into the Regex object's search() method.
4. Call the Match object's group() method to return a string of the actual matched text.

---

**More Pattern Matching with Regular Expressions**



*Grouping with Parenthses*

eg. 

```python
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') >>> mo = phoneNumRegex.search('My number is 415-555-4242.') 
>>> mo.group(1)
'415'
>>> mo.group(2) 
'555-4242'
>>> mo.group(0) 
'415-555-4242' 
>>> mo.group() 
'415-555-4242'


>>> mo.groups()
('415', '555-4242')
>>> areaCode, mainNumber = mo.groups() 
>>> print(areaCode)
415
>>> print(mainNumber)
555-4242

```

```python
>>> phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') 
>>> mo = phoneNumRegex.search('My phone number is (415) 555-4242.') 
>>> mo.group(1)
'(415)'
>>> mo.group(2)
'555-4242'
```



***Matching Multiple Groups with the Pipe***

- '|':  likes or 

```python
>>> heroRegex = re.compile (r'Batman|Tina Fey') 
>>> mo1 = heroRegex.search('Batman and Tina Fey.') 
>>> mo1.group()
'Batman'
>>> mo2 = heroRegex.search('Tina Fey and Batman.') 
>>> mo2.group()
'Tina Fey'
```

When both batman and Tina Fey occur in the searched string, the first occurrence of matching text will be returned as the Match object.

```python
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)') 
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> mo.group(1) 'mobile'
```



***Optional Matching with the Question Mark***

- ? : a pattern wihich match 0 or 1 

  eg. 

  ```python
  >>> batRegex = re.compile(r'Bat(wo)?man')
  >>> mo1 = batRegex.search('The Adventures of Batman') 
  >>> mo1.group()
  'Batman'
  >>> mo2 = batRegex.search('The Adventures of Batwoman') 
  >>> mo2.group()
  'Batwoman'
  ```

  the (wo)? part of the regex means that the pattern *wo* is an optional group. The regex will match text that has 0 or 1 instances of *wo* in it.



Using the earlier phone number example, you can make the regex look for phone numbers that do or do not have an area code.

```python
>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') 
>>> mo1 = phoneRegex.search('My number is 415-555-4242') 
>>> mo1.group()
'415-555-4242'

>>> mo2 = phoneRegex.search('My number is 555-4242') 
>>> mo2.group()
'555-4242'
```



- *: a pattern which match 0 or more

```python
>>> batRegex = re.compile(r'Bat(wo)*man')
>>> mo1 = batRegex.search('The Adventures of Batman') 
\>>> mo1.group()
'Batman'
>>> mo2 = batRegex.search('The Adventures of Batwoman') 
>>> mo2.group()
'Batwoman'
>>> mo3 = batRegex.search('The Adventures of Batwowowowoman') >>> mo3.group()
'Batwowowowoman'
```



- +: match 1 or more.

  ```python
  >>> batRegex = re.compile(r'Bat(wo)+man')
  >>> mo1 = batRegex.search('The Adventures of Batwoman') 
  >>> mo1.group()
  'Batwoman'
  >>> mo2 = batRegex.search('The Adventures of Batwowowowoman') 
  >>> mo2.group()
  'Batwowowowoman'
  
  >>> mo3 = batRegex.search('The Adventures of Batman') 
  >>> mo3 == None
  True
  ```



- {'number'}: 'number' means that you want to repeat a specific number of times.

  ```python
  >>> haRegex = re.compile(r'(Ha){3}') 
  >>> mo1 = haRegex.search('HaHaHa') 
  >>> mo1.group()
  'HaHaHa'
  >>> mo2 = haRegex.search('Ha') 
  >>> mo2 == None
  True
  ```

  

##### Greedy and Nongreedy Matching



```python
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()
'HaHaHaHaHa'

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
'HaHaHa'
```

Note: '?' can have two meanings in regex: 

​			1: declaring a nongreedy match 

​			2: flagging an optional group



##### The final() Method

```python
#search() method
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000') 
>>> mo.group()
'415-555-9999'

#findall() method
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
# has no groups 
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') 
['415-555-9999', '212-555-0000']

# has groups
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups >>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '1122'), ('212', '555', '0000')]
```



---



##### Character Classes

| shorthand character class | represents                                                   |
| ------------------------- | ------------------------------------------------------------ |
| \d                        | any numeric digit from 0-9                                   |
| \D                        | any character that is not a numeric from 0-9                 |
| \w                        | any letter, numeric digit or the underscore character.       |
| \W                        | any character that is not a letter, numeric digit, or the underscore character |
| \s                        | any space, tab, or newline character                         |
| \S                        | any character that is not a space, tab, or newline           |



##### Making your own character classes

- ```python
  >>> vowelRegex = re.compile(r'[aeiouAEIOU]')
  >>> vowelRegex.findall('RoboCop eats baby food. BABY FOOD.') ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
  ```

- [a-zA-Z0-9] match all lowercase letters, uppercase letters, and numbers

- ```python
  >>> consonantRegex = re.compile(r'[^aeiouAEIOU]')
  >>> consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
  ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
  ```

  

##### The Caret and Dollar Sign Characters

- ^: Use (^) at the start of a regex to indicate tht a match must occur at the beginning of the searched text.
- $: Use($) at the end of the regex to indicate the string must end with this regex pattern.

```python
>>> beginsWithHello = re.compile(r'^Hello')
>>> beginsWithHello.search('Hello world!') 
<_sre.SRE_Match object; span=(0, 5), match='Hello'> >>> beginsWithHello.search('He said hello.') == None True


>>> endsWithNumber = re.compile(r'\d$')
>>> endsWithNumber.search('Your number is 42')
<_sre.SRE_Match object; span=(16, 17), match='2'>
>>> endsWithNumber.search('Your number is forty two.') == None True
```



##### Matching Newlines with the Dot Character

- .: (.) sign will match everything except a newline. By passing "re.DOTALL" as the second argument, you can make the dot character match all characters, including the newline character.

  ```python
  >>> noNewlineRegex = re.compile('.*')
  >>> noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group()
  'Serve the public trust.'
  
  >>> newlineRegex = re.compile('.*', re.DOTALL)
  >>> newlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group()
  'Serve the public trust.\nProtect the innocent.\nUphold the law.'
  ```



##### Review of Regex Symbols:

- '?' : matches 0 or 1 
- '*' : matches 0 or more
- '+' : matches 1 or more
- '{n}' : matches exactly n 
- '{n, }' : matches n or more
- '{,m}' : matches 0 to m
- '{n,m}' : matches n to m
- '{n,m}?' or '*?' or '+?' : matches non-greedy 
- '^spam' : string must begin with spam
- 'spam$' : string must end with spam
- '.' : matches any character except new line
- '\d', '\w', '\s' : matches a digit, word, or space character
- '\D', '\W', '\S' : matches anything except a digit, word, or space character
- '[abc]' : matches any character between the brackets
- [^abc]': matches any character that isn't between the brackets



##### Case-Insensitive Matching

**re.I(re.IGNORECASE)**: ignore the uppercase or lowercase

```python
>>> robocop = re.compile(r'robocop', re.I)
>>> robocop.search('RoboCop is part man, part machine, all cop.').group() 'RoboCop'
>>> robocop.search('ROBOCOP protects the innocent.').group() 'ROBOCOP'
>>> robocop.search('Al, why does your programming book talk about robocop so much?').group() 'robocop'
```



##### Substituting Strings with the sub() Method

```python
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.') 'CENSORED gave the secret documents to CENSORED.'
```

```python
>>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
>>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
A**** told C**** that E**** knew B**** was a double agent.'
```

----

#### Questions related to Regex

1. What is the function that creates Regex objects?

   re.compile

2. Why are raw strings ofter used when creating Regex objects?

   Backslashes("\\") doesnt need to be escaped.

3. what does the search() method return?

   return matched objects.

4. How do you get the actual strings that match the pattern from a Match objects?

   The group() method returns the strings of the matched text

5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group1? group 2?

   Group0: entire match

   Group1: first ()

   ..

6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

   \\()  \\.

7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

   If the regex has no groups, a list of strings is returned. if the regex has groups, a list of tuples of strings is returned.

8. What does the | character signify in regular expressions?

   Either, or

9. What two things does the ? character signify in regular expressions?

   1. 0 or 1 of the preceding group
   2. used to signify nongreedy matching

10. What is the difference between the + and * characters in regular expressions?

    1. +: match one or more
    2. *: match 0 or more

11. What is the difference between {3} and {3,5} in regular expressions?

    {3}: matches exactly 3 instances of the preceding group

    {3,5}: matchs betweeen three and five instances

12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

    \d: single digit

    \w: word

    \s: space character

13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

    \D: not a digit

    \W: not a word

    \S: not a space character

14. How do you make a regular expression case-insensitive?

    passing re.I or re.IGNORECASE as the second argument to re.compile()

15. What does the . character normally match? What does it match if

    re.DOTALL is passed as the second argument to re.compile()?

    .  matches any character except a new line.

    If re.DOTALL is passed as the second argument to re.compile(), the the dot will also match the new line.

16. What is the difference between .* and .*??

    .*  : performs a greedy match

    .*?   : performs a nongreedy match

17. What is the character class syntax to match all numbers and lowercase letters?

    [0-9a-z]

18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

    'X drummers, X pipers, five rings, X hens'

19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

    the re.VERBOSE arguments allows you to add whitespace and comments to the string passed to re.compile()

20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

    - '42'
    - '1,234'
    - '6,368,745'
       but not the following:

    - '12,34,567' (which has only two digits between the commas)
    - '1234' (which lacks commas)

    re.compile(r'^d{1,3}(,{3})*$')

21. How would you write a regex that matches the full name of someone whose last name is Nakamoto? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

    - 'Satoshi Nakamoto'
    - 'Alice Nakamoto'
    - 'RoboCop Nakamoto' but not the following:

    - 'satoshi Nakamoto' (where the first name is not capitalized)
    - 'Mr. Nakamoto' (where the preceding word has a nonletter character)
    - 'Nakamoto' (which has no first name)
    - 'Satoshi nakamoto' (where Nakamoto is not capitalized)

    re.compile(r'^[[A-Z]][][a-z]*\sNakamoto')

22. How would you write a regex that matches a sentence where the first word is either *Alice*, *Bob*, or *Carol*; the second word is either *eats*, *pets*, or *throws*; the third word is *apples*, *cats*, or *baseballs*; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

    - 'Alice eats apples.'
    - 'Bob pets cats.'
    - 'Carol throws baseballs.'
    - 'Alice throws Apples.'
    - 'BOB EATS CATS.' but not the following:

    - 'RoboCop eats apples.'
    - 'ALICE THROWS FOOTBALLS.'
    - 'Carol eats 7 cats.'

    re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\\.', re.I)

