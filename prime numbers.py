flag1 = 1
for x in range (2,101):
    for y in range (2,10):
        if x!=y:
            if x%y == 0:
                flag1 = 0
    if flag1 == 1:
        print(x)
    flag1 = 1
    
        
    
