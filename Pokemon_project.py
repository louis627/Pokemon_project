#This project is aiming to create a pokemon game where the user can have his own pokemons and they can attcak the others'

class Pokemon:

  def __init__(self, name, level, p_type):
    self.name = name
    self.level = level
    self.p_type = p_type
    self.maxium_health = level*5
    self.current_health = level*5
    self.knocked_out = False

  def __repr__(self):
    return "This level {level} {name} has {health} hit points remaining. They are a {type} type Pokemon".format(level = self.level, name = self.name, health=self.current_health, type = self.p_type)


  def knock_out(self):
    self.knocked_out = True
    if self.current_health != 0:
      self.current_health = 0
      print("Your {name} pokemon is knocked out".format(name=self.name))

  def lose_health(self, lost_value):
    m=self.current_health-lost_value
    if m>0:
      print("{name} now has {value} health ".format(name=self.name, value=m))
    else:
      self.current_health =0
      self.knock_out()

  def regain_health(self, amount):
    n=self.current_health + amount
    if n < self.maxium_health:
      print("{name} now has {value} health ".format(name=self.name, value=n))
    else:
      print("{name} now has {value} health ".format(name=self.name, value=self.maxium_health))

  def revive(self):
    self.knocked_out = False
    if self.health ==0:
      self.health =1
    print(" The {name} is reviving now with the health of {x}". format(name=self.name, x=self.maxium_health))


  def attack(self, other):
    if (self.p_type =="Fire" and other.p_type =="Grass") or (self.p_type =="Water" and other.p_type =="Fire") or (self.p_type =="Grass" and other.p_type =="Water"):
      print("{name} can make {twice} damage to the {other_name} ".format(name=self.name, twice=self.level*2, other_name=other.name))
      other.lose_health(2*self.level)


    elif (self.p_type =="Fire" and other.p_type =="Water") or (self.p_type =="Water" and other.p_type =="Grass") or (self.p_type =="Grass" and other.p_type =="Fire"):
      print("{name} can make {half} damage to the {other_name} ".format(name=self.name, half=0.5* self.level, other_name=other.name))
      other.lose_health(0.5* self.level)

# If the pokemon attacking has neither advantage or disadvantage, then it deals damage equal to its level to the other pokemon
    elif (self.p_type == other_pokemon.p_type):
        print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level))
        other_pokemon.lose_health(self.level)

class Trainer:
#"""A trainer has a list of pokemon, a number of potions and a name. When the trainer gets created, the first pokemon in their list of pokemons is the active pokemon (number 0)"""
  def __init__(self, list_of_pokemon, trainer_name, number_of_potition):
    self.list_of_pokemon = list_of_pokemon #"""contain list of class Pokemon function [a,b,c] a=Pokemon("Charmander", 5, "Fire",)...
    self.trainer_name = trainer_name
    self.number_of_potition = number_of_potition
    self.current_act_pokemon = 0 #start from the first pokemon in the list and then can use the switch function to change the current pokemon.
  def __repr__(self):
    print("The trainer {name} now has the following pokemon:".format(name=self.trainer_name))
    for m in self.list_of_pokemon:
      print (m)
    return "The current active pokemon is {name}".format(name = self.list_of_pokemon[self.current_act_pokemon].name)

#change the current pokemon to the new active one, new_active is the index of the pokemon in the list
  def switch_pokemon(self, new_active):
    if new_active < len(self.list_of_pokemon) and new_active >=0:
      if self.list_of_pokemon[new_active].knocked_out == True:
        print("your {name} pokemon is knocked out.".format(name={self.list_of_pokemon[new_active].name}))
      elif new_active == self.current_act_pokemon:
        print("You are on your current pokemon")
      else:
        self.current_act_pokemon = new_active
        print("{name},now it is your turn".format(name=self.list_of_pokemon[self.current_act_pokemon].name))

  def potion(self):
    if self.number_of_potition >0:
      # a potition gain 20
      self.list_of_pokemon[self.current_act_pokemon].regain_health(20)
      self.number_of_potition -= 1
      print("You used potition on {name}".format(name=self.list_of_pokemon[self.current_act_pokemon].name))
    else:
       print("you don't have any potition")

  def attack_other_trainer(self, other_trainer):
    my_pokemon=self.list_of_pokemon[self.current_act_pokemon]
    other_pokemon=other_trainer.list_of_pokemon[other_trainer.current_act_pokemon]
    my_pokemon.attack(other_pokemon)

# Six pokemon are made with different levels. (If no level is given, it is level 5)
a = Pokemon("Charmander", 7, "Fire")
b = Pokemon("Squirtle", 5, "Water")
c = Pokemon("Squirtle", 1, "Water")
d = Pokemon("Bulbasaur", 10, "Grass")
e = Pokemon("Charmander", 5, "Fire")
f = Pokemon("Squirtle", 2, "Water")


#Two trainers are created. The first three pokemon are given to trainer 1, the second three are given to trainer 2.
trainer_one = Trainer([a,b,c], "Alex", 3)
trainer_two = Trainer([d,e,f], "Sara", 5)

# print(trainer_one)
# print(trainer_two)

# Testing attacking, giving potions, and switching pokemon.
trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one)
trainer_two.potion( )
trainer_one.attack_other_trainer(trainer_two)
trainer_two.switch_pokemon(0)
trainer_two.switch_pokemon(1)
