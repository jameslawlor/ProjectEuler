"""
=================================================
Project Euler Exercise 5
=================================================
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder. What is the smallest positive number that is evenly
 divisible by all of the numbers from 1 to 20?
"""
# Author: James Lawlor <jalawlor@tcd.ie>

def divisible(x,y = 20):
  for i in range(y, 0,-1):
    if x % i != 0: return False
      return True
j = 3
while divisible(j,10) != True:
  j+=1
print j
