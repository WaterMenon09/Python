count=int(0)
total_price=int(0)
price=int(0)
regect=int(0)
while True:
        
        weight=int(0)
        print("To finsih press '-1'")
        weight = float(input("Input weight: "))
        if weight==-1:
            print("The number of parcels are:", count)
            print("The total price is:", total_price)
            print("The total number of rejected parcels are", regect)
            break
        elif (weight<1):
            print("Error! The weight must be between 1 to 10 kgs.")
            regect+=1
            print("No. of rejects", regect)
            print(" ")
        elif (weight>10):
            print("Error! The weight must be between 1 to 10 kgs.")
            regect+=1
            print("No. of rejects", regect)
            print(" ")
            
        else:
            dimention1 = float(input("Input first dimention of size: "))
            dimention2 = float(input("Input second dimention of size: "))
            dimention3 = float(input("Input third dimention of size: "))
            print(" ")
            total_d= (dimention1 + dimention2 + dimention3)
            
            if ((dimention1 > 80) or (dimention2 > 80) or (dimention3 > 80)):
                print("Error! The dimentions of the package must be smaller than 80cm.")
                regect+=1
                print("No. of rejects", regect)
                print(" ")

            elif total_d >=200:
                print("Error! The sum of the three dimentions of the package must be smaller than 200cm.")
                regect+=1
                print("No. of rejects", regect)
                print(" ")
                 
            else:
                count+=1
                if (weight <= 5):
                    price=10
                    total_price+=price
                    print("Price", price)
                    print(" ")
                    
                else:
                    xtra=weight-5
                    price = 10 + xtra * 1
                    total_price+=price
                    print("Price", price)
                    print(" ")
