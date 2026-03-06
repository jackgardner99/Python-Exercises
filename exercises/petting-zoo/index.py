# from datetime import date
from walking import Alpaca, Goat, Llama, MiniatureDonkey, MiniaturePony, Rabbit, Sheep
from slithering import CoralSnake, KingSnake, RatSnake, Python
from swimming import GoldFish, KoiFish, Mallard, Goose


miss_fuzz = Llama("Miss Fuzz", "Llama", "midday", "llama chow")
liam = Goat("Liam", "Goat", "morning", "goat chow")
olivia = Sheep("Olivia", "Sheep", "morning", "sheep chow")
noah = MiniatureDonkey("Noah", "Miniature Donkey", "midday", "grass")
amelia = Alpaca("Amelia", "Alpaca", "midday", "grass")
oliver = Rabbit("Oliver", "Rabbit", "midday", "rabbit chow")
sophia = KingSnake("Sophia", "King Snake", "rats")
elijah = RatSnake("Elijah", "Rat Snake", "rats")
emma = CoralSnake("Emma", "Coral Snake", "rats")
mateo = Python("Mateo", "Python", "rats")
charlotte = Mallard("Charlotte", "Mallard", "minnows")
levi = KoiFish("Levi", "Koi Fish", "chow")
isabella = GoldFish("Isabella", "Gold Fish", "chow")
lucas = Goose("Lucas", "Goose", "minnows")
mia = MiniaturePony("Mia", "Miniature Pony", "morning", "grass")

print(f"{liam.name} the {liam.species} is available to pet during the {liam.shift} shift.")
amelia.feed()

print(olivia)