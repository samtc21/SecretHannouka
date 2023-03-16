import gc
import random


class Player:
    def __init__(self, playerName, email):
        self.playerName = playerName
        self.email = email
        self.restrictionList = [playerName]
        self.secretPick = ""

    def getMessagePick(self):
        if self.secretPick != "":
            return f"{self.playerName} picked {self.secretPick[0]} !"
        else:
            return f"you haven't picked anyone yet!"

    def pick(self, unpicked):
        playerPickable = [x for x in unpicked if x not in self.restrictionList]
        self.secretPick = random.choices(playerPickable, weights=None, k=1)
        unpicked.remove(self.secretPick[0])

    def getName(self):
        return self.playerName

    def getPick(self):
        return self.secretPick

    def getMail(self):
        return self.email

    def addRestriction(self, restriction):
        if restriction not in self.restrictionList:
            self.restrictionList.append(restriction)
            return(f"{restriction} added sucessfuly from restriction list ")
        else:
            return(f"{restriction} already exists in restriction list")

    def removeRestriction(self, restriction):
        if restriction in self.restrictionList:
            self.restrictionList.remove(restriction)
            return(f"{restriction} remove sucessfuly from restriction list ")
        else:
            return(f"{restriction} doest not exist in restriction list")

