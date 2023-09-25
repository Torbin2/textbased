import os
import random
import json

cheese = 0
spawned = False
skillpoints = 0
stage_difficulty = 1
maxplayerhp = 20
playerhp = 20
dodge_chance = 5
dead = False
player_level = 0
damage = 1
game_on = True
exp = 0
cheese_mode = False

textbased_logo = """
       /\\ 
      /  \\
     /    \\
    /      \\
   /   _    \\
  /   / \\    \\
 /   /   \\    \\
/___/_____\\____\\
\\   \\   /    /
 \\   \\ /    /
  \\   /    /
   \\ /    /
    \\    /
     \\  /
      \\/
"""

print(textbased_logo)

print("input help for commands")

def user_input():
  player_input = input("\ninput = ")
  
  global skillpoints
  global spawned
  global mhp
  global bmhp
  global cheese
  global playerhp
  global maxplayerhp
  global damage
  global exp
  global exp_requirement
  global stage_difficulty
  global cheese_mode
  global dodge_chance
  global dead

  if player_input == "help" :
    print("type f to find a (new) monster \ntype a to atack\ntype h to heal using cheese\ntype i to check player info`")
    print("type s to assign skillpoints\ntype 'save' to save\ntype 'load' to load any prevous saved games stats")
    print("type 't' to travel to a place with harder enemies")
    print("type 'cheese' to enter cheese mode")
  elif player_input == "test":
    print("yes                                   no")
  elif player_input == "cheese":
    cheese_mode = not cheese_mode
  elif player_input == "save":
    save_config()
  elif player_input == "load":
    load_config()
    cheese_mode = False
  elif player_input == "i":
    if cheese_mode == True:
      print("your in cheesemode")
      return
    print(f"{playerhp}/{maxplayerhp} health\n{skillpoints} skillpoints\n{cheese} cheese\n{dodge_chance}/10 dodge chance (lower is better)")
    print(f"level {player_level}\ndmg {damage}\n{exp}/{exp_requirement} exp")
  elif player_input == "f" :
    if cheese_mode == True:
      cheese += 1
      print(f"you found a piece cheese, you have {cheese}")
      playerhp -= 1
      dodge_chance +=1
      if playerhp <= 0:
        dead = True
        return
      return
    spawning(stage_difficulty,3*stage_difficulty)
  elif player_input == "a" :
    if spawned == False :
      print("spawn a monster first")
      return
    mhp -= damage
    if mhp <= 0:
      exp += stage_difficulty * random.randint(1,3)
      print(f"the slime is dead \n{exp}/{exp_requirement} exp to next level")
      spawned = False
      return
    print(f"the slime has {mhp}/{bmhp} health")
    enemy_hit()

  elif player_input == "h":
    if cheese_mode == True:
      print("your in cheesemode")
      return
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
    print(f"{cheese} cheese")
 
  elif player_input == "s":
    stats()

  elif player_input == "t":
    try :
     stage_difficulty = int(input("stage difficulty = "))    
    except ValueError:
      print("thats not a int")
      return
    print(f"travaling to biome {stage_difficulty}")

  else :
    print("invalid input")

def stats():
  
  global skillpoints
  global player_level
  global damage
  global maxplayerhp

  print("increase damage/max health whith 'd' and 'h'")
  if skillpoints >= 1:
    upgrade = input("upgrade ")
    if upgrade == "d":
      upgrades = int(input(f"choose amount of upgrades (you have {skillpoints} skillpoints) "))
      if upgrades > skillpoints :
        print("invalid amount")
      if upgrades <= skillpoints:
        damage += upgrades
        skillpoints-= upgrades
        print(f"you now deal {damage} damage")
    elif upgrade == "h":
      upgrades = int(input(f"choose amount of upgrades (you have {skillpoints} skillpoints) "))
      if upgrades > skillpoints :
        print("invalid amount")
      elif upgrades <= skillpoints:
        for i in range(upgrades):
          maxplayerhp += maxplayerhp
          skillpoints-= upgrades
          print(f"your max health is now {maxplayerhp}")
    else :
      print("increase damage/max health whith 'd' and 'h'")
  else :
    print("no skillpoints")

def spawning(minhp,maxhp):
  global cheese
  global spawned
  global mhp
  global bmhp
  if spawned == True:
      print("the slime tried to atack you")
      run = random.randint(1,2)
      if run == 1:
        print("you got away")
        spawned = False
        return
      if run == 2:
        print("you didn't get away")
        enemy_hit()
        return
  spawnrng = random.randint(1,20)
  if spawnrng <= 14:
    mhp = random.randint(minhp, maxhp)
    bmhp = mhp
    spawned = True
    print(f"a slime apeared with {mhp}/{bmhp} health")
    
  if spawnrng >= 15 and spawnrng <= 19:
    cheese += 1
    print(f"you found a piece cheese, you have {cheese}")
  if spawnrng == 20:
    cheese += 7
    print(f"you found a lot of cheese, you have {cheese}")
      

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
    playerhp -= stage_difficulty * random.randint(1,stage_difficulty)
    if playerhp <= 0:
      dead = True
      return
    print(f"you have {playerhp} health")

def save_config():

  global cheese
  global skillpoints
  global stage_difficulty
  global maxplayerhp
  global playerhp
  global dodge_chance
  global player_level 
  global damage
  global exp


  with open("config.json", 'w') as file:
    json.dump({
      "cheese": cheese,
      "skillpoints": skillpoints,
      "stage_difficulty" : stage_difficulty,
     "maxplayerhp" : maxplayerhp,
      "playerhp"  : playerhp,
     "dodge_chance" : dodge_chance,
      "player_level" : player_level,
      "damage" : damage,
      "exp" : exp
    }, file)

def load_config():

  global cheese
  global skillpoints
  global stage_difficulty
  global maxplayerhp
  global playerhp
  global dodge_chance
  global player_level 
  global damage 
  global exp

  if "config.json" not in os.listdir("."):
    save_config()
    return
  
  with open("config.json", "r") as f:
      data: dict = json.load(f)

      cheese = data["cheese"]
      skillpoints = data["skillpoints"]
      stage_difficulty = data["stage_difficulty"]
      maxplayerhp = data["maxplayerhp"]
      playerhp = data["playerhp"]
      dodge_chance = data["dodge_chance"]
      player_level = data["player_level"]
      damage = data["damage"]
      exp = data["exp"]


def check():
  global player_level
  global skillpoints
  global exp_requirement
  global exp
  
  
  if player_level == 0:
    exp_requirement = 1
  else:
    exp_requirement = 2 ** player_level
  if exp >= exp_requirement:
    exp -= exp_requirement
    player_level += 1
    skillpoints += 1
    print(f"level up to level {player_level}")


while game_on == True :
  if dead == True:
    print("you have been nubt\n reloading save")
    load_config()
    stage_difficulty = 1
    dead = False
  user_input()
  check()