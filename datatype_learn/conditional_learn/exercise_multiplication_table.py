# Write a Python program to create the multiplication table (from 1 to 10) of a number.
n=int(input("enter a number:"))
for number in range(1,11):
    multiplication=number*n
    print("{} x {}= {}".format(number,n,multiplication))