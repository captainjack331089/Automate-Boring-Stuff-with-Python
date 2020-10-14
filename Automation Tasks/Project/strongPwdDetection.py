#coding:utf-8
"""

Strong Password Detection
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase charac- ters, and has at least one digit. You may need to test the string against mul- tiple regex patterns to validate its strength.
"""""
import re
def isStrongpassword(password):
    """
    1: at least 8 charcaters long
    2: contains both uppercase and lowercase
    3: at least one digit
    :return:
    """
    t = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])\w{8,}$')
    check2 = t.search(password)
    #print(check2)

    if check2:
        return True
    return False
if __name__ == '__main__':
    p = str(input('1: at least 8 charcaters long \n 2: contains both uppercase and lowercase \n 3: at least one digit \n Please enter a password following by the above: '))
    if isStrongpassword(p):
        print('password is good')
    else:
        print('password is weak')

