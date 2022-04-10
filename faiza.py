lane1 = float(input("Enter time for lane 1 (seconds) : "))
lane2 = float(input("Enter time for lane 2 (seconds) : "))
lane3 = float(input("Enter time for lane 3 (seconds) : "))
flag = False

if (lane1<lane2 and lane1<lane3):
    if (lane2<lane3):
        print("Gold:\t lane 1\nSilver:\t lane 2\nBronze:\t lane 3")
        if ((lane3-lane1)/lane3 > 0.1):
            print("Drug test required!")
    else:
        print("Gold:\t lane 1\nSilver:\t lane 3\nBronze:\t lane 2")
        if ((lane2-lane1)/lane2 > 0.1):
            print("Drug test required!")
elif (lane2<lane1 and lane2<lane3):
    if (lane1<lane3):
        print("Gold:\t lane 2\nSilver:\t lane 1\nBronze:\t lane 3")
        if ((lane3-lane2)/lane3 > 0.1):
            print("Drug test required!")
    else:
        print("Gold:\t lane 2\nSilver:\t lane 3\nBronze:\t lane 1")
        if ((lane1-lane2)/lane1 > 0.1):
            print("Drug test required!")
else:
    if (lane1<lane2):
        print("Gold:\t lane 3\nSilver:\t lane 1\nBronze:\t lane 2")
        if ((lane2-lane3)/lane2 > 0.1):
            print("Drug test required!")
    else:
        print("Gold:\t lane 3\nSilver:\t lane 2\nBronze:\t lane 1")
        if ((lane1-lane3)/lane1 > 0.1):
            print("Drug test required!")

