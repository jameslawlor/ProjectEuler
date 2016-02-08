# Reduce to a mathematical problem - for an nxn grid there must be n Rights and n Downs. 
# How many ways can you order n Rights in a 2n sequence? This is answered by the binomial theorem:
import math; n=20;print math.factorial(2*n)/(math.factorial(n)*math.factorial(n))
