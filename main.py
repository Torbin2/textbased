import random

minhp = 1
maxhp = 1
hp = 1
xp = 1
atack = "b"
basehp = 1
level = 1


dev = input("skip?")
if dev == "qwerty":
  level = 2
  xp = 10

while level == 1:
  walk = input("press w to walk\n")

  dmg = xp
  minhp = 5
  maxhp = 10
  colours = ["green", "blue", "yellow"]

  if walk == 'w':

    hp = random.randint(minhp, maxhp)
    colour1 = random.choice(colours)
    basehp = hp
    print(f"a {colour1} slime apeared {hp}/{hp}")
    atack = input(f"press a for {dmg} damage\n")

    for i in range(999):
      if atack == "a":
        hp -= dmg

      if hp <= 0:
        xp += 1
        print(f"the {colour1} slime is dead xp = {xp}")
        if xp >= 10:
          level = 2
          atack = "b"
          print("travaling to level 2")
        break

      atack = "b"
      atack = input(f"the {colour1} slime has {hp}/{basehp} health\n")

while level == 2:
  walk = input("press f to find\n")

  dmg = xp
  minhp = 20
  maxhp = 40
  monsters = ["rock", "stone", "boulder"]

  if walk == 'f':
    hp = random.randint(minhp, maxhp)
    colour2 = random.choice(monsters)
    basehp = hp
    print(f"a {colour2} monster apeared {hp}/{hp}")
    atack = input(f"press a for {dmg} damage\n")
    for i in range(999):
      if atack == "a":
        hp -= dmg
      if hp <= 0:
        xp += 2
        print(f"the {colour2} monster is dead xp = {xp}")
        break
      #if xp >= 30:
      #level = 3
      #print("travaling to level 3")
      #break
      atack = "b"
      atack = input(f"the {colour2} slime has {hp}/{basehp} health\n")
