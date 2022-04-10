print("\nWelcome to the English/Metric conversion utility.\n\nThis utility allows you to convert between English units \n(miles, feet, inches) and metric units (kilometers, meters, \ncentimeters).")
print("\n------------------------------------------------------------\n")

Input = int(1)

while (Input!="3"):
    print("Which direction would you like to convert:")
    print("\tFor English to Metric type: 1")
    print("\tFor Metric to English type: 2")
    print("\tTo Quit type:               3")

    Input = input("Input your answer (1, 2 or 3): ")
    print(" ")

    while (Input=="1"):
        print("Select English units to convert to metric equivalent:")
        print("\tFor miles type:  1")
        print("\tFor feet type:   2")
        print("\tFor inches type: 3")
        To = input("\n\tChoose English units to convert (1, 2 or 3): ")
        if (To!="1" or To!="2" or To!="3"):
            print("\nERROR: Answer must be 1, 2 or 3. Try again.\n")
            continue
        
        print("Convert to which metric units:")
        print("\tFor kilometers type:  1")
        print("\tFor meters type:      2")
        print("\tFor centimeters type: 3")
        From = input("\n\tChoose target metric units (1, 2 or 3): ")
        
        
    while (Input=="2"):
        pass
    while (Input=="3"):
        pass
    if (Input!="1" or Input!="2" or Input!="3"):
        print("ERROR: Answer must be 1, 2 or 3. Try again.")
        continue
