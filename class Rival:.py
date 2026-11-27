class Rival:
    life = 3
    def attack(self):
        print("Ouch!")
        self.life -=1
    def checkLife(self):
        if self.life <= 0:
            print("You won!")
        else:
            print(self.life)
thanos = Rival()
magneto = Rival() 
thanos.checkLife()
thanos.attack() 
thanos.attack() 
thanos.attack() 
thanos.checkLife()
magneto.attack()
magneto.attack()
magneto.attack()
magneto.checkLife()