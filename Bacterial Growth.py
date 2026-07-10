'''
A specific bacterial culture doubles in number every hour. 
Write a program that asks the user for a starting number of bacteria (integer).
'''

# formula of Bacterial growth is Nt = N0 * 2^n.

N0 = int(input("Enter Initial Number of Bacterial Culture= "))
t = int(input("Total Time in Minutes= "))
g = int(input("Generation Time in Minutes= "))

# Calculate n = (t/g)
n = t / g

# Calculate the bacterial growth 
Nt = N0 * (2**n)

print("Final Number of Bacteria= ", Nt)
