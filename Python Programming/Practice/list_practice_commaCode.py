"""
Comma Code
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your func-tion should be able to work with any list value passed to it.
"""

def commaCode(alist):
    s = ', '
    l = len(alist)
    temp =  ''
    for i in range(1,l-1):
        temp += s + alist[i]

    return (alist[0] + temp + ' and ' + alist[-1])

if __name__ == '__main__':
    spam = ['apples', 'bananas', 'orange', 'tofu', 'cats']
    print(commaCode(spam))
