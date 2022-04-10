# File: Project1.py
# Student: nusaibah siddique
# UT EID: njs2886
# Course Name: CS303E
# 
# Date: 3/7/2021
# Description of Program: Using python to build a simple utility that allows converting from English length units (miles, feet, inches) to metric lenght units (kilometers, meters, centimeters), and vice versa.



import math
import time
"""Unit Converter"""


def validate(mode):
    if mode=="1" or mode=="2" or mode=="3":
        return int(mode)
    print("\nERROR: Answer must be 1, 2 or 3. Try again.\n")
    return False


def englishToMetric():
    units = {
        "unit1": {
            1: "miles",
            2: "feet",
            3: "inches"
        },
        "unit2": {
            1: "kilometers",
            2: "meters",
            3: "centimeters"
        }
    }
    covert_chart = {
        1: {
            1: 1.609,
            2: 1609.344,
            3: 160934
        },
        2: {
            1: 0.0003048,
            2: 0.3048,
            3: 30.48
        },
        3: {
            1: 2.54,
            2: 0.0254,
            3: 2.54
        },

    }
    unit1 = False
    while unit1 == False:
        print("Select English units to convert to metric equivalent:")
        print("\tFor miles type:  1")
        print("\tFor feet type:   2")
        print("\tFor inches type: 3")
        print("\n\tChoose English units to convert (1, 2 or 3):", end=" ")
        unit1 = input()
        if unit1 in ["1", "2", "3"]:
            unit1 = int(unit1)
        else:
            unit1 = False
            print("\nERROR: Answer must be 1, 2 or 3. Try again.\n")
    unit2 = False
    while unit2 == False:
        print("Convert to which metric units:")
        print("\tFor kilometers type:  1")
        print("\tFor meters type:      2")
        print("\tFor centimeters type: 3")
        print("\n\tChoose target metric units (1, 2 or 3):", end=" ")
        unit2 = input()
        if unit2 in ["1", "2", "3"]:
            unit2 = int(unit2)
        else:
            unit2 = False
            print("\nERROR: Answer must be 1, 2 or 3. Try again.\n")
    val = False
    while val == False:
        print(
            f'Enter the number of {units["unit1"][unit1]} to convert to {units["unit2"][unit2]}:', end=' ')
        val = input()
        try:
            val = float(val)
        except Exception as e:
            val = False
            print("\nERROR: Answer must be a numeric value. Try again.\n")
    if val == 0:
        print("can not convert 0")
    else:
        result = val*covert_chart[unit1][unit2]
        print(
            f'RESULT: {val} {units["unit1"][unit1]}={result} {units["unit2"][unit2]}')


def metricToEnglish():
    units = {
        "unit1": {
            1: "kilometers",
            2: "meters",
            3: "centimeters"
        },
        "unit2": {
            1: "miles",
            2: "feet",
            3: "inches"
        }

    }
    covert_chart = {
        1: {
            1: 0.621,
            2: 3280.84,
            3: 39370.1
        },
        2: {
            1: 0.000621,
            2: 3.280,
            3: 39.3701
        },
        3: {
            1: 6.214,
            2: 0.0328,
            3: 0.394
        },

    }
    unit1 = False
    while unit1 == False:
        print("Select metric units to convert to english equivalent:")
        print("\tFor kilometers type:  1")
        print("\tFor meters type:      2")
        print("\tFor centimeters type: 3")
        print("\n\tChoose English units to convert (1, 2 or 3):", end=" ")
        unit1 = input()
        if unit1 in ["1", "2", "3"]:
            unit1 = int(unit1)
        else:
            unit1 = False
            print("\nERROR: Answer must be 1, 2 or 3. Try again.\n")
    unit2 = False
    while unit2 == False:
        print("Convert to which english units:")
        print("\tFor miles type:  1")
        print("\tFor feet type:   2")
        print("\tFor inches type: 3")
        print("\n\tChoose target metric units (1, 2 or 3):", end=" ")
        unit2 = input()
        if unit2 in ["1", "2", "3"]:
            unit2 = int(unit2)
        else:
            unit2 = False
            print("\nERROR: Answer must be 1, 2 or 3. Try again.\n")
    val = False
    while val == False:
        print(
            f'Enter the number of {units["unit1"][unit1]} to convert to {units["unit2"][unit2]}:', end=' ')
        val = input()
        try:
            val = float(val)
        except Exception as e:
            val = False
            print("\nERROR: Answer must be a numeric value. Try again.\n")
    if val == 0:
        print("can not convert 0")
    else:
        result = val*covert_chart[unit1][unit2]
        print(
            f'RESULT: {val} {units["unit1"][unit1]}={result} {units["unit2"][unit2]}')

quit = False
while(not quit):
    print("Welcome to the English/Metric conversion utility.\nThis utility allows you to convert between English units\n(miles, feet, inches) and metric units(kilometers, meters,centimeters).")
    print("\n-----------------------------------------------------------------\n")
    print("Which direction would you like to convert:")
    print("\tFor English to Metric type: 1")
    print("\tFor Metric to English type: 2")
    print("\tTo Quit type:               3\n")
    print("\tInput your answer (1, 2 or 3):", end=" ")   
    mode = input()

    while (mode!=1 or mode!=2 or mode!=3):        
        print("\nERROR: Answer must be 1, 2 or 3. Try again.\n")
        print("Which direction would you like to convert:")
        print("\tFor English to Metric type: 1")
        print("\tFor Metric to English type: 2")
        print("\tTo Quit type:               3\n")
        print("\tInput your answer (1, 2 or 3):", end=" ")   
        mode = input()
    mode = int(mode)
    
    if mode == 1:
        englishToMetric()
    elif mode == 2:
        metricToEnglish()
    elif mode == 3:
        quit = True

