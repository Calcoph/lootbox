# python lootbox.py
from random import randint


commands = [
    "exit", "open", "open a bunch", "check coins",
    "help", "check inventory", "shortcuts"
    ]
shortcuts = {
    "exit": "x", "open": "s", "open a bunch": "a",
    "check coins": "z", "help": "h", "check inventory": "c", "shortcuts": "d"
    }
counters = {
    "shits": 0, "named shits": 0, "curses": 0, "commons": 0, "named commons": 0,
    "rares": 0, "named rares": 0, "epics": 0, "named epics": 0,
    "legendaries": 0, "named legendaries": 0, "penes": 0
    }

shits = {
    440: "Sutewo",  441: "Sohilaf",  442: "Sixogi",  443: "Sugohagut",
    444: "Sonodih",  445: "Socilozi",  446: "Slukuzik",  447: "Sufoza",
    448: "Susiata",  449: "Sijefoisu",  450: "Seair",  451: "Surogo",
    452: "Sawufie",  453: "Secodumuv",  454: "Sepokux",  455: "Sizoj",
    456: "Subowiko",  457: "Setaem",  458: "Sewiaye",  459: "Sumurej",
    460: "Sowas",  461: "Sarienuxo",  462: "Soroe",  463: "Suvake",  464: "Sujewul",
    465: "Sivedeb",  466: "Silame",  467: "Subuacu",  468: "Sugoqiva",
    469: "Samunuxo",  470: "Sayioe",  471: "Suwenivob",  472: "Socis",  473: "Sivuqe",
    474: "Seiup",  475: "Soediumo",  476: "Sazeewaxu",  477: "Sanarolo",
    478: "Sayuyo", 479: "Seloje",  480: "Sonau",  481: "Sebuiriahi",  482: "Seeqaqew",
    483: "Suwagi", 484: "Saoxo",  485: "Siyewa",  486: "Samukih",  487: "Seijeoze",
    488: "Sabeje",  489: "Semizov",  490: "Sumixalij",  491: "Subicasi",
    492: "Sefofugo",  493: "Soacee",  494: "Senononoc",  495: "Sugiz",
    496: "Saxuniyog", 497: "Siiku",  498: "Sirugo",  499: "Sifiah",  500: "Sofededi",
    501: "Sonajo", 502: "Sasakezen",  503: "Sojinijo",  504: "Sukes",  505: "Sexizagak",
    506: "Sabaebe", 507: "Savahuax",  508: "Siiaru",  509: "Suvicof",  510: "Seliw",
    511: "Sigayo", 512: "Soweak",  513: "Sohop",  514: "Sayagulo",  515: "Sioezo",
    516: "Sarulov", 517: "Sodede",  518: "Soterel",  519: "Sozekunip",  520: "Curse"
    }
commons = {
    180: "Cacep",  181: "Cipanouvo",  182: "Ciauhekas",
    183: "Cieuyafuc",  184: "Caqocaqao",  185: "Cakonusej",  186: "Cuxoiomoy",
    187: "Cuqeusok",  188: "Cubamoqe",  189: "Cavuburid",  190: "Celaqewo",
    191: "Cituyeeet",  192: "Cusuzeyuz",  193: "Ciooleeji",  194: "Citoyi",
    195: "Cugipayo",  196: "Cazawey",  197: "Cacapueap",  198: "Cayiuhe",
    199: "Cuwioei",  200: "Cuteali",  201: "Ciraxa",  202: "Cumokuhi",
    203: "Cabiis",  204: "Ceupuoeuk",  205: "Cebike",  206: "Cijad",  207: "Cagak",
    208: "Cevauk",  209: "Cegizi",  210: "Cetoyabo",  211: "Cauvafoak",
    212: "Cirofuriu",  213: "Cirodesuq",  214: "Corocuqoyo",  215: "Coduf",
    216: "Cikonu",  217: "Carauxi",  218: "Caousi",  219: "Ciuxeledo",
    220: "Catihe",  221: "Cegipe",  222: "Ciaqi",  223: "Cociwia",  224: "Caxeri",
    225: "Cavimev",  226: "Cagemu",  227: "Coiyob",  228: "Cuaenof",
    229: "Cosug",  230: "Cuqatouzu"
    }
