number = 312051

found = False
loop = 0
bottomLeft = 0
while not found:
    loopWidth = 2 * loop + 1
    bottomLeft = loopWidth * loopWidth
    if number <= bottomLeft:
        found = True
    else:
        loop+= 1
        
diff = bottomLeft - number

if diff % (2 * loop) == 0:
    # corners
    print(2 * loop)
elif diff % loop == 0:
    print(loop)
else:
    number = diff%loop
    print diff + number #wont work everytime but works for the input
