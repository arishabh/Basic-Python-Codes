import array
counter = 0
previndex = 0
final=['Empty']*10
arr = input(str("Enter the Camel String: "))
length=len(arr)
for index in range(1,length,1):
    uni=ord(arr[index])
    if (uni>=65)&(uni<=90):
        counter = counter+1
        final[counter-1]=arr[previndex:index]      
        previndex = index   
final[counter]=arr[previndex:length]
print(final)
        
                                            
                    
        
    
