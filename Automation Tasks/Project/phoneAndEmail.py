#coding:utf-8
#A project that matching all the emails and phone number from the clipboard
"""
Say you have the boring task of finding every phone number and email address in a long web page or document. If you manually scroll through the page, you might end up searching for a long time. But if you had a pro- gram that could search the text in your clipboard for phone numbers and email addresses, you could simply press ctrl-A to select all the text, press ctrl-c to copy it to the clipboard, and then run your program. It could replace the text on the clipboard with just the phone numbers and email addresses it finds.
"""""

import re, pyperclip

#TODO: Create Phone number regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                   #group1: area code with '()' or w/o '() or no area code both valid
    (\s|-|\.)?                           #group2: any space or '-'(0 or 1) are all valid
    (\d{3})                              #group3: 3 nubmers
    (\s|-|\.)                            #group4: another seperator
    (\d{4})                              #gorup5: 4 numbers
    (\s*({ext|ext.|x)\s*({\d{2,5}))?     #group6 and group7: extension
)''', re.VERBOSE)

#TODO: Create Email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9.%+-]+                     # any valid character
    @                                    # @
    [a-zA-Z0-9.-]+                       # domain
    (\.[a-zA-Z]{2,4})                    # dot.sth(2-4 characters)
)''', re.VERBOSE)

#TODO: Find match in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    #print(groups)
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups[0])

#TODO: Copy result to CLipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard..')
    print('\n'.join(matches))
else:
    print('No numbers or email found')
