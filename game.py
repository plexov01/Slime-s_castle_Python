# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3 <http://creativecommons.org/licenses/by/3.0/>
import pygame
import sys
from pygame import * #Строчка,  чтобы каждый  раз не писать pygame
import slime #импорт кода, относящегося к слайму из другого файла
import blocks #импорт кода, относящегося к описанию стен
# import objects
# импорт mixer для  звука
# from pygame import mixer
# Настройка звука
mixer.pre_init(44100,-16,2,512)
mixer.init()
#загрузка воспроизведения на  фоне
music = mixer.Sound("music/background_music.ogg")
music.play(-1)
#Громкость
volume=0.3
music.set_volume(volume)
#инициализация стилей
pygame.font.init()
# #Звук для воспроизведения на фоне(найдём позже)
# SoundJump=mixer.Sound('sounds/slime/jump.wav')
# SoundJump.play(-1)

#Задаю ширину и высоту окна
widthW=1920
heightW=1080 #1080
#Частота кадров в секунду
FPS=60   
#Создаю игру и окно
pygame.init()
screen=pygame.display.set_mode((widthW,heightW)) #Окно игры
#Название окна
pygame.display.set_caption("Slime's castle")
#Задаю иконку игры(вверху слева)
pygame.display.set_icon(pygame.image.load("image\icon\icon_slime.jpg"))
#Clock нужен для того, чтобы убедиться, что игра работает с заданной частотой кадров
clock=pygame.time.Clock()

fontObj = pygame.font.Font('freesansbold.ttf', 50)
textSurfaceObj = fontObj.render('Win!', True, (20,30,40))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (widthW//2, heightW//2)
deadSurFaceObj = fontObj.render('Dead!', True, (20,30,40)) 

#меню
class Menu:
    def __init__(self, volume, punkts=[120, 140, u'Punkt', (250, 250, 30), (250, 30, 250), 0]):
        self.punkts = punkts
        self.volume=volume

    def render(self, pover, font, num):
        for i in self.punkts:
            if num == i[5]:
                pover.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                pover.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        done = True
        font_menu = pygame.font.SysFont('ubuntu', 88)
        punkt = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0]+155 and mp[1] > i[1] and mp[1] < i[1]+90:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for c in pygame.event.get():
                if c.type == pygame.QUIT:
                    done = False
                    pygame.quit()
                    sys.exit()
                if c.type == pygame.KEYDOWN:
                    if c.key == pygame.K_ESCAPE:
                        done = False
                        pygame.quit()
                        sys.exit()
                    if c.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if c.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt += 1
                if c.type == pygame.MOUSEBUTTONDOWN and c.button == 1:
                    if punkt == 1:
                        done == False
                        game = Options(volume,punkts1)
                        game.options()
                    if punkt == 0:
                        done = False
                    elif punkt == 2:
                        done = False
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
            
#настройки
class Options:
    def __init__(self,volume, punkts1=[120, 140, u'Punkt1', (250, 250, 30), (250, 30, 250), 0]):
        self.punkts1 = punkts1
        self.volume=volume

    def render(self, pover, font, num):
        for i in self.punkts1:
            if num == i[5]:
                pover.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                pover.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def options(self):
        done = True
        font_options = pygame.font.SysFont('ubuntu', 88)
        punkt1 = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.punkts1:
                if mp[0] > i[0] and mp[0] < i[0]+155 and mp[1] > i[1] and mp[1] < i[1]+90:
                    punkt1 = i[5]
            self.render(screen, font_options, punkt1)
            for c in pygame.event.get():
                if c.type == pygame.QUIT:
                    done = False
                    pygame.quit()
                    sys.exit()
                if c.type == pygame.KEYDOWN:
                    if c.key == pygame.K_ESCAPE:
                        done = False
                        pygame.quit()
                        sys.exit()
                    if c.key == pygame.K_UP:
                        if punkt1 > 0:
                            punkt -= 1
                    if c.key == pygame.K_DOWN:
                        if punkt1 < len(self.punkts)-1:
                            punkt1 += 1
                if c.type == pygame.MOUSEBUTTONDOWN:
                    if punkt1 == 1:
                        if self.volume>1:
                            self.volume=1
                        else:
                            self.volume+=0.1         
                                       
                        music.set_volume(self.volume)

                    if punkt1 == 0:
                        done = False
                        game.menu()
                    elif punkt1 == 2:

                        if self.volume < 0:
                            self.volume = 0
                        else:
                            self.volume -= 0.1

                        music.set_volume(self.volume)


            pygame.display.flip()


#создаем настройки
punkts1 = [(200, 890, u'Back', (250, 250, 30), (250, 30, 250), 0),
           (810, 490, u'+', (250, 250, 30), (250, 30, 250), 1),
           (900, 490, u'-', (250, 250, 30), (250, 30, 250), 2)]
#создаем меню
punkts = [(810, 390, u'Game', (250, 250, 30), (250, 30, 250), 0),
          (810, 490, u'Options', (250, 250, 30), (250, 30, 250), 1),
          (810, 590, u'Quit', (250, 250, 30), (250, 30, 250), 2)]
game = Menu(volume,punkts)
game.menu()

