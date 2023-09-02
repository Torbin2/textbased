import os
import random
import json

cheese = 0
spawned = False
skilpoints = 0
level = 1
maxplayerhp = 20
playerhp = 20
dodge_chance = 5
dead = False
player_level = 1
damage = 1

print("input help for commands")

def user_input(minhp ,maxhp):
  player_input = input("\ninput = ")
  
  global skilpoints
  global spawned
  global mhp
  global bmhp
  global cheese
  global playerhp
  global maxplayerhp
  global damage

  if player_input == "help" :
    print("type f to find a (new) monster \ntype a to atack\ntype h to heal using cheese\ntype i to check player info`")
    print("type s to assign skilpoints\ntype 'save' to save\ntype 'load' to load any prevous saved games stats")
  
  elif player_input == "test":
    print("no test!")

  elif player_input == "save":
    save_config()
  elif player_input == "load":
    load_config()
  elif player_input == "i":
    print(f"{playerhp}/{maxplayerhp} health\n{skilpoints} skilpoints\n{cheese} cheese\n{dodge_chance}/10 dodge chance (lower is better)")

  elif player_input == "f" :
    spawnrng = random.randint(1,20)
    if spawnrng <= 10:
      mhp = random.randint(minhp, maxhp)
      bmhp = mhp
      spawned = True
      print(f"a slime apeared with {mhp}/{bmhp} health")
    
    if spawnrng >= 11 and spawnrng <= 19:
      cheese += 1
      print(f"you found a piece cheese, you have {cheese}")
    if spawnrng == 20:
      cheese += 3
      print(f"you found a lot of cheese, you have {cheese}")
      
  elif player_input == "a" :
    if spawned == False :
      print("spawn a monster first")
      return
    mhp -= damage
    if mhp <= 0:
      skilpoints += 1
      print(f"the slime is dead \nxp = {skilpoints}")
      spawned = False
      return
    print(f"the slime has {mhp}/{bmhp} health")
    enemy_hit()

  elif player_input == "h":
    if cheese == 0 and playerhp == maxplayerhp:
      print("insufficient cheese and already at full health")
    elif cheese == 0:
      print("insufficient cheese")
    elif playerhp == maxplayerhp:
      print("already at full health")
    elif cheese >= 1:
      healing_amount = random.randint(2,3)
      playerhp += healing_amount
      cheese -= 1
      if playerhp > maxplayerhp:
        healthcheck = playerhp - maxplayerhp
        healing_amount = healing_amount - healthcheck
        playerhp = maxplayerhp
      print(f"you healed {healing_amount} hp\ntotal hp = {playerhp}")
 
  elif player_input == "s":
    stats()

  else :
    print("invalid input")

def stats():
  
  global skilpoints
  global player_level
  global damage
  global maxplayerhp

  print("increase damage/max health whith 'd' and 'h'")
  while skilpoints >= 1:
    upgrade = input("upgrade ")
    if upgrade == "d":
      upgrades = int(input(f"choose amount of upgrades (you have {skilpoints} skillpoints) "))
      if upgrades > skilpoints :
        print("invalid amount")
      if upgrades <= skilpoints:
        damage += upgrades
        skilpoints-= upgrades
        print(f"you now deal {damage} damage")
    elif upgrade == "h":
      upgrades = int(input(f"choose amount of upgrades (you have {skilpoints} skillpoints) "))
      if upgrades > skilpoints :
        print("invalid amount")
      elif upgrades <= skilpoints:
          maxplayerhp += upgrades
          skilpoints-= upgrades
          print(f"your max health is now {maxplayerhp}")
    else :
      print("increase damage/max health whith 'd' and 'h'")

def enemy_hit():
  
  global dodge_chance
  global playerhp
  global dead

  damage_rng = random.randint(1,10)
  if damage_rng > dodge_chance:
    
    if 0 <= dodge_chance <= 3:
      print("enemy atack easily dodged")
    elif 4 <= dodge_chance <= 7:
      print("enemy atack dodged")
    elif 8 <= dodge_chance <= 11:
      print("enemy atack barely dodged")
    dodge_chance += 1
  
  elif damage_rng <= dodge_chance:
    
    if 0 <= dodge_chance <= 3:
      print("enemy atack barely hit")
    elif 4 <= dodge_chance <= 7:
      print("enemy atack hit")
    elif 8 <= dodge_chance <= 11:
      print("enemy atack easily hit")
   
    dodge_chance -= 1
    playerhp -= 1
    if playerhp <= 0:
      dead = True
      return
    print(f"you have {playerhp} health")

def save_config():

  global cheese
  global skilpoints
  global level
  global maxplayerhp
  global playerhp
  global dodge_chance
  global player_level 
  global damage 


  with open("config.json", 'w') as file:
    json.dump({
      "cheese": cheese,
      "skilpoints": skilpoints,
      "level" : level,
     "maxplayerhp" : maxplayerhp,
      "playerhp"  : playerhp,
     "dodge_chance" : dodge_chance,
      "player_level" : player_level,
      "damage" : damage
    }, file)

def load_config():

  global cheese
  global skilpoints
  global level
  global maxplayerhp
  global playerhp
  global dodge_chance
  global player_level 
  global damage 

  if "config.json" not in os.listdir("."):
    save_config()
    return
  
  with open("config.json", "r") as file:
    try:
      data: dict = json.load(file)

      cheese = data["cheese"]
      skilpoints = data["skilpoints"]
      level = data["level"]
      maxplayerhp = data["maxplayerhp"]
      playerhp = data["playerhp"]
      dodge_chance = data["dodge_chance"]
      player_level = data["player_level"]
      damage = data["damage"]
    except Exception as e:
      print(str(e))


while level == 1 :
  user_input(1,10)
  if skilpoints >= 5:
    level = 2
  if dead == True:
    print("your dead")
while level == 2:
  user_input(10,30)
  if dead == True:
    print("your dead")
