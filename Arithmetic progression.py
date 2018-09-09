flag=1
while flag==1:
    select = int(input("1.nth term\n2.Sum of Progression\nEnter your choice: "))
    if select==1:
        a = int(input("Enter the first term ofthe progression: "))
        n = int(input("Enter the value of n: "))
        d = int(input("Enter the common difference: "))
        u = a+(n-1)*d
        print("The nth term is: ",u)
    elif select ==2:
        a = int(input("Enter the first term ofthe progression: "))
        n = int(input("Enter the position of the last term: "))
        d = int(input("Enter the common difference: "))
        s = (n/2)*((2*a)+((n-1)*d))
        print("The sum of the progression is: ",s)
    flag = int(input("1.Use again\n2.End program\nEnter your choice"))
