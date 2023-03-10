import time
import re
import json
config = json.load(open("config.json"))
items = json.load(open("items.json"))
# save = json.load(open("saves/template/map.json")) get save adress

class flow:
    def __init__(self):
        pass

    def sleep():
        time.sleep(config["masterSleep"])
        pass

    def newLine():
        print("\n")
        pass

    def filter(inputString):
        return re.sub(r"[^a-zA-Z0-9 ]", "", inputString)

    def input(prompt):
        return flow.filter(input(prompt)).lower()

    def pressEnter():
        flow.newLine()
        flow.input("[Press enter to continue]")
        pass

    def choose(player, save, options,):
        result = None
        options = list(options)

        flow.newLine()
        flow.sleep()

        print("What do you do?")

        for option in options:
            if option == "search":
                searchTable = map["rooms"][f'x{player.position[0]}y{player.position[1]}']["loot"]
                replacementString = "search ("
                for place in searchTable.keys():
                    replacementString += place
                    replacementString += ", "
                    pass
                replacementString = replacementString[:-2]
                replacementString += ")"
                options[options.index(option)] = replacementString
                pass
            elif option == "go":
                options[options.index(option)] = "go (north, south, west, east)"
                pass
            elif option == "look":
                options[options.index(option)] = "look (north, south, west, east)"
                pass
            elif option == "check":
                options[options.index(option)] = "check (inventory, stats)"
                pass
            elif option == "menu":
                options[options.index(option)] = "menu (save, quit, save & quit)"

        for option in options:
            print("<" + option.title() + ">")

        flow.newLine()
        flow.sleep()

        def saveAndQuitGame(save=False, quit=False):
            if save == True:
                # save game here
                flow.sleep()
                print("Saving game...")
                flow.sleep()
                print("Save failed!")
                return
            if quit == True:
                return SystemExit

        def showCheck():
            print("Check what?")
            print("<Inventory> <Stats> <Back>")
            flow.newLine()
            response = flow.input("...")
            if "bac" in response:
                return flow.choose(player, options)
            elif ("in" or "nv") in response:
                player.showInventory()
            elif ("st" or "at") in response:
                player.showStats()
            pass

        def showMenu():
            print("What do you want to do?")
            print("<Save> <Quit> <Save & Quit> <Back>")
            flow.newLine()
            response = flow.input("... ")
            if "bac" in response:
                return flow.choose(player, options)
            elif ("qui" and "sav") in response:
                saveAndQuitGame(save=True, quit=True)
                pass
            elif "sav" in response:
                saveAndQuitGame(save=True)
                pass
            elif "qui" in response:
                saveAndQuitGame(quit=True)
                pass
            return

        def showSearch():
            lootTable = map["rooms"][f'x{player.position[0]}y{player.position[1]}']["loot"]

            print("What do you want to search?")
            searchOptions = ""
            for element in lootTable.keys():
                searchOptions += f"<{str(element).title()}> "
            print(searchOptions + "<Back>")
            flow.newLine()

            response = flow.input("I want to search the... ")
            
            if "bac" in response:
                return flow.choose(player, options)

            for place in lootTable.keys():
                print(place[:3])
                if place[:3] in response:
                    player.pickUp(items[lootTable[place]])
                    
                    modifiedMap = map.copy()
                    del modifiedMap["rooms"][f'x{player.position[0]}y{player.position[1]}']["loot"][place]
                    json.dump(modifiedMap, open(save.saveAdress, "w"))
                    break
                pass
            pass

        def findKeyword():
            rawInput = flow.input("I want to... ")
            flow.newLine()

            if "chec" and "inve" in rawInput:
                flow.sleep()
                player.showInventory()
                return flow.choose(player, save, options)
            elif "chec" and "stat" in rawInput:
                flow.sleep()
                player.showStats()
                return flow.choose(player, save, options)
            elif "chec" in rawInput:
                flow.sleep()
                showCheck()
                return flow.choose(player, save, options)
            elif "sear" in rawInput:
                flow.sleep()
                showSearch()
                return flow.choose(player, save, options)
            elif "go" in rawInput:
                flow.sleep()
                player.go()
                return flow.choose(player, options)
            elif "look" in rawInput:
                flow.sleep()
                player.look()
                return flow.choose(player, options)
            elif "menu" in rawInput:
                flow.sleep()
                return showMenu()

            print("Please rephrase that.")
            flow.newLine()
            flow.sleep()
            findKeyword()

        return findKeyword()
