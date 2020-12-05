from pygame import *

MoveSpeed=3 #Скорость движения слизня
#Ширина слизня
widthS=10 
#Вывсота слизня
heightS=10
#Цвет слизня
colorS="#3333FF"

class Slime(sprite.Sprite):
    #Конструктор
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        #Точки, в  которых появится слайм
        self.startX=x
        self.startY=y
        #Переменные, отвечающая  за передвижения
        self.moveX=0
        self.moveY=0
        self.image=Surface((widthS,heightS))
        self.image.fill(Color(colorS))
        self.rect=Rect(x,y,widthS,heightS) #Прямоугольный объект, для отслеживания местанахождения слизня

    # Функция обновления слайма при нажатии клавиш
    def update(self,left,right):
        if left:
            self.moveX=-MoveSpeed
        if right:
            self.moveX=+MoveSpeed
        if not(left or right):
            self.moveX=0
        #Аналогично проделываем  результат с rect
        self.rect.x+=self.moveX
        self.rect.y+=self.moveY
    

    # Функция отрисовки слайма на экране
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))


