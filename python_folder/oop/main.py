from person import Person

liam = Person ("Liam", "30", "6'7")
liam.set_hair ("Short, brown, curly")

jordan = Person ("Jordan", "27", "5'7")
jordan.set_hair ("blonde and straight")

print (f"The innovate instructor is called {jordan.name}, he is {jordan.age} years old and is only {jordan.height}.")
print (f"Liam's hair is {liam.hair} but Jordan's hair is {jordan.hair}")

liam.get_hair()
jordan.get_hair()