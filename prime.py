# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:54:03 2021
@author: Jim Carlson
"""

def prime_list(n):  #using lists, 'while' loop and Seive of Eratosthenes
    '''generate list of primes <= n, where n is an integer >= 2
       n <= 10**6 is a practical limit
    '''
    ppp = [2] #create list to hold 1st prime and subsequent primes
    xxx=list(range(3,n+1,2)) #all subsequent primes are odd integers
    while len(xxx) > 0:
        ppp.append(xxx[0]) #append prime number to list ppp from list xxx[0]
        xxx = [i for i in xxx if i%xxx[0] != 0] #delete all multiples of the prime
        if len(xxx) == 0 or xxx[0] > n**0.5: #sequence of 'or' is important
            break
    return  ppp+xxx