rares = {
    115: "Resaqi",  116: "Romebobi",  117: "Reapu",  118: "Rayujokio",
    119: "Raicooyac",  120: "Rifaaciey",  121: "Rafad",  122: "Riren",
    123: "Rideee",  124: "Rilema",  125: "Rabef",  126: "Rocujob",
    127: "Rorupalor",  128: "Rocowov",  129: "Rokoifouu",  130: "Rageakox",
    131: "Ropaecik",  132: "Roxicu",  133: "Rehezuefel",  134: "Racumoe",
    135: "Rediduiu",  136: "Rawuwe",  137: "Rileneufu",  138: "Roraloh",
    139: "Rilorat",  140: "Ronupoku",  141: "Repipo",  142: "Rubiyewema",
    143: "Riman",  144: "Rooxo",  145: "Repuemizo"
    }
epics = {
    70: "Eviizuu",  71: "Eqoici",  72: "Ecotini",  73: "Esukije",  74: "Elohoukoso",
    75: "Ejuvako",  76: "Eluwusix",  77: "Eqelij",  78: "Elafusij",  79: "Egouli",
    80: "Ekak",  81: "Eheyuvos",  82: "Esexesa",  83: "Eroofia",
    84: "Eqogubaki",  85: "Ecotah",  86: "Elotanig",  87: "Ewosaq",
    88: "Eyuoweq",  89: "Eviauhoh",  90: "Epofeuxa",
    }
legendaries = {
    4: "Xopoc",  5: "Panoli",  6: "Guwoexu",  7: "Megat",  8: "Vaeca",
    9: "Yunao",  10: "Zawixuli",  11: "Ruibupi",  12: "Vaawaw",  13: "Vocuv",
    14: "\[T]/",  15: "Pene",
    }

coins = 1000
price = 100 # The lootbox price

def change_sc():
    input3 = raw_input("What command's shortcut do you want to change?")
    input4 = raw_input("What will be the next shortcut?")

def make_sc_list():
    global commands
    global shortcuts
    s = "The shortcuts are: "
    ind = 0
    for command in commands:
        s = s + "%s '%s', " % (commands[ind], shortcuts[command])
        ind += 1
    return s

def open_a_bunch(x, coins):
    for n in range(int(x)):
        coins = open_lb(coins)
    return coins

def joinlist(lista):
    return ", ".join(lista)

def open_lb(coins): # Opens lootbox
    coins = coins - price
    n = randint(0, 1000)

    if n <= 520:#Shit
        rarity = 1 # 52%
    elif n > 520 and n <= 750:#Common
        rarity = 2 # 23%
    elif n > 750 and n <= 895:#Rare
        rarity = 3 # 14.5%
    elif n > 895 and n <= 985:#Epic
        rarity = 4 # 9%
    elif n > 985 and n <= 1000:#Legendary
        rarity = 5 # 1.5%
    else:
        print "error"

    if rarity == 1: # The item is Shit
        iden = randint(1, 520)
        if iden < 440:
            coins += 20
            counters["shits"] += 1
            print "Congratulations! You earned Shit #%s (20 coins)" % iden
        else:
            if iden == 520:
                coins = coins * 90 / 100
                print "You have acquired %s! (shit, lose 90%% of your coins)" % shits[iden]
                counters["curses"] += 1
            else:
                coins += 25
                counters["named shits"] += 1
                print "You have acquired %s! (Shit, 25 coins)" % shits[iden]
    elif rarity == 2: # The item is Common
        iden = randint(1, 230)
        if iden < 180:
            coins += 110
            counters["commons"] += 1
            print "Congratulations! You earned Common #%s (110 coins)" % iden
        else:
            coins += 130
            counters["named commons"] += 1
            print "You have acquired %s! (Common, 130 coins)" % commons[iden]
    elif rarity == 3: # The item is Rare
        iden = randint(1, 145)
        if iden < 115:
            coins += 165
            counters["rares"] += 1
            print "Congratulations! You earned Rare #%s (165 coins)" % iden
        else:
            coins += 205
            counters["named rares"] += 1
            print "You have acquired %s! (Rare, 205 coins)" % rares[iden]
    elif rarity == 4: # The item is Epic
        iden = randint(1, 90)
        if iden < 70:
            coins += 290
            counters["epics"] += 1
            print "Congratulations! You earned Epic #%s (290 coins)" % iden
        else:
            coins += 350
            counters["named epics"] += 1
            print "You have acquired %s! (Epic, 350 coins)" % epics[iden]
    elif rarity == 5: # The item is Legendary
        iden = randint(1, 15)
        if iden <= 3:
            coins += 680
            counters["legendaries"] += 1
            print "Congratulations! you earned Legendary #%s (680 coins)" % iden
        else:
            if iden != 15:
                coins += 1150
                counters["named legendaries"] += 1
                print "You have acquired %s! (Legendary, 1150 coins)" % legendaries[iden]
            else:
                if coins < 1000:
                    coins = 3000
                    cpene += 1
                    print"You have acquired %s! (Legendary, you now have 3000 coins)" % legendaries[iden]
                else:
                    coins = coins * 1.5
                    counters["penes"] += 1
                    print "You have acquired %s! (Legendary, your coins have been multipled by 1.5)" % legendaries[iden]

    if coins < price: # Run out of coins
        print "Game Over"
        return 0

    return coins