# Создаю слайма и  задаю его начальное положение
slime = slime.Slime(1750, 1400)
left=right=False
jump=False
up=down=False
#Для включения/выключения режима разработчика во время игры
CHECK=False
#Группируем все спрайты
entities=pygame.sprite.Group()
# Массив со всеми платформами, со всем во что будем врезаться
platforms=[]
# Массив с die блоками, от которых будем умирать
dieblocks=[]
#телепорты
teleports=[]
# Добавим в slime в группу спрайтов  
entities.add(slime)
# entities.add(expl)
# entities.add(portal)
#Создание пробного уровня(для отладки слайма)
level1=[
    "----------------------------------------",
    "-                                      -",
    "-$                                      -",
    "--++---++-                             -",
    "----------                             -",
    "-                                      -",
    "-                                      -",
    "-       --------------------------------",
    "-                                  --- -",
    "-                                      -",
    "-    ------                            -",
    "-                               -      -",
    "--             ---              -      -",
    "-                             ----  ---- -",
    "-                                      - -",
    "-   -    --------                      - -",
    "-                                      - -",
    "-                 ----------------- ---- -",
    "-                                      - -",
    "-                                      - -",
    "---------------------------          - - -        -       ",
    "-                                      - -           $    ",
    "-                          ---------- -- -           -    ",
    "-      $                               - -                ",
    "-   ---------------------------- ------- -       -        ",
    "-     -                       -          -                ",
    "-     -                       -          -           -    ",
    "-                             -          -       -        ",
    "----------------------------------------------------------"]


# #Координаты для отрисовки пробного уровня
x = y = 0
# Цикл, который добавляет в массив platforms все "твёрдые блоки", а также в отрисовку
for line in level1:
    for col in line:
        if col == "-":
            # Создаём экземпляр класса
            pf = blocks.Platform(x, y)
            # Добавляем его к группе спрайтов
            entities.add(pf)
            # Добавляем в массив объектов, с которыми можно сталкиваться
            platforms.append(pf)
        elif col == "*":
            # Создаём экземпляр класса
            pf = blocks.DieBlockLamp(x,y)
            # Добавляем его к группе спрайтов
            entities.add(pf)
            # Добавляем в массив объектов, от которых умираем
            dieblocks.append(pf)
        elif col == "+":
            # Создаём экземпляр класса
            pf = blocks.DieBlockLava(x,y)
            # Добавляем его к группе спрайтов
            entities.add(pf)
            # Добавляем в массив объектов, от которых умираем
            dieblocks.append(pf)
        elif col == "$":
            # Создаём экземпляр класса
            pf = blocks.Teleport(x,y)
            # Добавляем его к группе спрайтов
            entities.add(pf)
            # Добавляем в массив объектов, от которых умираем
            teleports.append(pf)
        x += 50
    y += 50
    x = 0

#Класс для динамической камеры
class  Camera:
    def  __init__(self,cameraF,width,height):
        self.cameraF=cameraF
        self.levelRect=Rect(0,0,width,height)

    def apply(self, target):
        return target.rect.move(self.levelRect.topleft)

    def update(self, target):
        self.levelRect=self.cameraF(self.levelRect, target.rect)
            
        

#Функция для камеры, которая будет отслеживать положение игрока
def cameraF(camera, TargetRect):
    #Определение координат  динамической камеры
    l=-TargetRect.x+widthW/2
    t=-TargetRect.y+heightW/2
    
    # # Для того, чтобы игрок не видел, что происходит за стенами уровня
    # l=min(0,l)
    # l=max(-(camera.width-widthW),l)

    # t=max(-(camera.height-heightW),t)
    # t=min(0,t)

    return Rect(l, t, camera.width, camera.height)


#Длина и ширина всего  уровня
TotalWidth = len(level1[0])*50
TotalHeight = len(level1)*50
# Создаю  объект класса камера, для слежения за игроком
camera=Camera(cameraF,TotalWidth,TotalHeight)


#Цикл игры
running=True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)
    # music.set_volume(Menu.volume)
    #Цикл для обработки нажатых клавиш игроком
    for event in pygame.event.get():
        #if для вызова меню в игре
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            game.menu()

        #if для закрытия игры при нажатии на крестик
        if event.type==pygame.QUIT:
            running=False
        #if для обработки  нажатий, для передвижения слайма
        if event.type==KEYDOWN and event.key==K_a:
            left=True
        if event.type==KEYDOWN and event.key==K_d:
            right=True
        if event.type==KEYDOWN and event.key==K_SPACE:
            jump=True
        if event.type==KEYDOWN and event.key==K_w:
            up=True
        if event.type==KEYDOWN and event.key==K_s:
            down=True
                
        if event.type==KEYUP and event.key==K_a:
            left=False
        if event.type==KEYUP and event.key==K_d:
            right=False
        if event.type==KEYUP and event.key==K_SPACE:
            jump=False
        if event.type==KEYUP and event.key==K_w:
            up=False
        if event.type==KEYUP and event.key==K_s:
            down=False


        
        #Для включения/выключения режима разработчика во время игры
        if event.type==KEYDOWN and event.key==K_F1:
            CHECK=True
        if event.type==KEYDOWN and event.key==K_F2:
            CHECK=False

    #Заливка заднего фона чёрным цветом
    screen.fill(("#000000"))

    
    slime.update(left,right,up,down,jump,platforms,CHECK,dieblocks,teleports) #Для передвижения  и взаимодействия с игрой

    #Добавляю слайма в цель отслеживания камеры
    camera.update(slime)

    #Отрисовываю все спрайты в области камеры
    for e in entities:
        screen.blit(e.image, camera.apply(e))
    
    if slime.win:
        screen.fill((123,132,55))
        screen.blit(textSurfaceObj, textRectObj)

    if slime.dead:
        screen.fill((123,132,55))
        screen.blit(deadSurFaceObj, textRectObj)

    #display.update нужен для однократного показа всего, что нарисовано на экране за 1 кадр
    pygame.display.update()
#При завершении цикла игры окно игры закрывается
pygame.quit()
sys.exit()
