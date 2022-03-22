var = "Activity 1 is complete"
var_length = len(var)

def activity_one():
    if (var_length % 2) == 0:
        print (f"{var} is {var_length} characters long. An even number.")
    else:
        print ("The string isn't even.")

activity_one()

alphabet = ["Invalid option",
"A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"P",
"Q",
"R",
"S",
"T",
"U",
"V",
"W",
"X",
"Y",
"Z"
]

def activity_two():
    user_input = int(input("Pick a letter between 1 and 26\n"))
    print (alphabet[user_input])

activity_two()