game_still_on = True
while game_still_on == True: # Inputs
    print
    input1 = str(raw_input("What do you want to do? ")) # Asks for inputs

    if input1 == "exit" or input1 == "GG" or input1 == shortcuts["exit"]: # Exits the game
        game_still_on = False
    elif input1 == "open" or input1 == shortcuts["open"]: # Opens lootbox
        coins = open_lb(coins)
        if coins == 0:
            will_to_continue = rawinput("Do you want to restart?[Y/N] ")
            if will_to_continue == "Y":
                coins = 1000
            elif will_to_continue == "N":
                game_still_on = False
                break
    elif input1 == "check coins" or input1 == shortcuts["check coins"]: # Checks coins
        print "Your wallet: %s" % int(coins)
    elif input1 == "help" or input1 == shortcuts["help"]:
        print "All available commands at the moment: %s" % joinlist(commands) # Types the commands
    elif input1 == "open a bunch" or input1 == shortcuts["open a bunch"]:
        enoughcoins = False
        while enoughcoins == False:
            input2 = raw_input("How many lootboxes would you like to open? ")
            if input2.isdigit():
                tries = int(input2)
                if tries <= 0:
                    enoughcoins = True
                    print
                elif coins / tries < price:
                    print "You don't have enough coins to do that!"
                else:
                    enoughcoins = True
                    coins = open_a_bunch(tries, coins)
                    if coins == 0:
                        will_to_continue = rawinput("Do you want to restart?[Y/N] ")
                        if will_to_continue == "Y":
                            coins = 1000
                        elif will_to_continue == "N":
                            game_still_on = False
                            break
            else:
                print "that is not a valid input!" # Opens more than one
    elif input1 == "check inventory" or input1 == shortcuts["check inventory"]:# Checks inventory
        print "You have obtained %s normal and %s named shits" % (counters["shits"], counters["named shits"])
        print "You have obtained %s normal and %s named commons" % (counters["commons"], counters["named commons"])
        print "You have obtained %s normal and %s named rares" % (counters["rares"], counters["named rares"])
        print "You have obtained %s normal and %s named epics" % (counters["epics"], counters["named epics"])
        print "You have obtained %s normal and %s named legendaries" % (counters["legendaries"], counters["named legendaries"])
        print "You have obtained %s penes" % counters["penes"]
        print "You have obtained %s curses" % counters["curses"]
    elif input1 == "shortcuts" or input1 == shortcuts["shortcuts"]:
        print make_sc_list() # Pritns the shortcuts
    else: # Input check
        print "Your input is not valid"
