'''
Write a function calculate_tm(primer) that estimates the melting temperature (Tm) of a given DNA primer string.
Rules:
    If the primer is less than 14 bases, use the Wallace rule:
        T_{m} = (wA + xT) * 2 + (yG + zC) * 4
    If the primer is 14 bases or longer, use the basic salt-adjusted formula:
        T_{m} = 64.9 + 41 * [ {(yG + zC - 16.4)} // {(wA + xT + yG + zC)} ]
    (Where w, x, y, and z are the counts of A, T, G, and C nucleotides, respectively).
Goal: 
Practice mathematical logic in Python, conditional statements, and counting string elements efficiently.
'''

primer_seq = input("Enter Your Primer Sequence: ").upper().strip()

len_primer_seq = len(primer_seq)
print("Your Primer Sequence Legth: ",len_primer_seq)

A_count = primer_seq.count("A")
T_count = primer_seq.count("T")
G_count = primer_seq.count("G")
C_count = primer_seq.count("C")

# use Wallance Rule Formula for Primer length <= 14
Tm_1 = 4 * (G_count + C_count) + 2 * (A_count + T_count)

# use The Basic satl-adjusted Formula for Primer length > 14
Tm_2 = 64.9 + (41 * ((G_count + C_count - 16.4) // (len_primer_seq)) )

if(len_primer_seq <= 14):
    print("Your Sequence is less than 14 ntd. So, Melting Temperature by Wallance Rule Formula is", Tm_1)
else:
    print("Your Sequence is Greater than 14 ntd. So, Melting Temperature by The Basic salt-adjusted Fromula is", Tm_2)

