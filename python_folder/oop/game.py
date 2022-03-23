
#? OOP Activity

from character import Character

superman = Character ("Clarke Kent", "Superman", "Metropolis", "The Justice League")
superman.set_powers ("Too many", "Kryptonite, Magic")

theflash = Character ("Wally West", "The Flash", "Central City", "The Justice League")
theflash.set_powers ("Super Speed", "Psionics")

batman = Character ("Bruce Wayne", "Batman", "Gotham", "The Justice League")
batman.set_powers ("Genius, wide array of gadgets, expert martial artist", "Just a normal human")

superman.get_powers()
print("------------------")
theflash.get_powers()
print("------------------")
batman.get_powers()