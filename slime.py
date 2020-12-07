from pygame import *
#Скорость движения слизня
MoveSpeed=5
#Сила прыжка
jumpPower=15
#Гравитация(потом нужно подогнатьпод реальную)
gravity=0.3


#Ширина слизня
widthS=20
#Высота слизня
heightS=20
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
        #Для проверки на земле ли находится слизень
        self.onGround=False
        #Как выглядит слизень
        self.image=Surface((widthS,heightS))
        self.image.fill(Color(colorS))
        self.rect=Rect(x,y,widthS,heightS) #Прямоугольный объект, для отслеживания местанахождения слизня(нужно заменить на овал)

    # Функция обновления слайма при нажатии клавиш
    def update(self,left,right,jump,platforms):
        if left:
            self.moveX=-MoveSpeed
        if right:
            self.moveX=+MoveSpeed
        if not(left or right):
            self.moveX=0
        if jump:
            if self.onGround:
                self.moveY=-jumpPower
        if not self.onGround:
            self.moveY+=gravity
        # Чтобы всегда работала гравитация
        self.onGround=False
        #Аналогично проделываем  результат с rect, добавляем взаимодействие rect с поверхностью
        self.rect.x+=self.moveX
        self.collide(self.moveX,0,platforms) #Проверка пересечения по горизонтали
        self.rect.y+=self.moveY 
        self.collide(0,self.moveY,platforms) #Проверка пересечения по вертикали
    
    # Функция обработки столкновений с препятствиями
    def collide(self,moveX,moveY,platforms):
        for each in platforms:
            # Если есть столкновение
            if sprite.collide_rect(self,each):
                if moveX>0:
                    self.rect.right=each.rect.left
                if moveX<0:
                    self.rect.left=each.rect.right
                if moveY>0:
                    self.rect.bottom=each.rect.top
                    self.moveY=0
                    self.onGround=True
                if moveY<0:
                    self.rect.top=each.rect.bottom
                    self.moveY=0