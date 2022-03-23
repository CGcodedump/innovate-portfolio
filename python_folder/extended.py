
int() #creates an integer data type

float() #creates a floating point data type 

str() #creates a string data type

var = "3"           #'3'
print (type(var)) 

var = int(var)      # 3
print(type(var))

var = float(var)    # 3.0
print(type(var))

#! Truthy and Falsy
#? Falsy is an empty value, everything else is Truthy

print ("What is your name?")
name = input()

if name: #* Checks to see if "name" has a value i.e if the user has entered a name
    print(f"Hello {name}, how are you?")
else: #* If the user enters a Falsy value e.g presses enter without typing a name. 
    print(f"You didn't give me your name!")

#! Not operator

#? != operator means 'not equal to'

print (not True)  #Expected: False
print (not False) #Expected: True

bool = False

if bool != True:
    print(False)
else:
    print(True)

#! Try/Except
#? Try/Except statements have very similar syntax to if/else statements but are for catching errors without your program breaking

def add_up():
    num1 = input("What is the first number you'd like to add up?\n")
    num2 = input("What is the second number you'd like to add up?\n")
    #*The above relies on the user to input a number. Input data by default is a string.
    try: #* Try is the best case scenario - the program will run if this action can be performed
        print(f"{num1} + {num2} is {(int(num1) + int(num2))}!")
    
    except: #* ..but in the cases where it can't execute the code, we provide a seperate case using except
        print("\n ERROR: Please input only numerical values.\n")
        print("*********************\n")
        add_up()

add_up()

#! Scope - global and local variables
#? Global variables are outside of a function, exists everywhere in the code. 
#? Local variables exist inside a function only.


#! Lists and tuples 
#? Both lists and tuples are a collection of values

even_nums = [2, 4, 6, 8, 10] #* List
odd_nums = (1, 3, 5, 7, 9)   #* Tuple
#? Lists vs Tuples
#? Mutable vs immutable
#? Changeable vs unchangeable

even_nums = [2, 4, 6, 8, 10] #* List
even_nums.append(12)
even_nums.insert(0,0)

#? Lists have multiple built-in methods to change the values they hold

odd_nums = (1, 3, 5, 7, 9)   #* Tuple
odd_nums.remove(1)
odd_nums.pop()

#? Tuples do not have any methods to change the values they hold.

#*So why a list or why a tuple.

#? Lists can handle their values being changed, inserted or deleted as part of your program-tuples cannot
#?that means tuples are stricter - they act more like constants with room for accidental errors.

#! While True
#? While loop syntax to get a program to run forever
#? but this can be dangerous - you might have to kill your terminal to get it to stop.

#while True:
#   print("Run forever")

#? Remember how Truthy works, this while loop will always run with the condition being true
#? but we can create a condition to make it false.

loop_runs = True #* Creates a boolean to set the loop off.

while loop_runs: #* Equivalent to while loop runs == True. True is Truthy so no value needs to be specified.
    print ("Run the loop!") #* The loop performs its task
    #Do something...

    #to stop the loop
    loop_runs = False #* changing the variable to false breaks the loop

#! While loops - break and continue

#?while program_is_running:
#?    if condition_is_met
#?        continue          #Continue with whatever the program's job is
#?    else:
#?        break             #Otherwise stop.

#? Continue and break are key words that can be used to manually stop or resume the job you've set your while loop to do.