Dictionary={}
Dictionary["Menon"]=14
Dictionary['Tonmoy']=17
Dictionary['Naved']=0
print(Dictionary)

Dict={}

try:
    barcode=input("Input barcode: ")
    print (Dictionary[barcode])

except:
    print("Error 404! Barode not found")
