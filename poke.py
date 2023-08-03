import json
import random

def extract_key_value(json_data, key):
    try:
        data = json.loads(json_data)
        return data[key]
    except:
        return None

print("Welcome to Pokemon Red")
name = input("What is your name: ")
coins = 5
stageprice = 5
level = 1
temp = 0
wandermax = 0

while True:
    game = input("Do you want a new game or load saved game: ").lower()
    if game == "new game" or game == "newgame":
        print("Welcome to the world of Pokemon")
        input("Press Enter to continue...")
        print("My name is Oak, but people call me the Pokemon Professor")
        input("Press Enter to continue...")
        print("This world is inhabited by creatures called Pokemon")
        input("Press Enter to continue...")
        print("For some people, Pokemon are pets, but for others, Pokemon are used to fight")
        break
    elif game in ["load saved game", "savegame", "save game", "loadsavedgame", "load save game", "loadsavegame"]:
        print("No save game feature available. Try again later.")

    else:
        print("Invalid input. Please choose 'new game' or 'load saved game'.")
        continue

print("This is my grandson, he is your rival, his name is Jack")

basepokechoice = ["pikachu", "charmander", "diglett", "ditto"]
baseenergyamount = 5

json_pikachu = '{"hp": 35, "maxhp": 274, "attack": 55, "maxattack": 229, "defence": 40, "maxdefence": 196, "special": "electroball", "level": 1, "health": 60, "stage": 0}'
json_charmander = '{"hp": 39, "maxhp": 282, "attack": 52, "maxattack": 223, "defence": 43, "maxdefence": 203, "special": "ember", "level": 1, "health": 60, "stage": 0}'
json_diglett = '{"hp": 10, "maxhp": 224, "attack": 55, "maxattack": 229, "defence": 25, "maxdefence": 163, "special": "mudslap", "level": 1, "health": 30, "stage": 0}'
json_ditto = '{"hp": 48, "maxhp": 300, "attack": 48, "maxattack": 214, "defence": 48, "maxdefence": 214, "special": "transform", "level": 1, "health": 50, "stage": 0}'

while True:
    basepoke = input("Choose your first Pokemon (Charmander, Pikachu, Diglett, or Ditto): ").lower()

    if basepoke in basepokechoice:
        if basepoke == "pikachu":
            playerenergy = (f"electric {baseenergyamount}").upper()
            pokemon_stats = json.loads(json_pikachu)
        elif basepoke == "charmander":
            playerenergy = (f"fire {baseenergyamount}").upper()
            pokemon_stats = json.loads(json_charmander)
        elif basepoke == "diglett":
            playerenergy = (f"rock {baseenergyamount}").upper()
            pokemon_stats = json.loads(json_diglett)
        elif basepoke == "ditto":
            playerenergy = (f"mystic {baseenergyamount}").upper()
            pokemon_stats = json.loads(json_ditto)
        break
    else:
        print("Not an option, try again")
        continue

print("Your first Pokémon is:", basepoke.upper())
print("Player's energy:", playerenergy)
print("Pokemon stats:")
print("HP:", pokemon_stats["hp"])
print("Max HP:", pokemon_stats["maxhp"])
print("Attack:", pokemon_stats["attack"])
print("Max Attack:", pokemon_stats["maxattack"])
print("Defence:", pokemon_stats["defence"])
print("Max Defence:", pokemon_stats["maxdefence"])
print("Special:", pokemon_stats["special"])
print("Health:", pokemon_stats["health"])
print("Stage:", pokemon_stats["stage"])

choices = ["attack", "defend", "heal", "run"]
basicbulbasaurhealth = 60
firstfight = True

