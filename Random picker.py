import random

for i in range(10*100):



    line = str(input("Enter Name:"))
    print("Be sure to split the names using space")
    read=line.split()
    randomwrd = random.choice(read)
    print("Name Selected: "+randomwrd)
    print(" ")