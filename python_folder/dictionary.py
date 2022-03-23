
#! Dictionaries

#? Dictionaries store data in a specific way, just like actual dictionaries you can look things up but they're not in alphabetical order.
#? They're more like lists - they store multiple values but we use { } to define our dictionaries

#* List
# my_cat = ["Salem", "black", "sassy"]

#* Dictionary
my_cat = {"name":"Salem", #* Key:Value pair is an Item
          "colour": "black",
          "mood": "sassy"  
         }

# #? Unlike lists they use key:value pairs. Basically they allow you to give each element a name
# #! Another example
# my_cat = {"name":"Salem",
#           "age": 4,
#           "hungry": True
#          }

#? Dictionaries do not have a numbered index, so we use different methods to extract or change values

print(my_cat["name"])   #*Extract the value for each key
print(my_cat["colour"])
print(my_cat["mood"])

my_cat["name"] = "Whiskers" #*Update the "name" key with the new value "Whiskers"
print(my_cat["name"])

print(my_cat.keys()) #* name, colour, mood
print(my_cat.values()) #* Salem, black, sassy
print(my_cat.items()) #* name, Salem... key + value = item. 
print(my_cat.get("name")) #* Find a value by its key. 


#! List method
#? When printing, you can tidy up the output a bit by using the list() method.

print(list(my_cat.keys()))

#? my_cat.keys - my_cat.values - my_cat.items

#! For Loops
#? Can be incorporated into For Loops as well.

for j in my_cat.keys():
    print(j)

#? my_cat.keys - my_cat.values - my_cat.items

#! .setdefault()
#? Set a new key:value using .setdefault()

my_cat.setdefault("hungry", True) #* Creates a new key and value.
#? BUT YOU CAN'T USE IT TO UPDATE AN EXISTING KEY.
my_cat.setdefault("mood", "sleepy")

#! Remove keys from dictionary
#! .pop() method

#my_cat.pop("mood") #* You must specify the ITEM you want to delete by using it's KEY.

#! del method

del my_cat["mood"] #* The keyword DEL lets you specify which key to delete.
