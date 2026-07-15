# Ask students for their grades then evaluate their division, where they stands?

# First i would like to ask students for their final SEM Grades

Grade = float(input("Enter your Final SEM Grade out of 10: "))

# Then gives division based on their grades
if(Grade >= 8):
    print("First Diviosion with Distinction")
elif(Grade >= 7 and Grade < 8):
    print("First Division")
elif(Grade >=6 and Grade < 7):
    print("Second Division")
elif(Grade >= 5.5 and Grade < 6):
    print("Pass")
else:
    print("Fail")
