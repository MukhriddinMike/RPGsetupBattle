from classes.game import Person, bcolors
from classes.magic import Spell

#create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

#Create white magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

'''
magic=[{"name":'Fire', 'cost':10, 'dmg':100},
        {"name":'Thunder', 'cost':10, 'dmg':100},
         {"name":'Blizzard', 'cost':10, 'dmg':124}]

player = Person(460,65,60,34,magic)
enemy = Person(1200,65,45,25,magic)
'''
player = Person(460,65,60,34,[fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200,65,45,25,[])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!' + bcolors.ENDC)
while running:
    print('=============')
    player.choose_action()
    choice = input("Choose action: ")
    index =int(choice)-1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You atacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough NP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "point of damage"+ bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

print("---------------------")

print("Enemy HP", bcolors.FAIL +str(enemy.get_hp() + "/" + str(enemy.get_max_hp() + bcolors.ENDC)))

print("Your HP", bcolors.OKGREEN + str(player.get_hp() + "/" + str(player.get_max_hp() + bcolors.ENDC)))

print("Your MP:", bcolors.OKBLUE + str(player.get_mp() + "/" + str(player.get_max_mp() + bcolors.ENDC)) )




if enemy.get_hp() == 0:
    print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
    running = False
elif player.get_hp() == 0:
    print(bcolors.FAIL + 'Your enemy has defeated you!' + bcolors.ENDC )
    running = False
