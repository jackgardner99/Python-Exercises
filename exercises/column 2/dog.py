class Dog:
    species = "Canis Familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    # another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    
class JackRussellTerrior(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

    
miles = JackRussellTerrior("Miles", 6)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
charlotte = GoldenRetriever("Charlotte", 2)

print(miles.speak())
print(buddy.speak("Yap"))
print(jim.speak("Woof"))
print(jack.speak("Woof"))
print(charlotte.speak())