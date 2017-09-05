var = input("Please enter a number: ")
if var >= 100: print "Thats a big number! #", var
else: print var, ": that's a small number"

# string = '';
string = raw_input("Please enter a string: ")
if len(string) < 50: print "short list"
else: print "long sentence"

myList = list()
output = []
myList = raw_input("please enter a list:")
output = myList.split(",")
if len(myList) >= 10: print"Big list"
else: print "short list"
# 1, 2, 3, leeroy jenkins, 4, 5
print output
#print output[3] #to see leeroy jenikins
