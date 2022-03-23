
#? OOP Activity

class Character():
    def __init__(self, real_name, superhero_name, active_city, affiliations):
        self.realname = real_name
        self.superheroname = superhero_name
        self.city = active_city
        self.team = affiliations
    
    def set_powers(self, hero_powers, weaknesses):
        self.powers = hero_powers
        self.weakness = weaknesses

    def get_powers(self):
        print(f"Real name: {self.realname}\nSuperhero ID: {self.superheroname}\nAO: {self.city}\nOrganisation: {self.team}")
        print (f"Known Powers: {self.powers}\nKnown Weaknesses: {self.weakness}")