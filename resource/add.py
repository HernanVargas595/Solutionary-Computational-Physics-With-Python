import sys
x = float(sys.argv[1]) # Note that the items in argv [ ]
y = float(sys.argv[2]) # are strings!
print("%0.3f + %0.3f = %0.3f " % (x, y, (x+y)))