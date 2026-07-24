"""
In bioinformatics, reading direction matters. Write a program to check if a list of nucleotides 
(e.g., ["A", "T", "G", "T", "A"]) is a palindrome, meaning it reads the exact same forwards and backwards. 
(Hint: use the copy() and reverse() methods).
"""

ntd = ["A", "T", "G", "T", "A"]
ntd_copy = ntd.copy()
ntd_copy.reverse()

if(ntd == ntd_copy):
    print("This is palindrome.")
else:
    print("This is not Plaindrome.")
