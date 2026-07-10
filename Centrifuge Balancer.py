'''
A centrifuge must be perfectly balanced to run safely. 
Write a program that asks the user for the weight of Sample A (integer) and the weight of Sample B (integer).

The Logic: 
Using an if/else statement, print "Safe to run" if the two weights are exactly equal to each other. 
If they are not equal, print "Danger: Unbalanced". 
(Hint: To check if two things are exactly equal in Python, use the double equals sign ==).
'''

W1 = int(input("Enter weight of Sample 1= "))
W2 = int(input("Enter weight of Sample 2= "))

if(W1 == W2):
    print("Safe to Run")
else:
    print("Danger: Unbalanced")