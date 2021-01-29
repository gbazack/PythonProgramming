"""
This module contains functions
which generate prime numbers
and test if an input number is prime
"""
import math

def generate(n):
   pnList=[2,3]
   nlist=list(range(4,n+1))
   
   for x in nlist:
      y=[math.gcd(i,x) for i in nlist]      
      if(y.count(1)+y.count(x))==len(y):
         pnList.append(x)
   return pnList

