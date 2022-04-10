#Less Do DIs!
dictionary={}
prices={}

def read(file_name):
    file=open(file_name + ".txt","r")
    print("\n \n")
    for line in file:
        print(line)
    file.close()

def entries():    
    Entry=int(input("Enter the number of different items you wish to purchase: "))
    for i in range (Entry):
        barcode=input("Enter barcode: ")
        try:
            if dictionary[barcode]==0:
                print("We're out of that item! Order more")
            elif dictionary[barcode]<=6:
                print("Running low on",barcode)
                print("Order more")
                number=int(input("Enter how many you wish to purchase: "))
                a=dictionary[barcode]          
                if a>=int(number):                                                                           
                    #Subtracting the barcode from the dictionary                            
                    dictionary[barcode]=(dictionary[barcode]-number)                          
                    for i in range (number):                                                               
                        file.write(barcode)                                                                    
                        file.write("\t \t \t")                                                             
                        file.write(str(prices[barcode]))                                      
                        file.write("\n")                                                                     
            else:
                number=int(input("Enter how many you wish to purchase: "))                
                if dictionary[barcode]>=(number):
                    #Subtracting the barcode from the dictionary 
                    dictionary[barcode]=(dictionary[barcode]-number)
                    for i in range (number):                        
                        file.write(barcode)
                        file.write("\t \t \t")
                        file.write(str(prices[barcode]))
                        file.write("\n")
                else:
                    print("Sorry there aren't that many instock.")         
        except:
            print("Incorrect barcode entered. That barcode is not saved in the dictionary.")
    file.close()

        #Actual Program starts from here#
while True:
    imput=input("""Press the corresponding values to start the task.
1. Open a new file.
2. Open an existing file.
3. Read an existing file.
dict. To update the dictionary.
close. Stop the loop.
: """)
    if imput=="1":
        #write
        file_name=input("Enter the name of the file that you wish to create: ")
        file=open(file_name + ".txt","w")
        file.write("Barcode \t  \t \t Price \n")
        entries()        

    elif imput=="2":
        #append
        
        file_name=input("Enter the name of the file that you wish to append: ")
        file=open(file_name + ".txt","a")
        entries()        

    elif imput=="3":
        #read
        file_name=input("Enter the name of the text file you wish to read: ")
        read(file_name)

    elif imput=="close" or imput=="CLOSE" or imput=="Close":
        break

    elif imput=='dict' or imput=='Dict' or imput=='DICT':
        barcode=input("Enter the barcode of the item you wish to store: ")
        number=int(input('Enter the quantity you wish to store: '))
        price=int(input("Enter the price of the item: "))
        dictionary[barcode]=number
        prices[barcode]=price
    
    else:
        print("Wrong input inserted! Read the instructions properly and start over.")
    print(" ")

print(dictionary)
