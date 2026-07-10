# Write a program that asks the user to input a pH level (as a floating-point number).

ph = float(input("Enter ph value= "))

if(14 > ph > 7):
    print("Basic ph")
elif(7 > ph > 0):
    print("Acidic ph")
elif(ph == 7):
    print("Neutral ph")
else:
    print("ph is out of Range!")    
