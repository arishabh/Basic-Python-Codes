flag1 = 1
while flag1==1:
    def f_to_i(feet):
        feet = float(input("Enter the number of feet: "))
        inch = feet*12
        print("inch =",inch)
    def i_to_f(inch):
        inch = float(input("Enter the number of inch: "))
        feet = inch/12
        print("feet =",feet)
    flag = 1
    feet = 0
    inch = 0
    while(flag==1):
        choice = int(input("1.Convert feet to inches?\n2.Convert inches to feet?\nEnter your choice: "))
        if choice==1:
            f_to_i(feet)
            flag = 0
        elif choice==2:
            i_to_f(inch)
            flag = 0
        else:
            print("Invalid choice, please re-enter in numbers only")
            flag = 1
    choice1=int(input("1.End program\n2.Restart program\nEnter your choice: "))
    if choice1==2:
        print("--------------------Restarting Program-----------------------")
        flag1 = 1
    else:
        print("--------------------Ending Program---------------------------")
        flag1 = 0
        
