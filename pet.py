class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks 
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy +=25
        print("tiered Boss", "Health:", self.health, "Energy:", self.energy)
        return self

    def eat(self):
        if self.health >= 100:
            print("all good not hungry Boss")
        else:
            self.energy +=5
            self.health +=10
            print("yummy meal Boss", "Health:", self.health, "Energy:", self.energy)
        return self

    def play(self):
        self.energy -=10
        self.health +=5
        print("good times Boss", "Health:", self.health, "Energy:", self.energy)
        return self
        
    def noise(self):
        print("thanks for the bath boss", "Health:", self.health, "Energy:", self.energy)
        return self

