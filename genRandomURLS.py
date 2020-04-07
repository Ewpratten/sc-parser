from random import choice
import string

def genim(code):
    return f"<img src='https://prnt.sc/{code}'>"

def getcode():
    return ''.join([choice(string.ascii_lowercase +  "0123456789") for i in range(6)])


print("firefox -new-tab", end="")
for i in range(30):
    print(f"-url https://prnt.sc/{getcode()}", end="")
    # print(f"<iframe src='https://prnt.sc/{getcode()}'>")
print("")