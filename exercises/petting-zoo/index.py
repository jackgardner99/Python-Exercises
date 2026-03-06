# from datetime import date
from walking import Alpaca, Goat, Llama, MiniatureDonkey, MiniaturePony, Rabbit, Sheep
from slithering import CoralSnake, KingSnake, RatSnake, Python
from swimming import GoldFish, KoiFish, Mallard, Goose


miss_fuzz = Llama("Miss Fuzz", "Llama", "midday")
liam = Goat("Liam", "Goat", "morning")
olivia = Sheep("Olivia", "Sheep", "morning")
noah = MiniatureDonkey("Noah", "Miniature Donkey", "midday")
amelia = Alpaca("Amelia", "Alpaca", "midday")
oliver = Rabbit("Oliver", "Rabbit", "midday")
sophia = KingSnake("Sophia", "King Snake")
elijah = RatSnake("Elijah", "Rat Snake")
emma = CoralSnake("Emma", "Coral Snake")
mateo = Python("Mateo", "Python")
charlotte = Mallard("Charlotte", "Mallard")
levi = KoiFish("Levi", "Koi Fish")
isabella = GoldFish("Isabella", "Gold Fish")
lucas = Goose("Lucas", "Goose")
mia = MiniaturePony("Mia", "Miniature Pony", "morning")

print(f"{liam.name} the {liam.species} is available to pet during the {liam.shift} shift.")


