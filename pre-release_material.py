def work():

    count=int(0)
    total_price=int(0)
    price=int(0)
    
    weight = float(input("Input weight: "))
    dimention1 = float(input("Input first dimention of size: "))
    dimention2 = float(input("Input second dimention of size: "))
    dimention3 = float(input("Input third dimention of size: "))
    print(" ")
    total_d= (dimention1 + dimention2 + dimention3)
    
    if ((dimention1 > 80) or (dimention2 > 80) or (dimention3 > 80)):
        print("Error! The dimentions of the package must be smaller than 80cm.")
        regect+=1
        print("No. of parcel:", parcel)
        print("Price", price)
        print("Total price", total_price)
        print("No. of rejects", regect)
        print(" ")
        
    elif total_d >=200:
        print("Error! The sum of the three dimentions must be smaller than 200cm.")
        regect+=1
        print("No. of parcel:", parcel)
        print("Price", price)
        print("Total price", total_price)
        print("No. of rejects", regect)
        print(" ")
         
    else:
        count=count+1
        if (weight <= 5):
            price=10
            total_price+=price
            print("No. of parcel:", parcel)
            print("Price", price)
            print("Total price", total_price)
            print("No. of rejects", regect)
            print(" ")
            
        else:
            xtra=weight-5
            price = 10 + xtra * 1
            total_price+=price
            print("No. of parcel:", parcel)
            print("Price", price)
            print("Total price", total_price)
            print("No. of rejects", regect)
            print(" ")
            
z=int(0)

while z!=0:
    work()