while True:
    print("You encounter a trainer with a bulbasaur equipped")
    if firstfight:
        print(f"Your stats are HP: {pokemon_stats['health']}, Attack: {pokemon_stats['attack']}, Defence: {pokemon_stats['defence']}, Stage: {pokemon_stats['stage']}")
        firstfight = False

    while True:
        firstattack = input("What is your move (Attack, Defend, Heal, Run): ").lower()
        if firstattack == "attack":
            print(f"You attacked Bulbasaur and dealt {pokemon_stats['attack']} damage")
            basicbulbasaurhealth -= pokemon_stats["attack"]
            print(f"Bulbasaur now has {basicbulbasaurhealth} health")
        elif firstattack == "defend":
            print("You defended yourself against Bulbasaur's attack that would have dealt 30 damage")
            print(f"You now have {pokemon_stats['health']} health")
        elif firstattack == "heal":
            if playerenergy.split()[1] == "mystic":
                pokemon_stats["health"] += 30
                print("Pokemon healed 30")
            else:
                print("Your pokemon doesn't have the ability to heal")
        elif firstattack == "run":
            print("You did not successfully run away")
        else:
            print("Not a valid input, it is now Bulbasaur's turn")

        if basicbulbasaurhealth <= 0:
            print("You defeated Bulbasaur! Congratulations!")
            coins += 10
            level += 1
            break

        print("Now its Bulbasaur's turn")
        if basicbulbasaurhealth >= 30:
            bulbaattack = choices[0]
        elif 15 <= basicbulbasaurhealth < 30:
            bulbaattack = choices[1]
        elif basicbulbasaurhealth < 15:
            bulbaattack = choices[2]
        else:
            bulbaattack = choices[3]

        if bulbaattack == "attack":
            pokemon_stats["health"] -= 30
            print("Bulbasaur attacked you and dealt 30 damage")
            print(f"Your {basepoke} now has {pokemon_stats['health']} health")
        elif bulbaattack == "defend":
            print(f"{basepoke} tried to attack and deal {pokemon_stats['attack']} damage, but Bulbasaur defended")
        elif bulbaattack == "heal":
            print("Bulbasaur healed 30 points")
            basicbulbasaurhealth += 30
            print(f"Bulbasaur's health is now {basicbulbasaurhealth}")
        else:
            print("Bulbasaur ran away")
            print("You defeated Bulbasaur! Congratulations!")
            coins += 10
            level += 1
            break

        if pokemon_stats["health"] <= 0:
            print("Your Pokemon fainted. You lost the battle.")
            coins -= 5
            temp += 1
            break

    if temp == 0:
        print(f"Congratulations, You won your first battle and gained {coins} coins")
    else:
        print(f"Sorry, you lost your first battle and now have {coins} coins")

    upgrading = True
    while upgrading:
        upgrade = input(f"Do you want to spend 10 coins to upgrade your pokemon to stage {pokemon_stats['stage'] + 1}, you have {coins} coins (y/n): ").lower()
        if upgrade == "y" and coins >= stageprice and pokemon_stats['stage'] < 15:
            coins = coins - stageprice
            stageprice += 5
            pokemon_stats['hp'] += 10
            pokemon_stats['maxhp'] += 10
            pokemon_stats['attack'] += 10
            pokemon_stats['maxattack'] += 10
            pokemon_stats['defence'] += 10
            pokemon_stats['maxdefence'] += 10
            pokemon_stats['health'] += 10
            pokemon_stats['stage'] += 1
            baseenergyamount += 5
            print(f"{basepoke} has been upgraded to stage {pokemon_stats['stage']} and now has {playerenergy}.")
            print("Pokemon stats:")
            print("HP:", pokemon_stats["hp"])
            print("Max HP:", pokemon_stats["maxhp"])
            print("Attack:", pokemon_stats["attack"])
            print("Max Attack:", pokemon_stats["maxattack"])
            print("Defence:", pokemon_stats["defence"])
            print("Max Defence:", pokemon_stats["maxdefence"])
            print("Special:", pokemon_stats["special"])
            print("Health:", pokemon_stats["health"])
            print("Stage:", pokemon_stats["stage"])
            upgrading = False
        elif upgrade == "n":
            print("Okay")
            upgrading = False
        else:
            print("Not an option")
            upgrading = True

    mewtwohealth = 130
    mewtwodamage = 90
    # Second Battle
    while True:
        print(f"After you won your first battle, you were confident in {basepoke}'s ability to fight")
        choice2 = input("You see a poster to fight a Mewtwo, do you want to fight (y/n)").lower()
        if choice2 == "y":
            print("You go to an arena with hordes of fans betting on who will win, you enter the ring with your pokemon and get ready")
            secondfight = True
            if secondfight:
                print(f"Your stats are HP: {pokemon_stats['health']}, Attack: {pokemon_stats['attack']}, Defence: {pokemon_stats['defence']}, Stage: {pokemon_stats['stage']}")
            while True:
                firstattack1 = input("What is your move (Attack, Defend, Heal, Run): ").lower()
                if firstattack1 == "attack":
                    print(f"You attacked Mewtwo and dealt {pokemon_stats['attack']} damage")
                    mewtwohealth = mewtwohealth - pokemon_stats["attack"]
                    print(f"Mewtwo now has {mewtwohealth} health")
                elif firstattack1 == "defend":
                    print(f"You defended yourself against Mewtwo's attack that would have dealt {mewtwodamage} damage")
                    print(f"You now have {pokemon_stats['health']} health")
                elif firstattack1 == "heal":
                    print("You are already at max health")
                elif firstattack1 == "run":
                    print("You successfully ran away but you lost 5 coins")
                    coins-=5
                    break
                    
                else:
                    print("Not a valid input, it is now Mewtwo's turn")

                if mewtwohealth <= 0:
                    print("You defeated Mewtwo! Congratulations!")
                    coins += 10
                    level += 1
                    break

                print("Now its Mewtwo's turn")
                if mewtwohealth >= 30:
                    mewtwoattack = choices[0]
                elif 15 <= mewtwohealth < 30:
                    mewtwoattack = choices[1]
                elif mewtwohealth < 15:
                    mewtwoattack = choices[2]
                else:
                    mewtwoattack = choices[3]

                if mewtwoattack == "attack":
                    pokemon_stats["health"] -= 30
                    print("Mewtwo attacked you and dealt 30 damage")
                    print(f"Your {basepoke} now has {pokemon_stats['health']} health")
                elif mewtwoattack == "defend":
                    print(f"{basepoke} tried to attack and deal {pokemon_stats['attack']} damage, but Mewtwo defended")
                elif mewtwoattack == "heal":
                    print("Mewtwo healed 30 points")
                    mewtwohealth += 30
                    print(f"Mewtwo's health is now {mewtwohealth}")
                    continue
                else:
                    print("Mewtwo ran away")
                    print("You defeated Mewtwo! Congratulations!")
                    coins += 10
                    level += 1
                    break

                if pokemon_stats["health"] <= 0:
                    print("Your Pokemon fainted. You lost the battle.")
                    coins -= 5
                    break

        elif choice2 == "n":
            print("You decide not to fight the trainer with a Mewtwo.")
            print("Then you decide to walk in and watch Cosmog fight the Mewtwo")
            print("You see that Mewtwo destroy the Cosmog")

        upgrade2 = input(f"After you see the Mewtwo beat Cosmog you think of upgrading your {basepoke} for {stageprice} coins, you have {coins} coins (y/n): ").lower()
        if upgrade2 == "y":
            coins=coins-stageprice
            stageprice += 5
            pokemon_stats['hp'] += 10
            pokemon_stats['maxhp'] += 10
            pokemon_stats['attack'] += 10
            pokemon_stats['maxattack'] += 10
            pokemon_stats['defence'] += 10
            pokemon_stats['maxdefence'] += 10
            pokemon_stats['health'] += 10
            pokemon_stats['stage'] += 1
            baseenergyamount += 5
            print(f"{basepoke} has been upgraded to stage {pokemon_stats['stage']} and now has {playerenergy}.")
            print("Pokemon stats:")
            print("HP:", pokemon_stats["hp"])
            print("Max HP:", pokemon_stats["maxhp"])
            print("Attack:", pokemon_stats["attack"])
            print("Max Attack:", pokemon_stats["maxattack"])
            print("Defence:", pokemon_stats["defence"])
            print("Max Defence:", pokemon_stats["maxdefence"])
            print("Special:", pokemon_stats["special"])
            print("Health:", pokemon_stats["health"])
            print("Stage:", pokemon_stats["stage"])
            break

        elif upgrade2 == "n":
            print("Okay")
            break

        else:
            print("Not an option")
            continue

    while True:
        print(f"Ok {name}, you have proved yourself in the ability to train {basepoke}")
        input("Press Enter to continue...")
        print("Now you have the freedom to explore Kanto in its full beauty")
        input("Press Enter to continue...")
        print("You can type (1. for upgrading your pokemon)")
        input("Press Enter to continue...")
        print("Press (2. To explore shops and equip your pokemon)")
        input("Press Enter to continue...")
        print("Press (3. To go to the arena and fight a pokemon)")
        input("Press Enter to continue...")
        print("Press (4. Wander around)")
        input("Press Enter to continue...")
        print("Press (5. To check your stats)")
        input("Press Enter to continue...")
        print("Press (6. For help)")
        input("Press Enter to continue...")
        print("Press (7. To save and exit)")
        break
  
    while True:
          freechoice = input("What action do you want to perform? ")
  
          if freechoice == "1":
              choice3 = input(f"To upgrade to stage {pokemon_stats['stage'] + 1}, you need to have {stageprice} coins, you have {coins} coins (y/n): ").lower()
              if choice3 == "y" and coins >= stageprice and pokemon_stats['stage'] < 6:
                  coins -= stageprice
                  stageprice += 5
                  pokemon_stats['hp'] += 10
                  pokemon_stats['maxhp'] += 10
                  pokemon_stats['attack'] += 10
                  pokemon_stats['maxattack'] += 10
                  pokemon_stats['defence'] += 10
                  pokemon_stats['maxdefence'] += 10
                  pokemon_stats['health'] += 10
                  pokemon_stats['stage'] += 1
                  baseenergyamount += 5
                  print(f"{basepoke} has been upgraded to stage {pokemon_stats['stage']} and now has {playerenergy}.")
                  print("Pokemon stats:")
                  print("HP:", pokemon_stats["hp"])
                  print("Max HP:", pokemon_stats["maxhp"])
                  print("Attack:", pokemon_stats["attack"])
                  print("Max Attack:", pokemon_stats["maxattack"])
                  print("Defence:", pokemon_stats["defence"])
                  print("Max Defence:", pokemon_stats["maxdefence"])
                  print("Special:", pokemon_stats["special"])
                  print("Health:", pokemon_stats["health"])
                  print("Stage:", pokemon_stats["stage"])
              elif choice3 == "n":
                  print("Okay")
              else:
                  print("Not an option")
  
          elif freechoice == "2":
            choice4 = input("You walk into town and find 4 shops ( Energy shop,  Attack shop,  Pokemon shop,  Wander shop): ").lower()
            if choice4 == "energyshop" or choice4 == "energy shop":
              print(f"Welcome to the Energy Shop, You can buy energy for your {basepoke} pokemon")
              choice5 = input(f"You have {playerenergy} energy, do you want to buy 5 more for 5 coins (y/n): ").lower()
              if choice5 == "y":
                baseenergyamount += 5
                playerenergy = playerenergy + baseenergyamount
                print(playerenergy)
                continue
              elif choice5 == "n":
                print("Okay")
                continue
              else:
                print("Not an option")
                continue
            elif choice4 == "attackshop" or choice4 == "attack shop":
                choice6 = input("Do you want to buy 10 attack for 5 coins (y/n)").lower()
                if choice6 == "y":
                      pokemon_stats["attack"] += 10
                      coins -= 5
                      print(f"You have {pokemon_stats['attack']} attack")
                elif choice6 == "n":
                    print("Okay")
                    continue
                elif choice4 == "pokemonshop" or choice4 == "pokemon shop":
                  print("Sorry Pokemon shop is closed come back later")
                elif choice4 == "wandershop" or choice4 == "wander shop":
                  choice7=input("Do you want to spend 20 coins to reset your wander count (y/n)")
                if choice7=="y":
                  print(f"Okay, you now have {wandermax} Wandering attempts left")
                  continue
                elif choice7=="n":
                  print("Okay")
                  continue
                else:
                  print("Not an option")
                  continue
            else:
              print("Not an option")
              continue
              
  
          elif freechoice == "3":
              pokemonchoicefree = ["tepig", "kyogre", "sneasler", "poliwhirl"]
              computerrandpoke = random.choice(pokemonchoicefree)
              tepighealth = 80
              tepigattack = 35
              kygorehealth = 130
              kygoreattack = 30
              sneaslerhealth = 120
              sneaslerattack = 60
              poliwhirlhealth = 90
              poliwhirlattack = 30
  
              if computerrandpoke in pokemonchoicefree:
                  if computerrandpoke == "tepig":
                      print(f"You walk into the ring after signing up to fight with {computerrandpoke}")
                      if firstfight:
                          print(f"Your stats are HP: {pokemon_stats['health']}, Attack: {pokemon_stats['attack']}, Defence: {pokemon_stats['defence']}, Stage: {pokemon_stats['stage']}")
  
                      while True:
                          firstattack1 = input("What is your move (Attack, Defend, Heal, Run): ").lower()
                          if firstattack1 == "attack":
                              print(f"You attacked Tepig and dealt {pokemon_stats['attack']} damage")
                              tepighealth -= pokemon_stats["attack"]
                              print(f"Tepig now has {tepighealth} health")
                          elif firstattack1 == "defend":
                              print("You defended yourself against Tepig's attack that would have dealt 30 damage")
                              print(f"You now have {pokemon_stats['health']} health")
                          elif firstattack1 == "heal":
                              if playerenergy.split()[1] == "mystic":
                                  pokemon_stats["health"] += 30
                                  print("Pokemon healed 30")
                              else:
                                  print("Your pokemon doesn't have the ability to heal")
                          elif firstattack1 == "run":
                              print("You successfully ran away")
                              break
                          else:
                              print("Not a valid input, it is now Tepig's turn")
  
                          if tepighealth <= 0:
                              print("You defeated Tepig! Congratulations!")
                              coins += 10
                              level += 1
                              break
  
                          print("Now it's Tepig's turn")
                          if tepighealth >= 30:
                              tepigchoice = choices[0]
                          elif 15 <= tepighealth < 30:
                              tepigchoice = choices[1]
                          elif tepighealth < 15:
                              tepigchoice = choices[2]
                          else:
                              tepigchoice = choices[3]
  
                          if tepigchoice == "attack":
                              pokemon_stats["health"] -= 30
                              print("Tepig attacked you and dealt 30 damage")
                              print(f"Your {basepoke} now has {pokemon_stats['health']} health")
                          elif tepigchoice == "defend":
                              print(f"{basepoke} tried to attack and deal {pokemon_stats['attack']} damage, but Tepig defended")
                          elif tepigchoice == "heal":
                              print("Tepig healed 30 points")
                              tepighealth += 30
                              print(f"Tepig's health is now {tepighealth}")
                              continue
                          else:
                              print("Tepig ran away")
                              print("You defeated Tepig! Congratulations!")
                              coins += 10
                              level += 1
                              break
  
                          if pokemon_stats["health"] <= 0:
                              print("Your Pokemon fainted. You lost the battle.")
                              coins -= 5
                              break
  
                  if computerrandpoke == "kygore":
                      print(f"You walk into the ring after signing up to fight with {computerrandpoke}")
                      if firstfight:
                          print(f"Your stats are HP: {pokemon_stats['health']}, Attack: {pokemon_stats['attack']}, Defence: {pokemon_stats['defence']}, Stage: {pokemon_stats['stage']}")
  
                      while True:
                          firstattack1 = input("What is your move (Attack, Defend, Heal, Run): ").lower()
                          if firstattack1 == "attack":
                              print(f"You attacked Kygore and dealt {pokemon_stats['attack']} damage")
                              kygorehealth -= pokemon_stats["attack"]
                              print(f"Kygore now has {kygorehealth} health")
                          elif firstattack1 == "defend":
                              print("You defended yourself against Kygore's attack that would have dealt 60 damage")
                              print(f"You now have {pokemon_stats['health']} health")
                          elif firstattack1 == "heal":
                              if playerenergy.split()[1] == "mystic":
                                  pokemon_stats["health"] += 30
                                  print("Pokemon healed 30")
                              else:
                                  print("Your pokemon doesn't have the ability to heal")
                          elif firstattack1 == "run":
                              print("You successfully ran away")
                          else:
                              print("Not a valid input, it is now Kygore's turn")
  
                          if kygorehealth <= 0:
                              print("You defeated Kygore! Congratulations!")
                              coins += 10
                              level += 1
                              break
  
                          print("Now its Kygore's turn")
                          if kygorehealth >= 30:
                              kygorechoice = choices[0]
                          elif 15 <= kygorehealth < 30:
                              kygorechoice = choices[1]
                          elif kygorehealth < 15:
                              kygorechoice = choices[2]
                          else:
                              kygorechoice = choices[3]
  
                          if kygorechoice == "attack":
                              pokemon_stats["health"] -= kygoreattack
                              print("Kygore attacked you and dealt 60 damage")
                              print(f"Your {basepoke} now has {pokemon_stats['health']} health")
                          elif kygorechoice == "defend":
                              print(f"{basepoke} tried to attack and deal {pokemon_stats['attack']} damage, but Kygore defended")
                          elif kygorechoice == "heal":
                              print("Kygore healed 30 points")
                              kygorehealth += 30
                              print(f"Kygore's health is now {kygorehealth}")
                              continue
                          else:
                              print("Kygore ran away")
                              print("You defeated Kygore! Congratulations!")
                              coins += 10
                              level += 1
                              break
  
                          if pokemon_stats["health"] <= 0:
                              print("Your Pokemon fainted. You lost the battle.")
                              coins -= 5
                              break
  
                  if computerrandpoke == "sneasler":
                      print(f"You walk into the ring after signing up to fight with {computerrandpoke}")
                      if firstfight:
                          print(f"Your stats are HP: {pokemon_stats['health']}, Attack: {pokemon_stats['attack']}, Defence: {pokemon_stats['defence']}, Stage: {pokemon_stats['stage']}")
  
                      while True:
                          firstattack1 = input("What is your move (Attack, Defend, Heal, Run): ").lower()
                          if firstattack1 == "attack":
                              print(f"You attacked Sneasler and dealt {pokemon_stats['attack']} damage")
                              sneaslerhealth -= pokemon_stats["attack"]
                              print(f"Sneasler now has {sneaslerhealth} health")
                          elif firstattack1 == "defend":
                              print("You defended yourself against Sneasler's attack that would have dealt 60 damage")
                              print(f"You now have {pokemon_stats['health']} health")
                          elif firstattack1 == "heal":
                              if playerenergy.split()[1] == "mystic":
                                  pokemon_stats["health"] += 30
                                  print("Pokemon healed 30")
                              else:
                                  print("Your pokemon doesn't have the ability to heal")
                          elif firstattack1 == "run":
                              print("You successfully ran away")
                          else:
                              print("Not a valid input, it is now Sneasler's turn")
  
                          if sneaslerhealth <= 0:
                              print("You defeated Sneasler! Congratulations!")
                              coins += 10
                              level += 1
                              break
  
                          print("Now its Sneasler's turn")
                          if sneaslerhealth >= 30:
                              sneaslerchoice = choices[0]
                          elif 15 <= sneaslerhealth < 30:
                              sneaslerchoice = choices[1]
                          elif sneaslerhealth < 15:
                              sneaslerchoice = choices[2]
                          else:
                              sneaslerchoice = choices[3]
  
                          if sneaslerchoice == "attack":
                              pokemon_stats["health"] -= sneaslerattack
                              print("Sneasler attacked you and dealt 60 damage")
                              print(f"Your {basepoke} now has {pokemon_stats['health']} health")
                          elif sneaslerchoice == "defend":
                              print(f"{basepoke} tried to attack and deal {pokemon_stats['attack']} damage, but Sneasler defended")
                          elif sneaslerchoice == "heal":
                              print("Sneasler healed 30 points")
                              sneaslerhealth += 30
                              print(f"Sneasler's health is now {sneaslerhealth}")
                              continue
                          else:
                              print("Sneasler ran away")
                              print("You defeated Sneasler! Congratulations!")
                              coins += 10
                              level += 1
                              break
  
                          if pokemon_stats["health"] <= 0:
                              print("Your Pokemon fainted. You lost the battle.")
                              coins -= 5
                              break
  
                  if computerrandpoke == "poliwhirl":
                      print(f"You walk into the ring after signing up to fight with {computerrandpoke}")
                      if firstfight:
                          print(f"Your stats are HP: {pokemon_stats['health']}, Attack: {pokemon_stats['attack']}, Defence: {pokemon_stats['defence']}, Stage: {pokemon_stats['stage']}")
  
                      while True:
                          firstattack1 = input("What is your move (Attack, Defend, Heal, Run): ").lower()
                          if firstattack1 == "attack":
                              print(f"You attacked Poliwhirl and dealt {pokemon_stats['attack']} damage")
                              poliwhirlhealth -= pokemon_stats["attack"]
                              print(f"Poliwhirl now has {poliwhirlhealth} health")
                          elif firstattack1 == "defend":
                              print("You defended yourself against Poliwhirl's attack that would have dealt 60 damage")
                              print(f"You now have {pokemon_stats['health']} health")
                          elif firstattack1 == "heal":
                              if playerenergy.split()[1] == "mystic":
                                  pokemon_stats["health"] += 30
                                  print("Pokemon healed 30")
                              else:
                                  print("Your pokemon doesn't have the ability to heal")
                          elif firstattack1 == "run":
                              print("You successfully ran away")
                          else:
                              print("Not a valid input, it is now Poliwhirl's turn")
  
                          if poliwhirlhealth <= 0:
                              print("You defeated Poliwhirl! Congratulations!")
                              coins += 10
                              level += 1
                              break
  
                          print("Now its Poliwhirl's turn")
                          if poliwhirlhealth >= 30:
                              poliwhirlchoice = choices[0]
                          elif 15 <= poliwhirlhealth < 30:
                              poliwhirlchoice = choices[1]
                          elif poliwhirlhealth < 15:
                              poliwhirlchoice = choices[2]
                          else:
                              poliwhirlchoice = choices[3]
  
                          if poliwhirlchoice == "attack":
                              pokemon_stats["health"] -= poliwhirlattack
                              print("Poliwhirl attacked you and dealt 60 damage")
                              print(f"Your {basepoke} now has {pokemon_stats['health']} health")
                          elif poliwhirlchoice == "defend":
                              print(f"{basepoke} tried to attack and deal {pokemon_stats['attack']} damage, but Poliwhirl defended")
                          elif poliwhirlchoice == "heal":
                              print("Poliwhirl healed 30 points")
                              poliwhirlhealth += 30
                              print(f"Poliwhirl's health is now {poliwhirlhealth}")
                              continue
                          else:
                              print("Poliwhirl ran away")
                              print("You defeated Poliwhirl! Congratulations!")
                              coins += 10
                              level += 1
                              break
  
                          if pokemon_stats["health"] <= 0:
                              print("Your Pokemon fainted. You lost the battle.")
                              coins -= 5
                              break
  
          elif freechoice == "4":
            if wandermax < 10:
              wanderingoptions = ["you found 30 coins on the ground", "you found a card for 7 energy", "you found a boost for 3 attack"]
              wanderoptions = random.choice(wanderingoptions)
              print(f"While wandering around {wanderoptions}")
              if wanderoptions == "you found 30 coins on the ground":
                coins += 30
                print(f"You have {coins} coins")
                wandermax += 1
              elif wanderoptions == "you found a card for 7 energy":
                baseenergyamount += 7
                print(f"You have {playerenergy} energy")
                wandermax += 1
              else:
                print(f"You have {pokemon_stats['attack']} attack")
                pokemon_stats['attack'] += 3
                wandermax += 1
            else:
              print("You Feel Tired And You Cant Wander Anymore")
              continue
  
          
          elif freechoice == "5":
            print("Pokemon stats:")
            print("HP:", pokemon_stats["hp"])
            print("Max HP:", pokemon_stats["maxhp"])
            print("Attack:", pokemon_stats["attack"])
            print("Max Attack:", pokemon_stats["maxattack"])
            print("Defence:", pokemon_stats["defence"])
            print("Max Defence:", pokemon_stats["maxdefence"])
            print("Special:", pokemon_stats["special"])
            print("Health:", pokemon_stats["health"])
            print("Stage:", pokemon_stats["stage"])
            print(f"You have {coins} coins and {playerenergy} energy")

          elif freechoice == "6":
            print("Now you have the freedom to explore Kanto in its full beauty")
            input("Press Enter to continue...")
            print("You can type (1. for upgrading your pokemon)")
            input("Press Enter to continue...")
            print("Press (2. To explore shops and equip your pokemon)")
            input("Press Enter to continue...")
            print("Press (3. To go to the arena and fight a pokemon)")
            input("Press Enter to continue...")
            print("Press (4. Wander around)")
            input("Press Enter to continue...")
            print("Press (5. To check your stats)")
            input("Press Enter to continue...")
            print("Press (6. For help)")
            input("Press Enter to continue...")
            print("Press (7. To save and exit)")

          elif freechoice == "7":
            print("Bye")
            break

          else:
            print("Not an option")

    break

print("Thanks for playing Pokemon Red!")
print(f"Your final stats: HP: {pokemon_stats['hp']}, Max HP: {pokemon_stats['maxhp']}, Attack: {pokemon_stats['attack']}, Max Attack: {pokemon_stats['maxattack']}, Defence: {pokemon_stats['defence']}, Max Defence: {pokemon_stats['maxdefence']}, Special: {pokemon_stats['special']}")
print("You collected", coins, "coins in total.")