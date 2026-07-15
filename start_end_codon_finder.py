'''
Target Sequence Slicer
Input: 
    Ask the user to input a 15-character nucleotide sequence (e.g., "ATGCGTAACGTTGCA").
Task: 
    Use string slicing to extract and print only the first 3 characters (the start codon) and the last 3 characters. 
    Use negative indexing to find the last 3 characters.  
'''

str = input(str("Enter 15-character nucleotide sequence: "))

print("Start codon: ",str[:3]) 
print("End codon: ",str[-3:])
