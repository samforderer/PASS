# Author: Sam Forderer, 000355553
# PASS: Week 10
# File IO and Lists

# Summary: Goal of this program is to take a list of names from the user in a while loop
#          and write them to a file.


names = [] # The array of names.
name = "" # The current name in while loop.


while True:
    name = input("Enter Name or 'q' to stop: ")
    if name == "q" or name == " ":
        break

    names.append(name)    
 

# Create/open file.
filename = (input("Enter filename:") + ".txt")
f = open(filename, "a")


# Loop through each name and write them to file.
for name in names:
    f.write(name + "\n")

# Must close the file when finished.
f.close()



