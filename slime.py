from pygame import *
import pyganim
mixer.pre_init(44100, -16, 2, 512)
mixer.init()
#Скорость движения слизня
MoveSpeed=5
#Сила прыжка
jumpPower=11
#Гравитация(потом нужно подогнать под реальную)
gravity=0.3
#Задержка анимации
AnimationDelay=0.1
AnStay=['animation/slime/stay0.png']

AnStayLeft = ['animation/slime/slimeStayLeft.png']

AnStayRight = ['animation/slime/slimeStayRight.png']

AnStayUp = ['animation/slime/slimeStayUp.png']

#Добавляю анимации
AnRight =['animation/slime/slimeRight1.png',
          'animation/slime/slimeRight2.png',
          'animation/slime/slimeRight3.png',
          'animation/slime/slimeRight4.png']
           
AnLeft = ['animation/slime/slimeLeft1.png',
          'animation/slime/slimeLeft2.png',
          'animation/slime/slimeLeft3.png',
          'animation/slime/slimeLeft4.png']

AnJump = ['animation/slime/slimeJump1.png',
          'animation/slime/slimeJump2.png',
          'animation/slime/slimeJump3.png',
          'animation/slime/slimeJump4.png']

AnLeftUp = ['animation/slime/slimeLeftUp1.png',
            'animation/slime/slimeLeftUp2.png',
            'animation/slime/slimeLeftUp3.png',
            'animation/slime/slimeLeftUp4.png']

AnLeftDown = ['animation/slime/slimeLeftDown1.png',
              'animation/slime/slimeLeftDown2.png',
              'animation/slime/slimeLeftDown3.png',
              'animation/slime/slimeLeftDown4.png']

AnRightUp = ['animation/slime/slimeRightUp1.png',
             'animation/slime/slimeRightUp2.png',
             'animation/slime/slimeRightUp3.png',
             'animation/slime/slimeRightUp4.png']
             
AnRightDown = ['animation/slime/slimeRightDown1.png',
               'animation/slime/slimeRightDown2.png',
               'animation/slime/slimeRightDown3.png',
               'animation/slime/slimeRightDown4.png']

AnUpLeft = ['animation/slime/slimeUpLeft1.png',
            'animation/slime/slimeUpLeft2.png',
            'animation/slime/slimeUpLeft3.png',
            'animation/slime/slimeUpLeft4.png']

