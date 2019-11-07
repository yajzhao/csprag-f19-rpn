#!/usr/bin/env python3

import operator
from colorama import init
from colorama import Fore, Back, Style
init()

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}


def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
   
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if int(result) < 0:
            print(Fore.RED + str(result))
            print(Style.RESET_ALL)        
        else:
            print(Back.GREEN + str(result))
            print(Style.RESET_ALL)

if __name__ == '__main__':
    main()
