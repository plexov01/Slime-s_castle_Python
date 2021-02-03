from pygame import *
import pyganim
mixer.pre_init(44100, -16, 2, 512)
mixer.init()
#Скорость движения слизня
MoveSpeed=5
#Сила прыжка
jumpPower=11
#Гравитация(потом нужно подогнать под реальную)
gravity=0.35
#Задержка анимации
AnimationDelay=0.1
AnStay=['animation/slime/stay.png']

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
widthS=image.load('animation/slime/stay.png').get_width()
#Высота слизня
heightS=image.load('animation/slime/stay.png').get_height()
#Цвет слизня
colorS="#444444"

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
        #Размеры слизня в зависимости от поеверхности
        self.SizeGroundWidth=widthS
        self.SizeGroundHeight=heightS

        self.SizeByWallWidth=image.load('animation/slime/slimeLeftUp1.png').get_width()
        self.SizeByWallHeight=image.load('animation/slime/slimeLeftUp1.png').get_height()

        self.SizeJumpWidth=image.load('animation/slime/slimeJump1.png').get_width()
        self.SizeJumpHeight=image.load('animation/slime/slimeJump1.png').get_height()
        # Для выносливости
        self.stamina=100 # Изменяется от 0 до 100
        self.AllowIncrease=True # Переменная, которая разрешает востанавливать выносливость или запрещает
        self.CheckTimeAllowIncrease=0 # Вспомогательная переменная, чтобы отслеживать время, в течении которого запрещено востанавливать выносливость
        self.ForbidIncreaseTime=2000 # Сколько по времени будет запрещено восстанавливать выносливостьв милисекундах

        self.IncreaseStamina=1.5 #Увеличение выносливости
        self.DecreaseStaminaUp=5 #Уменьшение выносливости на потолке
        self.DecreaseStaminaUpStand = 3  # Уменьшение выносливости на потолке, когда слизень не двигается
        self.DecreaseStaminaWall=2 # Уменьшение на стене, когда слизень двигается
        self.DecreaseStaminaJump=30 # Уменьшение выносливости при прыжке
        self.DecreaseStaminaWallStand=1.5 # Уменьшение выносливости на стене, когда слизень не двигается
        self.CurrentTime=time.get_ticks()

        self.CheckTimeIncrease=0 #Вспомогательная переменная, чтобы увеличивать выносливость через какой-то промежуток времени
        self.CheckTimeDecrease=0 #Вспомогательная переменная, чтобы уменьшать выносливость через какой-то промежуток времени
        # Для начисления опыта
        self.Level=1 # Уровень слизня
        self.SumExp=0  # Сумма всего опыта слизня
        self.SumShowExp=0 #Вспомогательная переменная, чтобы отображать количество опыта в шкале
        self.SumInreaseExp=0 # Сколько опыта нужно прибавить слизню
        self.CheckTimeIncreaseExp=0 # Вспомогательная переменная, чтобы увеличивать опыт
        self.TimeShowAdd = 0 # Время показа статичной шкалы
        self.t_Exp=-1 # Переменная для отслеживания времени
        self.y_Exp=0 #Начальная координата y шкалы с опытом

        self.ShowScaleExp = False # Показываем шкалу в целом
        self.ShowScaleExpCold = False  # Показываем статичную шкалу
        #Частоты увеличения и уменьшения выносливости в милисекундах(каждые сколько-то милисекунд)
        self.RateIncrease=40
        self.RateDecrease=60

        self.CooldownCling = False  # Вспомогательная переменные, чтобы не давать слизню прилипать к стенам
        # self.CooldownCheckTimeCling=500
        self.CheckTimeCling=0
        #Время в милисекундах сколько слизень не сможет прилипать к стенам, после полного исчерпания выносливости
        self.CooldownClingTime=1000

        # Для итогового окна после уровня
        self.StartLevelTime = time.get_ticks()
        self.LevelTime=0

        #Для создания победного окна
        self.win = False
        #Для смерти
        self.dead = False
        
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
        self.LastRectCentery=self.rect.centery
        # Закгрузка звука прыжка
        self.SoundJump=mixer.Sound('sounds/slime/jump.wav')

        # Загрузка звука поедания грибов
        self.SoundEat=mixer.Sound("sounds/slime/eat.wav")
        
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

    def teleporting(self,goX, goY): #Функция для телепорта
        self.rect.x = goX
        self.rect.y = goY

    def die(self): #Функция для смерти
        self.teleporting(self.startX, self.startY) # перемещаемся в начальные координаты
    
    def win(self):
        self.teleporting(self.startX, self.startY) # перемещаемся в начальные координаты
        

    # Функция обновления слайма при нажатии клавиш
    def update(self,left,right,up,down,jump,platforms,check,dieblocks,teleports,mon,vanish):
        self.CurrentTime=time.get_ticks()
        # Проверка раз в секунду можем ли мы восстанавливать выносливость
        if self.CurrentTime-self.CheckTimeAllowIncrease>1000 and not self.AllowIncrease:
            
            self.ForbidIncreaseTime-=1000
            if self.ForbidIncreaseTime<=0:
                self.ForbidIncreaseTime=0
                self.AllowIncrease=True
            self.CheckTimeAllowIncrease=time.get_ticks()
        


        # Если не прошёл кулдан на прилипание, то мы не можем прилипнуть к стенам
        if self.CurrentTime-self.CheckTimeCling > self.CooldownClingTime and self.CooldownCling:
            self.CooldownCling=False
            self.CheckTimeCling=time.get_ticks()

        if self.onGround:
            if self.CurrentTime-self.CheckTimeIncrease > self.RateIncrease:
                if self.AllowIncrease:
                    self.stamina += self.IncreaseStamina*((self.CurrentTime-self.CheckTimeIncrease)/75+1)
                self.CheckTimeIncrease = time.get_ticks()
            
            if (self.rect.width != widthS) and (self.rect.height != heightS):
                self.image=Surface((widthS,heightS))
                # Обновляем  размер rect
                self.rect=self.image.get_rect()
                self.image.fill(Color(colorS))
                self.image.set_colorkey(Color(colorS))
                # Устанавливаем изменённый rect по правильным координатам
                self.rect.bottom=self.LastRectbottom
                self.rect.centerx=self.LastRectCenterx

        elif not self.onGround and not((self.Up and up) or self.LeftPress or self.RightPress):
            # Выносливость может востанавливаться, если она не кончилась в момент прилипания, если кончилась - то не будет востанавливаться, пока слизень опять не сможет прилипать ко стенам
            if self.CurrentTime-self.CheckTimeIncrease > self.RateIncrease:
                if self.AllowIncrease and not self.CooldownCling:
                    self.stamina += self.IncreaseStamina
                self.CheckTimeIncrease = time.get_ticks()

            if (self.rect.width != self.SizeJumpWidth) and (self.rect.height != self.SizeJumpHeight):
                self.image = Surface((self.SizeJumpWidth, self.SizeJumpHeight))
                # Обновляем  размер rect
                self.rect = self.image.get_rect()
                # Устанавливаем изменённый rect по правильным координатам
                self.rect.centery=self.LastRectCentery
                self.rect.centerx=self.LastRectCenterx

                
        if not self.onGround:
            self.moveY+=gravity


        if left:
            self.moveX=-MoveSpeed
            if self.onGround:
                self.image.fill(colorS)
                self.image.set_colorkey(Color(colorS))
                self.PALeft.blit(self.image,(0,0))
            elif not self.onGround and not((self.Up and up) or self.LeftPress or self.RightPress):
                self.image.fill(colorS)
                self.image.set_colorkey(Color(colorS))
                self.PAJump.blit(self.image, (0, 0))
            if self.Left and self.stamina>0:
                if (self.rect.width!=self.SizeByWallWidth) and (self.rect.height!=self.SizeByWallHeight):
                    self.image=Surface((self.SizeByWallWidth, self.SizeByWallHeight))
                    
                    # Обновляем  размер rect
                    self.rect=self.image.get_rect()
                    # Устанавливаем изменённый rect по правильным координатам
                    self.rect.x=self.LastRectx
                    self.rect.bottom=self.LastRectbottom
                if up:
                    if self.CurrentTime-self.CheckTimeDecrease > self.RateDecrease:
                        self.stamina -= self.DecreaseStaminaWall
                        self.CheckTimeDecrease = time.get_ticks()
                    self.moveY=-MoveSpeed
                    self.image.fill(colorS)
                    self.image.set_colorkey(Color(colorS))
                    self.PALeftUp.blit(self.image,(0,0))
                if down:
                    if self.CurrentTime-self.CheckTimeDecrease > self.RateDecrease:
                        self.stamina -= self.DecreaseStaminaWall
                        self.CheckTimeDecrease = time.get_ticks()
                    self.moveY=+MoveSpeed
                    self.image.fill(colorS)
                    self.image.set_colorkey(Color(colorS))
                    self.PALeftDown.blit(self.image, (0, 0))
                
                if not(up or down):
                    if self.CurrentTime-self.CheckTimeDecrease > self.RateDecrease:
                        self.stamina -= self.DecreaseStaminaWallStand
                        self.CheckTimeDecrease = time.get_ticks()
                    self.moveY=0
                    self.image.fill(colorS)
                    self.image.set_colorkey(Color(colorS))
                    self.PAStayLeft.blit(self.image, (0, 0))
            if self.stamina<=0:
                self.CooldownCling=True

                    

        if right:
            self.moveX=+MoveSpeed
            if self.onGround:
                self.image.fill(colorS)
                self.image.set_colorkey(Color(colorS))
                self.PARight.blit(self.image, (0, 0))
            elif not self.onGround and not((self.Up and up) or self.LeftPress or self.RightPress):
                self.image.fill(colorS)
                self.image.set_colorkey(Color(colorS))
                self.PAJump.blit(self.image, (0, 0))

            if self.Right and self.stamina > 0:
                if (self.rect.width!=self.SizeByWallWidth) and (self.rect.height!=self.SizeByWallHeight):
                    self.image=Surface((self.SizeByWallWidth, self.SizeByWallHeight))
                    # Обновляем  размер rect
                    self.rect=self.image.get_rect()
                    # Устанавливаем изменённый rect по правильным координатам
                    self.rect.bottomright=(self.LastRectRight,self.LastRectbottom)

                if up:
                    if self.CurrentTime-self.CheckTimeDecrease > self.RateDecrease:
                        self.stamina -= self.DecreaseStaminaWall
                        self.CheckTimeDecrease = time.get_ticks()
                    self.moveY=-MoveSpeed
                    self.image.fill(colorS)
                    self.image.set_colorkey(Color(colorS))
                    self.PARightUp.blit(self.image,(0,0))
                if down:
                    if self.CurrentTime-self.CheckTimeDecrease > self.RateDecrease:
                        self.stamina -= self.DecreaseStaminaWall
                        self.CheckTimeDecrease = time.get_ticks()
                    self.moveY=+MoveSpeed
                    self.image.fill(colorS)
                    self.image.set_colorkey(Color(colorS))
                    self.PARightDown.blit(self.image, (0, 0))
                
                if not(up or down):
                    if self.CurrentTime-self.CheckTimeDecrease > self.RateDecrease:
                        self.stamina -= self.DecreaseStaminaWallStand
                        self.CheckTimeDecrease = time.get_ticks()
                    self.moveY=0
                    self.image.fill(colorS)
                    self.image.set_colorkey(Color(colorS))
                    self.PAStayRight.blit(self.image, (0, 0))

            if self.stamina <= 0:
                self.CooldownCling = True
                
        if not(left or right):
            self.moveX=0
            if self.onGround:
                self.image.fill(colorS)
                self.image.set_colorkey(Color(colorS))
                self.PAStay.blit(self.image, (0, 0))
            elif not self.onGround  and not((self.Up and up) or  self.LeftPress or self.RightPress):
                self.image.fill(colorS)
                self.image.set_colorkey(Color(colorS))
                self.PAJump.blit(self.image, (0, 0))

        if jump:
            if self.onGround and self.stamina>self.DecreaseStaminaJump:
                self.stamina-=self.DecreaseStaminaJump
                self.moveY=-jumpPower
                self.SoundJump.play()
        
        if up:
            if self.Up and self.stamina > 0:
                self.moveY=0
                if (self.rect.width != widthS) and (self.rect.height != heightS):
                    self.image = Surface((widthS, heightS))
                    self.rect=self.image.get_rect()
                    self.rect.centerx=self.LastRectCenterx
                    self.rect.y=self.LastRecty
                if not(left  or right):
                    if self.CurrentTime-self.CheckTimeDecrease > self.RateDecrease:
                        self.stamina -= self.DecreaseStaminaUpStand
                        self.CheckTimeDecrease = time.get_ticks()
                    self.moveX=0
                    self.image.fill(colorS)
                    self.image.set_colorkey(Color(colorS))
                    self.PAStayUp.blit(self.image, (0,0))
                if left:
                    if self.CurrentTime-self.CheckTimeDecrease > self.RateDecrease:
                        self.stamina -= self.DecreaseStaminaUp
                        self.CheckTimeDecrease = time.get_ticks()
                    self.moveX=-MoveSpeed
                    self.image.fill(colorS)
                    self.image.set_colorkey(Color(colorS))
                    self.PAUpLeft.blit(self.image,(0,0))
                if right:
                    if self.CurrentTime-self.CheckTimeDecrease > self.RateDecrease:
                        self.stamina -= self.DecreaseStaminaUp
                        self.CheckTimeDecrease = time.get_ticks()
                    self.moveX=MoveSpeed
                    self.image.fill(colorS)
                    self.image.set_colorkey(Color(colorS))
                    self.PAUpRight.blit(self.image, (0,0))

            
            # Если выносливость ноль, то не можем прилипать к потолку
            if self.stamina <= 0:
                self.CooldownCling = True
            # Если время запрета на восстановление выносливости не истекло, то выносливость не восстанавливается
        if self.ForbidIncreaseTime>0:
            self.AllowIncrease=False
        
        
        # Проверка каждые 25 милисекунды получил ли слизень опыт
        if time.get_ticks()-self.CheckTimeIncreaseExp > 25:
            self.CheckTimeIncreaseExp = time.get_ticks()
            # Если опыт больше 2.5 то начинаем анимацию показывания шкалы с опытом
            if self.SumInreaseExp>=2.5 :
                self.ShowScaleExp=True
                # добавляем милисекунды ко времени, сколько шкала будет висеть статично
                if not (self.t_Exp>=self.TimeShowAdd+1 and self.t_Exp<=self.TimeShowAdd+3):
                    self.TimeShowAdd+=0.030
                # Если шкала статична добавляем опыт на шкалу
                if self.ShowScaleExpCold:
                    self.SumExp+=2.5
                    self.SumInreaseExp -= 2.5
                    self.SumShowExp+=2.5
                if self.SumShowExp>=100:
                    self.Level+=int(self.SumShowExp//100)
                    self.SumShowExp -= 100*(self.SumShowExp//100)
                    # print("level=",self.Level)
        # Функция для определения координат шкалы
        if self.ShowScaleExp:
            if self.t_Exp == -1:
                self.t_Exp = 0
            # Шкала статична, когда нет анимации движения выползания или заползания
            if self.t_Exp >= 1 and self.t_Exp < self.TimeShowAdd+1:
                self.ShowScaleExpCold = True
            else:
                self.ShowScaleExpCold = False
            # Если шкала статична, то y постоянна
            if self.ShowScaleExpCold:
                self.y_Exp = 50

            if self.t_Exp < 1 and not self.ShowScaleExpCold:
                self.y_Exp = -70*(self.t_Exp-1)**2+50

            if self.t_Exp >= self.TimeShowAdd+1:
                self.y_Exp = -70*(self.t_Exp-(self.TimeShowAdd+1))**2+50

            if self.t_Exp >= 0:
                self.t_Exp += 1/60
            # Если закончилась анимация заползания шкалы даём знак о прекращении показа шкалы
            if self.t_Exp > self.TimeShowAdd+3:
                self.t_Exp = -1
                self.ShowScaleExp = False
                self.TimeShowAdd=0

        
        # Выносливость изменяется в значениях от 0 до 100
        
        if self.stamina>100:
            self.stamina=100
        if self.stamina<0:
            self.stamina=0
        #Проверка пересекается ли rect со стенами
        self.RectCheck(self.rect, platforms)

        # Чтобы всегда работала гравитация и  столкновения со стенами
        self.onGround=False
        # Чтобы  всегда  работали взаимодействия  со стенами
        self.Right=False
        self.Left=False
        self.Up=False
        self.RightPress=False
        self.LeftPress=False
        self.UpPress=False
        #Аналогично проделываем  результат с rect, добавляем взаимодействие rect с поверхностью
        self.rect.x+=self.moveX
        self.collide(self.moveX,0,platforms,dieblocks,teleports,mon,vanish) #Проверка пересечения по горизонтали
        self.rect.y+=self.moveY 
        self.collide(0,self.moveY,platforms,dieblocks,teleports,mon,vanish) #Проверка пересечения по вертикали
        # Для того, чтобы можно было увидеть rect
        if  check:
            self.image.fill(('#FFFFFF'))
        # Если есть кулдаун на прилипание, убираем все касания
        if self.CooldownCling:
            self.RightPress=False
            self.Right=False
            self.LeftPress=False
            self.Left=False
            self.Up=False

        # Обновлением точек, по которым устанавливается rect
        self.LastRectbottom = self.rect.bottom
        self.LastRectx = self.rect.x #Для левой стены
        self.LastRecty=self.rect.y
        self.LastRectRight=self.rect.right # Для  правой стены
        self.LastRectTop=self.rect.top
        self.LastRectCenterx=self.rect.centerx
        self.LastRectCentery=self.rect.centery
        # print(self.LevelTime,' ',self.StartLevelTime)
        # print(self.stamina)
        # print(self.CooldownCling)

    # Функция обработки столкновений с препятствиями
    def collide(self, moveX, moveY, platforms, dieblocks, teleports, mon, vanish):
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
                    # self.UpPress=True
                    self.moveY=0
                
            if (self.rect.right==each.rect.left) and (self.rect.centery<each.rect.bottom and self.rect.centery>each.rect.top):
                self.Right=True
                
            if (self.rect.left == each.rect.right) and (self.rect.centery < each.rect.bottom and self.rect.centery > each.rect.top):
                self.Left=True

            if (self.rect.top == each.rect.bottom) and (self.rect.centerx+1>=each.rect.left and self.rect.centerx-1<=each.rect.right):
                self.Up=True
        

        for each in dieblocks:
            if sprite.collide_rect(self,each): # если пересекаемый блок - blocks.BlockDie
                self.dead = True
                Slime.die(self)# умираем
        for each in teleports:
            if sprite.collide_rect(self,each): # если пересекаемый блок - телепорт
                self.win = True
                Slime.win(self)
                self.LevelTime=time.get_ticks()-self.StartLevelTime
                self.StartLevelTime=time.get_ticks()
        for each in mon:
            if sprite.collide_rect(self,each): # если пересекаемый монстра
                self.dead=True
                Slime.die(self)# умираем
        # Если столкнулись с исчезающим объектом, объект пропадает из исчезающих
        for each in vanish:
            if sprite.collide_rect(self,each):
                self.SumInreaseExp +=10
                self.SoundEat.play()
                vanish.remove(each)

    def RectCheck(self,LastRect,platforms):
        #Если есть пересечение с платформами,  то передвигаем слайма в нужную сторону
        for each in platforms:
            if each.rect.collidepoint(LastRect.right-1,LastRect.centery):
                while each.rect.collidepoint(LastRect.right, LastRect.centery):
                    LastRect.x-=1

            if each.rect.collidepoint(LastRect.centerx, LastRect.top):
                while each.rect.collidepoint(LastRect.centerx, LastRect.top):
                    LastRect.y += 1

            if each.rect.collidepoint(LastRect.x, LastRect.top+1):
                while each.rect.collidepoint(LastRect.x, LastRect.top+1):
                    LastRect.x += 1

            if each.rect.collidepoint(LastRect.left, LastRect.bottom-1):
                while each.rect.collidepoint(LastRect.left, LastRect.bottom-1):
                    LastRect.x += 1

            if each.rect.collidepoint(LastRect.right-1, LastRect.top):
                while each.rect.collidepoint(LastRect.right-1, LastRect.top):
                    LastRect.y+=1

            if each.rect.collidepoint(LastRect.x, LastRect.top):
                while each.rect.collidepoint(LastRect.x, LastRect.top):
                    LastRect.y+=1
            

            if LastRect.collidepoint(each.rect.x,each.rect.top):
                while LastRect.collidepoint(each.rect.x,each.rect.top):
                    LastRect.x -= 1

            if LastRect.collidepoint(each.rect.x, each.rect.bottom-1):
                while LastRect.collidepoint(each.rect.x, each.rect.bottom-1):
                    LastRect.x -= 1