AnUpRight = ['animation/slime/slimeUpRight1.png',
             'animation/slime/slimeUpRight2.png',
             'animation/slime/slimeUpRight3.png',
             'animation/slime/slimeUpRight4.png']

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
        # Проверка у стен ли находится слизень
        self.Right=False
        self.Left=False
        self.Up=False
        # Проверка у стен находится слизень + нажимает ли игрок клавишу
        self.RightPress=False
        self.LeftPress=False
        self.UpPress=False
        #Как выглядит слизень
        self.image=Surface((widthS,heightS))
        
        self.rect=self.image.get_rect() #Прямоугольный объект, для отслеживания местанахождения слизня
        self.rect.x=x
        self.rect.y=y
        # Для отслеживания rect слизня и правильного изменениея rect, в зависимости от обстоятельств
        self.LastRectbottom = self.rect.bottom
        self.LastRectx = self.rect.x #Для левой стены
        self.LastRecty=self.rect.y
        self.LastRectRight=self.rect.right # Для  правой стены
        self.LastRectTop=self.rect.top
        self.LastRectCenterx=self.rect.centerx
        # Закгрузка звука прыжка
        self.SoundJump=mixer.Sound('sounds/slime/jump.wav')
        
        #Функциядля созданий списка анимаций
        def MakeFrameAnim(animWay,delay):
            FrameAnim=[]
            for anim in animWay:
                FrameAnim.append((anim, delay))
            ReadyAnim = pyganim.PygAnimation(FrameAnim)
            return ReadyAnim
        
        #Анимации покоя
        self.PAStay=MakeFrameAnim(AnStay,AnimationDelay)
        self.PAStayRight=MakeFrameAnim(AnStayRight,AnimationDelay)
        self.PAStayLeft=MakeFrameAnim(AnStayLeft,AnimationDelay)
        self.PAStayUp=MakeFrameAnim(AnStayUp,AnimationDelay)

        self.PAStay.play()
        self.PAStayRight.play()
        self.PAStayLeft.play()
        self.PAStayUp.play()
        # Анимация  движения вправо
        self.PARight=MakeFrameAnim(AnRight,AnimationDelay)
        self.PARight.play()

        # Анимация движения влево
        self.PALeft=MakeFrameAnim(AnLeft,AnimationDelay)
        self.PALeft.play()

        #Анимация прыжка
        self.PAJump=MakeFrameAnim(AnJump,AnimationDelay)
        self.PAJump.play()

        #Анимации прилипания и ползанья по стенам
        self.PALeftUp=MakeFrameAnim(AnLeftUp,AnimationDelay)
        self.PALeftDown=MakeFrameAnim(AnLeftDown,AnimationDelay)
        self.PARightUp=MakeFrameAnim(AnRightUp,AnimationDelay)
        self.PARightDown=MakeFrameAnim(AnRightDown,AnimationDelay)

        self.PAUpLeft=MakeFrameAnim(AnUpLeft,AnimationDelay)
        self.PAUpRight=MakeFrameAnim(AnUpRight,AnimationDelay)

        self.PALeftUp.play()
        self.PALeftDown.play()
        self.PARightUp.play()
        self.PARightDown.play()

        self.PAUpLeft.play()
        self.PAUpRight.play()
        

    # Функция обновления слайма при нажатии клавиш
    def update(self,left,right,up,down,jump,platforms,check):
                    
        if self.onGround:
            self.image=Surface((widthS,heightS))
            # Меняем  размер rect
            self.rect=self.image.get_rect()
            # Устанавливаем изменённый rect по правильным координатам
            self.rect.bottom=self.LastRectbottom
            if self.Right:
                self.rect.right = self.LastRectRight
            else:
                self.rect.x = self.LastRectx


        elif not self.onGround and not( self.LeftPress or self.RightPress or self.UpPress):
            self.image = Surface((image.load('animation/slime/slimeJump1.png').get_width(), image.load('animation/slime/slimeJump1.png').get_height()))
            # Меняем  размер rect
            # self.rect = self.image.get_rect()
            self.rect.width=image.load('animation/slime/slimeJump1.png').get_width() #36
            self.rect.height=image.load('animation/slime/slimeJump1.png').get_height() #34
            # Устанавливаем изменённый rect по правильным координатам
            self.rect.bottom=self.LastRectbottom
            if self.Right:
                self.rect.right = self.LastRectRight
            else:
                self.rect.x = self.LastRectx
            
        if not self.onGround and not(self.LeftPress or self.RightPress or self.UpPress):
            self.moveY+=gravity

        if left:
            self.moveX=-MoveSpeed
            if self.onGround:
                self.image.fill((0,0,0))
                self.PALeft.blit(self.image,(0,0))
            elif not self.onGround and not(self.LeftPress or self.RightPress or self.UpPress):
                self.image.fill((0, 0, 0))
                self.PAJump.blit(self.image, (0, 0))
            if self.LeftPress:
                self.image=Surface((image.load('animation/slime/slimeLeftUp1.png').get_width(), image.load('animation/slime/slimeLeftUp1.png').get_height()))
                
                # Меняем  размер rect
                self.rect=self.image.get_rect()
                # Устанавливаем изменённый rect по правильным координатам
                self.rect.x=self.LastRectx
                self.rect.bottom=self.LastRectbottom
                    
                if up:
                    self.moveY=-MoveSpeed
                    self.image.fill((0,0,0))
                    self.PALeftUp.blit(self.image,(0,0))
                if down:
                    self.moveY=+MoveSpeed
                    self.image.fill((0, 0, 0))
                    self.PALeftDown.blit(self.image, (0, 0))
                
                if not(up or down):
                    self.moveY=0
                    self.image.fill((0, 0, 0))
                    self.PAStayLeft.blit(self.image, (0, 0))

            
        if right:
            self.moveX=+MoveSpeed
            if self.onGround:
                self.image.fill((0, 0, 0))
                self.PARight.blit(self.image, (0, 0))
            elif not self.onGround and not(self.LeftPress or self.RightPress or self.UpPress):
                self.image.fill((0, 0, 0))
                self.PAJump.blit(self.image, (0, 0))

            if self.RightPress:
                self.image=Surface((image.load('animation/slime/slimeRightUp1.png').get_width(), image.load('animation/slime/slimeRightUp1.png').get_height()))
                # Меняем  размер rect
                self.rect=self.image.get_rect()
                # Устанавливаем изменённый rect по правильным координатам
                self.rect.right = self.LastRectRight
                self.rect.bottom=self.LastRectbottom
                    
                if up:
                    self.moveY=-MoveSpeed
                    self.image.fill((0,0,0))
                    self.PARightUp.blit(self.image,(0,0))
                if down:
                    self.moveY=+MoveSpeed
                    self.image.fill((0, 0, 0))
                    self.PARightDown.blit(self.image, (0, 0))
                
                if not(up or down):
                    self.moveY=0
                    self.image.fill((0, 0, 0))
                    self.PAStayRight.blit(self.image, (0, 0))
                
        if not(left or right):
            self.moveX=0
            if self.onGround:
                self.image.fill((0, 0, 0))
                self.PAStay.blit(self.image, (0, 0))
            elif not self.onGround:
                self.image.fill((0, 0, 0))
                self.PAJump.blit(self.image, (0, 0))

        if jump:
            if self.onGround:
                self.moveY=-jumpPower
                self.SoundJump.play()
        # if up:
        #     if self.UpPress:
        #         self.image=Surface((image.load('animation/slime/slimeStayUp.png').get_width(), image.load('animation/slime/slimeStayUp.png').get_height()))
        #         # Меняем  размер rect
        #         self.rect.width=45#image.load('animation/slime/slimeJump1.png').get_width() #36
        #         self.rect.height=24#image.load('animation/slime/slimeJump1.png').get_height() #34
        #         # self.rect=self.image.get_rect()
        #         # Устанавливаем изменённый rect по правильным координатам
        #         if left:
        #             self.rect.x=self.LastRectx
        #         elif right:
        #             self.rect.right=self.LastRectRight
        #         else:
        #             self.rect.x=self.LastRectx
        #         # self.rect.x=self.LastRectx
        #         self.rect.top=self.LastRectTop

        #         if left:
        #             self.moveX=-MoveSpeed
        #             self.image.fill((0,0,0))
        #             self.PAUpLeft.blit(self.image,(0,0))
        #         if right:
        #             self.moveX=+MoveSpeed
        #             self.image.fill((0, 0, 0))
        #             self.PAUpRight.blit(self.image, (0, 0))
                
        #         if not(left or right):
        #             self.moveY=0
        #             self.image.fill((0, 0, 0))
        #             self.PAStayUp.blit(self.image, (0, 0))  


        # Чтобы всегда работала гравитация и  столкновения со стенами
        self.onGround=False
        
        self.Right=False
        self.Left=False
        self.Up=False
        self.RightPress=False
        self.LeftPress=False
        self.UpPress=False
        #Аналогично проделываем  результат с rect, добавляем взаимодействие rect с поверхностью
        self.rect.x+=self.moveX
        self.collide(self.moveX,0,platforms) #Проверка пересечения по горизонтали
        self.rect.y+=self.moveY 
        self.collide(0,self.moveY,platforms) #Проверка пересечения по вертикали
        # Для того, чтобы можно было увидеть rect
        if  check:
            self.image.fill(('#FFFFFF'))
        # Обновлением точек, по которым устанавливается rect
        self.LastRectbottom = self.rect.bottom
        self.LastRectx = self.rect.x #Для левой стены
        self.LastRecty=self.rect.y
        self.LastRectRight=self.rect.right # Для  правой стены
        self.LastRectTop=self.rect.top
        self.LastRectCenterx=self.rect.centerx
        
        #print(self.rect.right," ",self.rect.topright," ",self.UpPress)
    
    # Функция обработки столкновений с препятствиями
    def collide(self,moveX,moveY,platforms):
        for each in platforms:
            # Если есть столкновение
            if sprite.collide_rect(self,each):
                if moveX>0:
                    self.rect.right=each.rect.left
                    self.RightPress=True
                if moveX<0:
                    self.rect.left=each.rect.right
                    self.LeftPress=True
                if moveY>0:
                    self.rect.bottom=each.rect.top
                    self.moveY=1
                    self.onGround=True
                if moveY<0:
                    self.rect.top=each.rect.bottom
                    self.moveY=1
                    self.UpPress=True
            if (self.rect.right==each.rect.left):
                self.Right=True
            if (self.rect.left==each.rect.right):
                self.Left=True
            if self.rect.top==each.rect.bottom:
                self.Up=True
