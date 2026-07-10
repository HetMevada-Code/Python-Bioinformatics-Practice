'''
Problem 3: Restriction Enzyme Cutter

EcoRI is a restriction enzyme that cuts DNA specifically at the sequence "GAATTC".
The Input: 
    Ask the user for a long DNA sequence.
The Task: 
    Count how many times the sequence "GAATTC" appears in the user's string.
The Logic:
    If the count is 0, print "No EcoRI cut sites found."
    If the count is exactly 1, print "Sequence will be cut into 2 fragments."
    If the count is greater than 1, print "Warning: Multiple cut sites detected!"
'''

dna_Seq = input("Enter Long DNA Sequence: ")
re_sites = dna_Seq.count("GAATTC")

if(re_sites == 0):
    print("No ECORI cut sites found.")
elif(re_sites == 1):
    print("Sequence will be cut into 2 fragments.")
else:
    print("Warning: Multiple cut sites detected!")