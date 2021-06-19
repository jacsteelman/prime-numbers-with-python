# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:54:03 2021
@author: Jim Carlson
"""

import numpy as np

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

def prime_np(n): #relatively easy to understand; generates a list of primes <= n
    '''generate list of primes <= n, limit of 10**9 (but 10**8 much faster)'''
    ppp = np.ones(n+1, dtype=bool) #array with True values
    ppp[0:2] = False #set first two elements to False
    for i in range(2,round(n**0.5)+1):  #range has the same values as the index IDs of array
        if i == 2:
            ppp[i*i::i] = False  #changes all even numbers except 2 to False
        elif ppp[i]:
            ppp[i*i::2*i] = False #selectively change True to False but skips even numbers
    ppp = np.flatnonzero(ppp) #return an array of index values of nonzero elements (the primes)
    return ppp
