"""
=================================================
Project Euler Exercise 4
=================================================
A palindromic number reads the same both ways. The largest palindrome: made from
the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
# Author: James Lawlor <jalawlor@tcd.ie>
def palindromeCheck(x): # Checks to see if integer x is a palindrome
  return str(x)==str(x)[::-1]
largest = 0.0
# run through lists of all 3 digit numbers
for a,b in zip(range(999,100,-1),range(999,100,-1)):
  if palindromeCheck(a*b) == True and a*b > largest:
    largest = a*b
print largest			
