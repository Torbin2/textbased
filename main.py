import random

print("input help for commands")

spawned = False
xp = 1
level = 1 

def user_input(minhp ,maxhp):
  player_input = input("input = ")
  
  global xp
  global spawned
  global mhp
  global bmhp

  if player_input == "help" :
    print("type f to find a (new) monster \ntype a to atack")
  
  elif player_input == "f" :
    mhp = random.randint(minhp, maxhp)
    bmhp = mhp
    spawned = True
    print(f"\na slime apeared {mhp}/{bmhp}")

  elif player_input == "a" :
    if spawned == False :
      print("spawn a monster first")
      return
    dmg = xp
    mhp -= dmg
    if mhp <= 0:
      xp += 1
      print(f"the slime is dead \nxp = {xp}")
      spawned = False
      return
    print(f"the slime has {mhp}/{bmhp}")

while level == 1 :
  user_input(1,10)