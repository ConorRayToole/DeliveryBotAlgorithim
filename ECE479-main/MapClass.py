import random
import BotClass
import tkinter as tk # for gui

class Map:

    def __init__(self, Length, Height):
        self.length = Length
        self.height = Height
        self.obstacle1 = ["x","x","x"] 
        self.obstacle2 = [["x" for p in range(3)] for k in range(3)]
        self.map = [[0 for i in range(self.length)] for j in range(self.height)]
    
    def getLength(self):
        return self.length

    def printMap(self, window):
        #window = tk.Tk()
        for i in range(self.length):
            for j in range(self.height):
                # gui
                temp = self.map[i][j]
                frame = self.createTile(temp, window)
                frame.grid( row = j, column = i, pady = 2, padx = 2)
                # end of gui
                
                #print (self.map[i][j], " ",end="")
            #print("")

        #window.update()

    def updateMap(self, window):
        window.update()

    def generateObstacles(self, repeat):
        count = 0

        while count < repeat:
            #generates random start coordinate for wall
            numV = random.randint(1, (self.length - 4)) #length - 5 prevents the obstacle from exsisting over the grid wall                  
            numH = random.randint(1, (self.length - 4))
            #generates random start coordinate for cube
            num2V = random.randint(1, (self.length - 4))                   
            num2H = random.randint(1, (self.length - 4))
            
            #generates 3 space wall
            for H in range(3):       
                # map[horizontal][vertical]; H for horizontal; V for vertical
                self.map[numV+H][numH] = self.obstacle1[H - 1] # -1 prevents index out of range
            
            #this next portion is to generate the 3x3 squares
            H = 0
            for H in range(3):
                for V in range(3):
                    self.map[num2V + V][num2H + H] = self.obstacle2[H - 1][V - 1]
            
            count = count + 1

    def generateBot(self, roboto, window):
        #roboto = BotClass.Bot(0,0)
        self.map[roboto.getX()][roboto.getY()] = 1
        window.update()

    def mapReset(self):
        self.map = [[0 for i in range(self.length)] for j in range(self.height)]

    def createTile(self, type, parent):
        if type == "x":
            color = "red"
        if type == 0:
            color = "gray15"
        if type == 1:
            color = "blue"
        if type == 2:
            color = "cadetblue1"
        if type == 3:
            color = "green"

        frame = tk.Frame(parent, bg=color, width=20, height=20,)
        return frame
    
    def getValue(self, x, y):
        return self.map[x][y]
    
    def setValue(self, x, y, z):
        self.map[x][y] = z
    
    def generateTrail(self, roboto, window):
        self.map[roboto.getX()][roboto.getY()] = 2
        window.update()

    def generateGoal(self, roboto):
        numV = roboto.goal[1]
        numH = roboto.goal[0]

        self.map[numH][numV] = 3