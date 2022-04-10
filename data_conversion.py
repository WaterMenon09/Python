for i in range (100):
    print("""Do you want to convert
    a. Binary to denary, or
    b. Denary to binary, or
    c. Denary to hexadecimal?""")
    choice=input("Type the corresponding letter to your choice: ")

    if choice=="a" or choice=="A":
        value=(input("Input the binary value you wish to convert: ")) 
        if len(value)==8:
            a=int(value[7])
            b=int(value[6])
            c=int(value[5])
            d=int(value[4])
            
            e=int(value[3])
            f=int(value[2])
            g=int(value[1])
            h=int(value[0])
            output=(1*a + 2*b + 4*c + 8*d + 16*e + 32*f + 64*g + 128*h)
            print("The converted denary value is", output)
        else:
            print("You have to input an exact of 8 digits or 1 byte.")

    elif choice=="b" or choice=="B":     #ROTATED THE ENTIRE THING!!!#
        binary=[]
        value=int(input("Input the denary value you wish to convert: "))
        if value!=0:        
            while value!=1:
                mod=value%2
                value=value//2
                binary.append(mod)
            binary.append(1)
            while len(binary)<8:
                binary.append(0)
            binary.reverse()    #reversed here#
            print('The converted binary value is',binary)
            print(' ')
        else:
            binary.append(0)
            print('The converted binary value is', binary)
            print(' ')

    elif choice=="c" or choice=="C":
                                        #Denary to hexadecimal
        value=int(input("Input the denary you wish to convert: "))
        hexa=[]
        if value>=16:
            mod=value%16
            value=value//16
            hexa.append(value)
            if mod==10:
                hexa.append('A')
            elif mod<10:
                hexa.append(mod)
            elif mod==11:
                hexa.append('B')
            elif mod==12:
                hexa.append('C')
            elif mod==13:
                hexa.append('D')
            elif mod==14:
                hexa.append('E')
            else:
                hexa.append('F')
                
        elif value<10:
            hexa.append(value)

        elif value==10:
            hexa.append("A")
        elif value==11:
            hexa.append('B')
        elif value==12:
            hexa.append('C')
        elif value==13:
            hexa.append('D')
        elif value==14:
            hexa.append('E')
        else:
            hexa.append('F')

        print("The converted hexadecimal value is:", hexa)

    elif choice=="x" or choice=="X":
        break
        
    else:
        print("Please read the instructions and start over.")
    print(' ')
    print("Press 'X' to exit the loop.")
    print(' ')
