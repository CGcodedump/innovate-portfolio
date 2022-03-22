# greeting = "Hello World"

# print(greeting)

# string = "This is text"
# boolean = True or False
# integer = 12345
# floating_point = 123.45

# greeting = "hello world"
# print (len(greeting))
# print (greeting[1])
# print (greeting.upper())
# print (greeting.title())
# print (greeting.capitalize())

# import random
# #import random as rd - changes the name of the random function
# var = random.random()

# my_greeting = "Hello"
# my_message = "How are you?"

# #concatenation
# print (my_greeting + my_message) 

# #interpolation
# print (f"{my_greeting} there, nice to meet you")

# char_name = input("Welcome, what is your name?\n")
# print(f"Welcome {char_name}, it's nice to meet you")

# def cash_machine(amount,account):
#     print(f"Withdrawing £{amount} from account {account}")

# cash_machine(100, 50606051243)

# fruit = ["Apple",
#         "Pear",
#         "Peach",
#         "Banana",
#         "Strawberry"
#     ]

# print (fruit[2])
# fruit[2] = "Orange"
# print (fruit)

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

