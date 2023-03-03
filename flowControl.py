import time
import json
config = json.load(open("config.json"))


class flow:
    def __init__(self):
        pass

    def sleep():
        time.sleep(config["masterSleep"])
        pass

    def newLine():
        print("\n")
        pass

    def pressEnter():
        flow.newLine()
        input("[Press enter to continue]")
        pass

    def choose(player, *options):
        presets = ("go", "look", "check")
        print("What do you do?")

        for option in options:
            if option == "go":
                option = "go (north, south, west, east)"
                pass
            elif option == "look":
                option = "look (north, south, west, east)"
                pass
            elif option == "check":
                option = "check (inventory, stats)"
                pass

            print("<" + option.title() + ">")
            pass

        flow.sleep()
        flow.newLine()

        def showStats():
            print("Yes, here you go.")
            pass

        def showInventory():
            flow.newLine()
            print("Yes, here you go.")
            print(player.inventory)
            pass

        def findKeyword():
            rawInput = input("I want to... ").lower()
            
            if "chec" and "inve" in rawInput:
                showInventory()
                return
            elif "chec" and "stat" in rawInput:
                showStats()
                return
            elif "chec" in rawInput:
                flow.newLine()
                print("Check what?")
                print("<Inventory> <Stats>")
                flow.newLine()
                response = input("...").lower()
                if "inve" in response:
                    showInventory()
                    return
                elif "stat" in response:
                    showStats()
                    return

            print("Please rephrase that.")
            flow.newLine()
            flow.sleep()
            findKeyword()

        findKeyword()