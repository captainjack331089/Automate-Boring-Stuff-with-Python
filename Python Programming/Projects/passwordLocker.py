# coding:utf-8
# An insecure password locker program

PASSWORDS = {'email': '123',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  #first command line arg is the account name
# print(account)
# print(PASSWORDS)
if account in PASSWORDS:
    #print(sys.argv)
    pyperclip.copy(PASSWORDS[account])
    print('PASSWORD for' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
