'''
Problem: CRISPR Cas9 PAM Validator

For CRISPR Cas9 to successfully cut DNA, the 20-nucleotide guide RNA target sequence must be immediately followed by a PAM sequence, 
which is typically "NGG" (meaning any nucleotide, followed by two Guanines).
The Input: 
    Ask the user for a raw DNA target sequence.
The Task: 
    Clean the sequence (uppercase, remove spaces). 
    First, check if the length of the sequence is exactly 23 nucleotides (20 for the target + 3 for the PAM).
The Logic:
    If the length is not 23, print "Error: Sequence must be exactly 23 nucleotides."
    If the length is correct, check if the very last two characters are exactly "GG".
    If they are "GG", print "Valid Cas9 Target". Otherwise, print "Invalid PAM Sequence".
    (Hint: You will need a nested if/else statement here, or use the and operator!)
'''

raw_seq = input("Enter Your Raw DNA Target Sequence: ").upper().strip()

print(len(raw_seq))

if(len(raw_seq) != 23):
    print("Error: Sequence must be exactly 23 nucleotides.")
elif(len(raw_seq) == 23):
    print("Lenght is correct.")
    if(raw_seq.endswith("GG")):
        print("Valid Cas9 Target")
    else:
        print("Invalid PAM Sequence")

