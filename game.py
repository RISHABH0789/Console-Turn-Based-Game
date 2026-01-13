import random

class Character:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def attack(self,other):
        power = random.randint(1,10)
        other.health -= power
    def heal(self,other):
        if self.health == 100:
            print("FULL HEALTH!")
            other.attack(self)
        else:
            self.health += random.randint(10,20)
            if self.health > 100:
                self.health = 100
    def block(self,other):
        chance = random.randint(0,1)
        if chance == 0:
            self.health = self.health
        else:
            print("CANNOT BLOCK THIS ATTACK")
            other.attack(self)
    def status(self):
        print(f"{self.name}'s Health: {self.health}")

player = Character("PLAYER",100)
enemy = Character("ENEMY",100)

game = True
while game:
    print("ATTACK[A]    BLOCK[B]    HEAL[H]")
    decision = input().lower()
    
    if decision == "a":
        player.attack(enemy)
        enemy.attack(player)
        player.status()
        enemy.status()
    elif decision == "b":
        player.block(enemy)
        player.status()
        enemy.status()
    elif decision == "h":
        player.heal(enemy)
        player.status()
        enemy.status()
    else:
        print("Inappropriate Decision")
        enemy.attack(player)
        player.status()
        enemy.status()
    
    if player.health <= 0 and enemy.health <= 0:
        print("It's TIE!")
        game = False
    elif player.health <= 0:
        print("You LOSE!")
        game = False
    elif  enemy.health <= 0:
        print("You WON!")
        game = False