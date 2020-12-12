from pygame import *
import pyganim
#Скорость движения слизня
MoveSpeed=5
#Сила прыжка
jumpPower=15
#Гравитация(потом нужно подогнатьпод реальную)
gravity=0.3
#Задержка анимации
AnimationDelay=0.1
AnStay=['animation/slime/stay0.png']

#Добавляю анимации
AnRight =['animation/slime/slimeRight1.png',
          'animation/slime/slimeRight2.png',
          'animation/slime/slimeRight3.png',
          'animation/slime/slimeRight4.png']
           
AnLeft = ['animation/slime/slimeLeft1.png',
          'animation/slime/slimeLeft2.png',
          'animation/slime/slimeLeft3.png',
          'animation/slime/slimeLeft4.png']

#Ширина слизня
widthS=image.load('animation/slime/stay0.png').get_width()
#Высота слизня
heightS=image.load('animation/slime/stay0.png').get_height()
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
        
        self.rect=self.image.get_rect() #Прямоугольный объект, для отслеживания местанахождения слизня
        self.rect.x=x
        self.rect.y=y
        
        #Функциядля созданий списка анимаций
        def MakeFrameAnim(animWay,delay):
            FrameAnim=[]
            for anim in animWay:
                FrameAnim.append((anim, delay))
            ReadyAnim = pyganim.PygAnimation(FrameAnim)
            return ReadyAnim
        
        #Анимация покоя
        self.PAStay=MakeFrameAnim(AnStay,AnimationDelay)
        self.PAStay.play()

        # Анимация  движения вправо
        self.PARight=MakeFrameAnim(AnRight,AnimationDelay)
        self.PARight.play()

        # Анимация движения влево
        self.PALeft=MakeFrameAnim(AnLeft,AnimationDelay)
        self.PALeft.play()

    # Функция обновления слайма при нажатии клавиш
    def update(self,left,right,jump,platforms):
        if left:
            self.moveX=-MoveSpeed
            self.image.fill((0,0,0))
            self.PALeft.blit(self.image,(0,0))
        if right:
            self.moveX=+MoveSpeed
            self.image.fill((0,0,0))
            self.PARight.blit(self.image,(0,0))
        if not(left or right):
            self.moveX=0
            if not jump:
                self.image.fill((0,0,0))
                self.PAStay.blit(self.image,(0,0))
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
