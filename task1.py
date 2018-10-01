#My first attempt


# Open the file

myfile = open("running-config.cfg")

# Variables for storing stuff
mylist_intname = []

#Run throught the file and collect the interfacenames
for line in myfile:
  # First Remove the whitespaces and extra stuff from the beg and end
  line = line.strip()
  # Create a list of strings for each line
  line = line.split()
  """ This is the place where we check if list of 0 is "interface" and copy the value of list of 1 """
  if (line[0] == "interface"):
    mylist_intname.append(line[1])

print (mylist_intname)
