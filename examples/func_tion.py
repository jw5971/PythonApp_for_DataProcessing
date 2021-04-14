# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:52:46 2020

@author: JIWU5
"""

def print_1_to_100():
    """
    print_1_to_100:
        
        Print integers from 1 to 100 (inclusive), using following rules:
        for multiples of 3, print “Fizz” (instead of the number);
        for multiples of 5, print “Buzz” (instead of the number); 
        for multiples of both 3 and 5, print “FizzBuzz” (instead of the number)
    
    """
    for i in range(1, 101,1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 15 == 0:
            print("FizzBuzz")
        else:
            print(i)


def Next_Prime(x):
    """
    Next_Prime:
        given an arbitrary integer x, calculate the next biggest prime number
    Parameters:
        int, x 
    returns:
        the next biggest prime number
    
    """
    x += 1

    for i in range(2, x):

        if (x % i) == 0:
            x += 1
    else: return x

def Swap(A, B):
    """
    Swap:
        exchange the value of two numbers without using other middle variables
     Parameters:
         two numbers, A,B
    return:
        the resulted variables with echanged value
    """
    
    A, B = B, A
    
    return A, B


def Palindrome(word):
    """
    Palindrome:
        chech whether a word is a Palindrome
    Parameters:
        string, a word
    Return:
        True/False    
    """
    if  word == word[::-1]:   
        return True
    else:
        return False
   

def main():
    print('Func1: print 1 - 100 \n' )
    print_1_to_100()
    print('Finish printing 1 - 100 \n' )
    
    print('Func2: print next prime' )
    x = int(input('Please input a positive integer:'))
    NPrime = Next_Prime(x)
    print('The next prime is ', NPrime )
    print('Finish printing the next prime \n' )
    
    print('Func3: Swap' )
    A, B = map(int, input('Please input two numbers seperated by space:').split())
    print("Before swap - ","A:",A,"\n","B:",B)
    A, B = Swap(A,B)
    print("After swap - ","A:",A,"\n","B:",B)
    print('Finish Swap \n' )
    
    print('Func4: palindrome' )
    print(Palindrome(input("Please input a word:")))
    print('Finish judging palindrome \n' )

if __name__ == '__main__':
    main()