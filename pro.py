import pyxel
import math
import random


pyxel.init(200,200)
pyxel.cls(7)
pyxel.mouse(True)

a=0
b=0
masu=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
x=0
y=0

class Gameover:
    def __init__(self):
        #gameover時の処理を追加




class App:
    def __init__(self):

        self.scene = 0　#スタート＝0、ゲーム＝1、ゲームオーバー＝2
        self.a = 0
        self.b = 0
        self.score = 0
        self.count = 0
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
                #右を押されたときの処理を追加
            if pyxel.btnp(pyxel.KEY_LEFT):
                #左を押されたときの処理を追加
            if pyxel.btnp(pyxel.KEY_UP):
                #上を押されたときの処理を追加
            if pyxel.btnp(pyxel.KEY_RIGHT):
                #下を押されたときの処理を追加
            



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
                    #グリッドの良いぎ
            pyxel.text(5,5,'2048',0)

            
App()
