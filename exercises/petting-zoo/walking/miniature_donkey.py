from datetime import date

class MiniatureDonkey:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True