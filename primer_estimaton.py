''' 
Problem: The Primer Melting Temperature (T_m) Estimator

A common rule of thumb for calculating the basic melting temperature of a short DNA primer is the Wallace Rule:
T_m = 4 \times (G + C) + 2 \times (A + T)
The Input: 
    Ask the user to input a primer sequence.
The Task:
    Clean the input to ensure it is uppercase and has no hidden spaces at the beginning or end.
    Count the total number of G and C nucleotides.
    Count the total number of A and T nucleotides.
    Calculate the T_m using the Wallace formula.
The Logic: 
    An ideal primer often has a T_m between 52°C and 65°C. Use chained comparisons 
    (like you did in the pH problem) to check the T_m. If it falls in this range, print "Optimal Tm". 
    If it is lower, print "Tm too low". 
    If it is higher, print "Tm too high".
'''
# Ask the user to input a primer sequence.
primer_seq = input("Enter Your primer Sequence: ").upper().strip()


G_count = primer_seq.count("G")
C_count = primer_seq.count("C")
A_count = primer_seq.count("A")
T_count = primer_seq.count("T")

# Calculate the T_m using the Wallace formula
T_m= 4 * (G_count + C_count) + 2 * (A_count + T_count)

print(T_m)

if(52 <= T_m <= 65):
    print("Optimal Tm")
elif(T_m < 52):
    print("Tm too Low")
else:
    print("Tm too High")

