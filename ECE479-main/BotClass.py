import tkinter as tk # for gui
import random
import MapClass

class Bot:
    def __init__(self, x, y, map):
        
        self.start = [map.height - 1,int(map.length/2) - 1]
        self.current = self.start
        self.goal = [y,x]

    def getX(self):
        return self.current[1]
    
    def getY(self):
        return self.current[0]

    def moveRight(self, map):
        tempH = self.current[1]
        tempV = self.current[0]
        value = map.getValue(tempH+1, tempV)

        if tempH + 1 > map.length:
            self.current = self.current
            return False
        elif value == "x":
            self.current = self.current
            return False
        else:
            self.current[1] = tempH + 1
            return True
        
    def moveLeft(self, map):
        tempH = self.current[1]
        tempV = self.current[0]
        value = map.getValue(tempH - 1, tempV)

        if tempH - 1 < 0:
            self.current = self.current
            return False
        elif value == "x":
            self.current = self.current
            return False
        else:
            self.current[1] = tempH - 1
            return True
        
    def moveForward(self, map):
        tempH = self.current[1]
        tempV = self.current[0]
        value = map.getValue(tempH, tempV - 1)

        if tempV - 1 < 0:
            self.current = self.current
            return False
        elif value == "x":
            self.current = self.current
            return False
        else:
            self.current[0] = tempV - 1
            return True
        
    def moveBack(self, map):
        tempH = self.current[1]
        tempV = self.current[0]
        value = map.getValue(tempH, tempV + 1)

        if tempV + 1 > map.height:
            self.current = self.current
            return False
        elif value == "x":
            self.current = self.current
            return False
        else:
            self.current[0] = tempV + 1
            return True
        
    def generateGoal(self, map):
        numV = random.randint(1, 4) 
        numH = random.randint(1, (map.length - 1))

        self.goal = [numH,numV]