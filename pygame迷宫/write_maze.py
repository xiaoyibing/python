import random

road=[]
road1=[]
road3 = []
n=0
class Maze:
    def __init__(self, x, y):
        # self.maze=0
        self.visited = False#判断之前是否已经访问过
        self.x,self.y = x,y#坐标
        #寻找相邻的1
        self.neighbors = []
    def nei(self):
        self.moves = [[0, 2], [0, -2], [2, 0], [-2, 0]]
        for move in self.moves:
            if 0 < self.x + move[0] < MIX and 0 < self.y + move[1] < MIX :
                self.neighbors.append([self.x + move[0], self.y + move[1]])
    def first(self):
        maze[1][1].visited = True
        for i in range(MIX):
            for j in range(MIX):
                if i % 2 == 1 and j % 2 == 1:
                    if [1, 1] in maze[i][j].neighbors:
                        maze[i][j].neighbors.remove([1, 1])
        road1.append([0,1])
        road1.append([1, 1])
        maze[1][1].connect()

    def connect(self):
        global road
        global road1
        global n
        if n!=(MIX//2)*(MIX//2):
            if len(self.neighbors)!=0:
                self.neighbor = random.choice(self.neighbors)
                if maze[self.neighbor[0]][self.neighbor[1]].visited==False:
                    road1.append([(self.neighbor[0] + self.x) // 2, (self.neighbor[1] + self.y) // 2])
                    road.append(self.neighbor)
                    road1.append(self.neighbor)
                    # print(road)
                    n+=1

                    maze[self.neighbor[0]][self.neighbor[1]].visited = True
                    for i in range(MIX):
                        for j in range(MIX):
                            if i % 2 == 1 and j % 2 == 1:
                                if self.neighbor in maze[i][j].neighbors:
                                    maze[i][j].neighbors.remove(self.neighbor)


                    maze[self.neighbor[1]][self.neighbor[0]].connect()

            else:
                if len(road)!=0:
                    end=road[-1]
                    # print(end)
                    del road[-1]
                    maze[end[1]][end[0]].connect()
                else:
                    pass
        else:
            pass
class Wall_2:
    def __init__(self):
        global maze
        maze = [[Maze(x,y) for x in range(MIX)] for y in range(MIX)]
        for i in range(MIX):
            for j in range(MIX):
                if i%2==1 and j%2==1:
                    # maze[i][j].maze=1
                    maze[i][j].nei()

        maze[1][1].first()
        road1.append([MIX-1,MIX-2])
        for i in range(MIX):
            for j in range(MIX):
                if [i,j] not in road1:
                    road3.append([i,j])
# Wall_2()
class Diferent:
    def __init__(self):
        pass
    def nan1(self):
        global MIX
        MIX = 11
        Wall_2()
    def nan2(self):
        global MIX
        MIX = 21
        Wall_2()
