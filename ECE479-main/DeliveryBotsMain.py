from math import sqrt
import MapClass
import BotClass
import tkinter as tk # for gui
from enum import Enum

def main():

    map = MapClass.Map(15,15)
    roboto = BotClass.Bot(0,0, map)
    obstacles = [False, False, False, False]
    #########    left  right  forward  back
    direction = [False, False, False, False]

    def generateMap():
        map.mapReset()
        map.generateObstacles((map.length/3))
        roboto.generateGoal(map)
        map.generateGoal(roboto)
        map.generateBot(roboto, window)
        map.printMap(window)

    def moveBot():
        # Algorithim goes here 
        moving = True
        getDirection(map, roboto)
        i = 0
        while moving == True and i <= 40:
            i = i + 1
            checkEnviro(map, roboto)
            #getDirection(map, roboto)
            if roboto.getX() == roboto.goal[0] and roboto.getY() == roboto.goal[1]:
                map.setValue(roboto.getX(), roboto.getY(), 3)
                moving = False
            elif direction[2] == True:
                map.generateTrail(roboto, window) # before you move set that square to light blue then move
                roboto.moveForward(map)
                map.generateBot(roboto, window)
                map.printMap(window)
            elif direction[1] == True:
                map.generateTrail(roboto, window) # before you move set that square to light blue then move
                roboto.moveRight(map)
                map.generateBot(roboto, window)
                map.printMap(window)
            elif direction[0] == True:
                map.generateTrail(roboto, window) # before you move set that square to light blue then move
                roboto.moveLeft(map)
                map.generateBot(roboto, window)
                map.printMap(window)
            elif direction[3] == True:
                map.generateTrail(roboto, window) # before you move set that square to light blue then move
                roboto.moveBack(map)
                map.generateBot(roboto, window)
                map.printMap(window)
            else:
                moving = False
            getDirection(map, roboto)
        map.printMap(window)
        return        
       
    def getDirection(map, roboto):
        location = [roboto.getX(),roboto.getY()]
        tempL = location[:] # [:] makes it so that the copy does not affect the original
        goalLoc = [roboto.goal[0],roboto.goal[1]]
        direction[0] = False #left
        direction[1] = False #right
        direction[2] = False #up
        direction[3] = False #down
        checkEnviro(map, roboto)

        ############# Hypotnuse Hueristic ###################

        best = 0
        tempL[0] = location[0] - 1
        temp1 = getHypo(tempL, goalLoc)

        tempL = location[:]
        tempL[0] = location[0] + 1
        temp2 = getHypo(tempL, goalLoc)

        if obstacles[0] == True:
            temp1 = 100

        if temp2 <= temp1: # if the hypotnuse to go left is bigger than to go right direction is set to right
            if obstacles[1] == False: #right
                best = 1
                temp1 = temp2
                
        tempL = location[:]
        tempL[0] = location[0]  
        tempL[1] = location[1] - 1
        temp2 = getHypo(tempL, goalLoc)

        if temp2 <= temp1: #forward
            if obstacles[2] == False:
                best = 2
                temp1 = temp2

        # if obstacles[0] == True and best == 0:
        #     if obstacles[2] == True: 
        #         if map.getValue(location[0] - 1,location[1]) != 2:
        #             best = 0
        #         else:
        #             best = 3
        #     else:
        #         best = 2

        ################### Wall Checking ######################

        match best:
            case 0: # wants to go left
                if map.getValue(location[0] - 1, location[1]) == 2: #already been to the left
                    if map.getValue(location[0] + 1, location[1]) == 2:
                        best = 3
                    else:
                        best = 1 # back up 
            case 1: #wants to go right
                if map.getValue(location[0] + 1, location[1]) == 2: #already been right
                    if map.getValue(location[0] - 1, location[1]) == 2: 
                        best = 3 # if its also been left then it back up 
                    else:
                        best = 0 # otherwise is goes left
            case 2: #wants to go forward
                if map.getValue(location[0], location[1] - 1) == 2: # already been forward
                    if map.getValue(location[0] + 1, location[1]) == 2 and map.getValue(location[0] - 1, location[1]) == 2:
                        best = 3
                    elif map.getValue(location[0] + 1, location[1]) == 2:
                        best = 0 
                    else:
                        best = 1 
            case 3: 
                best = 3
            
        if obstacles[0] == True and best == 0:
            if obstacles[1] != True: #backward
                if map.getValue(location[0] - 1,location[1]) != 2:
                    best = 0
                else:
                    best = 3
            else:
                best = 3
        direction[best] = True

    def getHypo(location, goalLoc):
        return sqrt((abs(goalLoc[0] - location[0]))**2 + (abs(goalLoc[1] - location[1]))**2)

    def checkEnviro(map, roboto):
        #            left   right  above  below
        location = [roboto.getX(),roboto.getY()]
        obstacles[0] = False #left
        obstacles[1] = False #right
        obstacles[2] = False #above
        obstacles[3] = False #below

        if map.getValue(location[0] - 1, location[1]) == "x" or location[0] == 0:
            obstacles[0] = True

        if map.getValue(location[0] + 1, location[1]) == "x" or location[0] == map.length:
            obstacles[1] = True

        if map.getValue(location[0], location[1] - 1) == "x":
            obstacles[2] = True

        if location[1] != (map.height - 1):
            if map.getValue(location[0], location[1] + 1) == "x":
                obstacles[3] = True
        else:
            obstacles[3] = True
        return
        #return obstacles

    #generate window
    window = tk.Tk()

    #button component
    startButton = tk.Button(
        text="New Map",
        width=10, 
        height=5,
        command = generateMap,
    )

    Button = tk.Button(
        text="Move",
        width=10, 
        height=5,
        command = moveBot,
    )

    #adding to frame
    Button.grid(row = map.length, column = int(map.length/2 - 4), columnspan = 4, pady = 2, padx = 2)
    startButton.grid(row = map.length, column = int(map.length/2), columnspan = 4, pady = 2, padx = 2)
    window.mainloop()

if __name__ == "__main__":
    main()