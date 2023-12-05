import pyxel
import math
import random

a=0
b=0
masu=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
x=0
y=0


pyxel.init(200,200)
pyxel.cls(7)
pyxel.mouse(True)

class Tumi:
    def hanntei(self,masu):
        self.tumi = 1
        for x in range(4):
            for y in range(4):
                if masu[x][y] == 0:
                    self.tumi = 0
        return self.tumi


class App:
    def __init__(self):

        self.scene = 0
        self.a = 0
        self.b = 0
        self.score = 0
        self.count = 0
        self.tumi = Tumi()
        pyxel.run(self.update,self.draw)


    def update(self):
        if self.scene == 0:
            pyxel.mouse(True)
            if ((50 <= pyxel.mouse_x <= 150) and (50 <= pyxel.mouse_y <= 150)) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): #　マウス座標を使用している
                self.scene = 1
                pyxel.mouse(False)
        if self.scene == 1:
            
            if self.count == 0:
                for x in range(4):
                    for y in range (4):
                        masu[x][y]=0
                self.score=0
                self.score += 1
                masu[pyxel.rndi(0,3)][pyxel.rndi(0,3)] = int(pyxel.rndi(11,20)/10)*2
                self.count += 1


            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.score += 1
                for x in range(4):
                    y = 0
                    for y in range(3):
                        while(masu[x][2 - y] >=2 and masu[x][3 - y] == 0):
                            masu[x][3 - y] = masu[x][2 - y]
                            masu[x][2 - y] = 0
                            y -= 1
                            if y == -1:
                                break
                for x in range(4):
                    for y in range (3):
                        if masu[x][3-y] == masu[x][2-y]:
                            masu[x][3-y] = 2*masu[x][3-y]
                            masu[x][2-y] = 0

                for x in range(4):
                    y = 0
                    for y in range(3):
                        while(masu[x][2 - y] >=2 and masu[x][3 - y] == 0):
                            masu[x][3 - y] = masu[x][2 - y]
                            masu[x][2 - y] = 0
                            y -= 1
                            if y == -1:
                                break
                self.tumi.tumi=self.tumi.hanntei(masu)
                if self.tumi.tumi==0:
                    xx = 0
                    while(xx==0):
                        g=pyxel.rndi(0,3)
                        h=pyxel.rndi(0,3)

                        if masu[g][h] == 0:
                            masu[g][h]=int(pyxel.rndi(11,20)/10)*2
                            xx=1
                else:
                    self.scene = 2
                    pyxel.mouse(True)

            if pyxel.btnp(pyxel.KEY_LEFT):
                self.score += 1
                for x in range(4):
                    y = 0
                    for y in range(3):
                        while(masu[x][y + 1] >=2 and masu[x][y] == 0):
                            masu[x][y] = masu[x][y + 1]
                            masu[x][y + 1] = 0
                            y -= 1
                            if y == -1:
                                break
                for x in range(4):
                    for y in range (3):
                        if masu[x][y] == masu[x][y+1]:
                            masu[x][y] = 2*masu[x][y+1]
                            masu[x][y+1] = 0

                for x in range(4):
                    y = 0
                    for y in range(3):
                        while(masu[x][y + 1] >=2 and masu[x][y] == 0):
                            masu[x][y] = masu[x][y + 1]
                            masu[x][y + 1] = 0
                            y -= 1
                            if y == -1:
                                break
                self.tumi.tumi=self.tumi.hanntei(masu)
                if self.tumi.tumi==0:
                    xx = 0
                    while(xx==0):
                        g=pyxel.rndi(0,3)
                        h=pyxel.rndi(0,3)

                        if masu[g][h] == 0:
                            masu[g][h]=int(pyxel.rndi(11,20)/10)*2
                            xx=1
                else:
                    self.scene = 2
                    pyxel.mouse(True)

            
                            
            if pyxel.btnp(pyxel.KEY_UP):
                self.score += 1
                for y in range(4):
                    x = 0
                    for x in range(3):
                        while(masu[x+1][y] >=2 and masu[x][y] == 0):
                            masu[x][y] = masu[x+1][y]
                            masu[x+1][y] = 0
                            x -= 1
                            if x == -1:
                                break
                for y in range(4):
                    for x in range (3):
                        if masu[x][y] == masu[x+1][y]:
                            masu[x][y] = 2*masu[x+1][y]
                            masu[x+1][y] = 0

                for y in range(4):
                    x = 0
                    for x in range(3):
                        while(masu[x+1][y] >=2 and masu[x][y] == 0):
                            masu[x][y] = masu[x+1][y]
                            masu[x+1][y] = 0
                            x -= 1
                            if x == -1:
                                break
                self.tumi.tumi=self.tumi.hanntei(masu)
                if self.tumi.tumi==0:
                    xx = 0
                    while(xx==0):
                        g=pyxel.rndi(0,3)
                        h=pyxel.rndi(0,3)

                        if masu[g][h] == 0:
                            masu[g][h]=int(pyxel.rndi(11,20)/10)*2
                            xx=1
                else:
                    self.scene = 2
                    pyxel.mouse(True)
            
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.score += 1
                for y in range(4):
                    x = 0
                    for x in range(3):
                        while(masu[2-x][y] >=2 and masu[3-x][y] == 0):
                            masu[3-x][y] = masu[2-x][y]
                            masu[2-x][y] = 0
                            x -= 1
                            if x == -1:
                                break
                for y in range(4):
                    for x in range (3):
                        if masu[3-x][y] == masu[2-x][y]:
                            masu[3-x][y] = 2*masu[3-x][y]
                            masu[2-x][y] = 0

                for y in range(4):
                    x = 0
                    for x in range(3):
                        while(masu[2-x][y] >=2 and masu[3-x][y] == 0):
                            masu[3-x][y] = masu[2-x][y]
                            masu[2-x][y] = 0
                            x -= 1
                            if x == -1:
                                break
                self.tumi.tumi=self.tumi.hanntei(masu)
                if self.tumi.tumi==0:
                    xx = 0
                    while(xx==0):
                        g=pyxel.rndi(0,3)
                        h=pyxel.rndi(0,3)

                        if masu[g][h] == 0:
                            masu[g][h]=int(pyxel.rndi(11,20)/10)*2
                            xx=1
                else:
                    self.scene = 2
                    pyxel.mouse(True)


            for x in range(4):
                for y in range(4):
                    if masu[x][y] >= 2048:
                        self.scene = 3

        if self.scene == 2:
            if ((0 <= pyxel.mouse_x <= 200) and (0 <= pyxel.mouse_y <= 200)) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): #　マウス座標を使用している
                self.scene = 0
                self.count = 0
                pyxel.mouse(False)
        

                        
                        
                
       


    def draw(self):
        if self.scene == 0:
            pyxel.cls(7)
            pyxel.rect(50,50,100,100,8)
            pyxel.text(90,97,'start',0)
        if self.scene == 1:
            pyxel.rect(20,20,160,160,14)
            for a in range(4):
                for b in range(4):
                    pyxel.rect(32+37*a,32+37*b,25,25,7)
            pyxel.text(5,5,'2048',0)
            
            for x in range(4):
                for y in range(4):
                    if masu[y][x]==0:
                        pyxel.text(42+37*x,42+37*y,str(masu[y][x]),7)
                    elif masu[y][x]==2:
                        pyxel.text(42+37*x,42+37*y,str(masu[y][x]),3)
                    elif masu[y][x]==4:
                        pyxel.text(42+37*x,42+37*y,str(masu[y][x]),2)
                    elif masu[y][x]==8:
                        pyxel.text(42+37*x,42+37*y,str(masu[y][x]),1)
                    elif masu[y][x]==16:
                        pyxel.text(42+37*x,42+37*y,str(masu[y][x]),4)
                    elif masu[y][x]==32:
                        pyxel.text(42+37*x,42+37*y,str(masu[y][x]),5)
                    elif masu[y][x]==64:
                        pyxel.text(42+37*x,42+37*y,str(masu[y][x]),6)
                    elif masu[y][x]==128:
                        pyxel.text(38+37*x,42+37*y,str(masu[y][x]),8)
                    elif masu[y][x]==256:
                        pyxel.text(38+37*x,42+37*y,str(masu[y][x]),9)
                    else:
                        pyxel.text(38+37*x,42+37*y,str(masu[y][x]),0)
        if self.scene == 2:
            pyxel.cls(7)
            pyxel.rect(50,50,100,100,12)
            pyxel.text(80,97,'game over',0)
            pyxel.text(80,105,('score:' + str(self.score) ),0)
        if self.scene == 3:
            pyxel.rect(50,50,100,100,12)
            pyxel.text(80,97,'game clear',0)
            pyxel.text(80,105,('score:' + str(self.score) ),0)

App()
