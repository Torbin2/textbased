import random

cheese = 0
spawned = False
xp = 1
level = 1
maxplayerhp = 20
playerhp = 20
dodge_chance = 5
dead = False
print("input help for commands")

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
  
  if damage_rng <= dodge_chance:
    
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
      print("your dead")
      return
    print(f"you have {playerhp} health")

def user_input(minhp ,maxhp):
  player_input = input("\ninput = ")
  
  global enemy_hit
  global xp
  global spawned
  global mhp
  global bmhp
  global cheese
  global playerhp
  global maxplayerhp


  if player_input == "help" :
    print("type f to find a (new) monster \ntype a to atack\ntype h to heal using cheese\ntype i to check player info`")
  
  elif player_input == "test":
    print("no current tests")
  
  elif player_input == "i":
    print(f"{playerhp}/{maxplayerhp} health\n{xp} xp\n{cheese} cheese\n {dodge_chance}/10 dodge chance (lower is better)")

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
    dmg = xp
    mhp -= dmg
    if mhp <= 0:
      xp += 1
      print(f"the slime is dead \nxp = {xp}")
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
      if playerhp > maxplayerhp:
        healthcheck = playerhp - maxplayerhp
        healing_amount = healing_amount - healthcheck
        playerhp = maxplayerhp
      print(f"you healed {healing_amount} hp\ntotal hp = {playerhp}")
 
  else :
    print("invalid input")

while level == 1 :
  user_input(1,10)
  if xp >= 5:
    level = 2
while level == 2:
  user_input(10,30)