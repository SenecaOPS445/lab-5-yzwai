#!/usr/bin/env python3
# Author ID: yzwai, 133310227

def add(number1, number2):
    # Add two numbers together, return the result, 
    try:
        return int(number1) + int(number2)
    # if error return string 'error: could not add numbers'
    except (ValueError, TypeError):
        return 'error: could not add numbers'
    

def read_file(filename):
    # Read a file, return a list of all lines, 
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    # if error return string 'error: could not read file'
    except FileNotFoundError:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception