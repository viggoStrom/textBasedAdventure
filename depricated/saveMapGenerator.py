import random
import datetime
import re
import json
import shutil

import flowControl
flow = flowControl.flow


class map():
    def __init__(self, survivor):
        def generateAdress():
            num = random.randbytes(8)
            num = str(abs(hash(survivor.name + str(num))))

            date = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S-")

            playerName = re.sub(r"[^a-zA-Z]", "", survivor.name)

            saveAdress = f'saves/{date}{playerName}{num}.json'

            try:
                open(saveAdress, "x")
                # flow.sleep()
                # flow.newLine()
                # print("[Saved successfully]")
                pass
            except:
                generateAdress()

            return saveAdress

        self.saveAdress = generateAdress()

        try:
            shutil.copy("saveTemplate.json", self.saveAdress)
        except:
            print("Error: Files missing... (./saveTemplate.json)")
            SystemExit

        # code that writes to json
        save = json.load(open(self.saveAdress))
        save["player"]["position"] = survivor.position
        json.dump(save, open(self.saveAdress, "w"))
        pass