# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3 <http://creativecommons.org/licenses/by/3.0/>
import pygame
import sys
import enemies  # Импорт кода для монстра
# import fire #Импорт кода для огня
from pygame import * #Строчка,  чтобы каждый  раз не писать pygame
import slime #импорт кода, относящегося к слайму из другого файла
import blocks #импорт кода, относящегося к описанию стен
import objects
from light import Light #Импорт класса, необхдимого для создания освещения
from menu import Menu,punkts
from HUD import DrawScaleStamina
# import menu
# import options


# импорт mixer для  звука
# from pygame import mixer
# Настройка звука
mixer.pre_init(44100,-16,2,512)
mixer.init()
#загрузка воспроизведения на  фоне
music = mixer.Sound("music/background_music.ogg")
music.play(-1)
#Громкость
volume=0#0.3
music.set_volume(volume)
#инициализация стилей
pygame.font.init()
# #Звук для воспроизведения на фоне(найдём позже)

#Задаю ширину и высоту окна
widthW=1920#1000
heightW=1080 #1080
#Частота кадров в секунду
FPS=60
#Создаю игру и окно
pygame.init()
screen = pygame.display.set_mode((widthW, heightW), FULLSCREEN|SCALED|DOUBLEBUF)  # Окно игры , FULLSCREEN|SCALED|DOUBLEBUF

# pygame.FULLSCREEN – полноэкранный режим
# pygame.DOUBLEBUF – двойная буферизация(рекомендуется при совместном использовании HWSURFACE или OPENGL)
# pygame.HWSURFACE – аппаратное ускорение отрисовки(только для режима FULLSCREEN)
# pygame.OPENGL – обработка отображений  с помощью библиотеки OpenGL
# pygame.RESIZABLE – окно с изменяемыми размерами
# pygame.NOFRAME – окно без рамки и заголовка
# pygame.SCALED – разрешение, зависящее от размеров рабочего стола.
#Название окна
pygame.display.set_caption("Slime's castle")
#Задаю иконку игры(вверху слева)
pygame.display.set_icon(pygame.image.load("image/icon/icon_slime.ico"))
#Clock нужен для того, чтобы убедиться, что игра работает с заданной частотой кадров
clock=pygame.time.Clock()
StartTime=time.get_ticks()
#Текст победы/проигрыша
fontObj = pygame.font.Font('freesansbold.ttf', 50)
textSurfaceObj = fontObj.render('Win!', True, (20,30,40))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (widthW//2, heightW//2)
deadSurFaceObj = fontObj.render('Dead!', True, (20,30,40)) 

            
# Создание меню
Menu = Menu(volume,music,punkts)
# # Включение меню при старте игры
# Menu.MenuProcessing()

# Создаю слайма и  задаю его начальное положение
slime = slime.Slime(160, 1360)
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
bg_blocks = [] #Блоки заднего фона
#Группа и массив монстров
mon=[]
fires=pygame.sprite.Group() #Огоньки
# Добавим в slime в группу спрайтов 
animatedEntities = pygame.sprite.Group() # все анимированные объекты, за исключением героя 
# entities.add(expl)
monsters = pygame.sprite.Group() # Все передвигающиеся объекты
# entities.add(expl)
# entities.add(portal)
#Создание пробного уровня(для отладки слайма)
level1=[
    "----------------------------------------------------------",
    "-                                                        -",
    "-                                                        -",
    "-                                                        -",
    "-   -             *          **       ***              $ -",
    "--- - ----------------------------------------------------",
    "-   -    -                                               -",
    "-   -                                                    -",
    "-   -+                                                   -",
    "-   -   -                                      -         -",
    "-   -                 *                                  -",
    "-           -        --         -                   -    -",
    "-                        --    *     --             -    -",
    "-     -                        -           -           - -",
    "-            --                    -    -           -    -",
    "-++++++++++++++++++++++++++-                        -    -",
    "----------------------------                       -+    -",
    "-                                                   -    -",
    "-                                                   -    -",
    "-                                                        -",
    "-                                                       --",
    "-                                                        -",
    "-                                        -           -   -",
    "-                                        -               -",
    "-                                        -               -",
    "-                                        -               -",
    "-                    -      -     *      -        -      -",
    "-          -         -++++++-     -      -+++++++++++++++-",
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
            pf = objects.Fire(x,y)
            # Добавляем его к группе спрайтов
            bg = blocks.Background(x,y)
            entities.add(pf)
            fires.add(pf)
            bg_blocks.append(bg)
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
            bg = blocks.Background(x,y)
            bg_blocks.append(bg)
        else:
            bg = blocks.Background(x,y)
            bg_blocks.append(bg)
        x += 50
    y += 50
    x = 0
#Добавим монстра
mn = enemies.Monster(760, 1324, 1.3, 0.2, 150, 6)  # Создаем монстра
entities.add(mn)
monsters.add(mn)
mon.append(mn)

TrueScroll=[0,0]
# # Класс для динамической камеры
# class  Camera:
#     def  __init__(self,cameraF,width,height):
#         self.cameraF=cameraF
#         self.levelRect=Rect(0,0,width,height)

#     def apply(self, target):
#         # print(target.rect.move(self.levelRect.topleft))
#         return target.rect.move(self.levelRect.topleft)

#     def update(self, target):
#         self.levelRect=self.cameraF(self.levelRect, target.rect)
            
        

# #Функция для камеры, которая будет отслеживать положение игрока
# def cameraF(camera, TargetRect):
#     #Определение координат  динамической камеры
#     l=-TargetRect.x+widthW/2
#     t=-TargetRect.y+heightW/2
    
#     # # Для того, чтобы игрок не видел, что происходит за стенами уровня
#     # l=min(0,l)
#     # l=max(-(camera.width-widthW),l)

#     # t=max(-(camera.height-heightW),t)
#     # t=min(0,t)
#     # print(camera.width, ' ', camera.height)
#     return Rect(l, t, camera.width, camera.height)


# #Длина и ширина всего  уровня
# TotalWidth = len(level1[0])*50
# TotalHeight = len(level1)*50
# # Создаю  объект класса камера, для слежения за игроком
# # camera=Camera(cameraF,TotalWidth,TotalHeight)

# LightMap=Light(1920,1080)
# LightSlime = pygame.Surface((widthW,heightW))
# LightSlime.fill((255,255,255,100))

# LightSlime.blit(LightMap.MakeLight(),(0,0),special_flags=BLEND_RGBA_SUB)
# LightSlime.set_colorkey((55,55,55,100))

# lightType1 = image.load('effects/light/lightType12.png').convert_alpha()
# lightType1R1000 = transform.scale(lightType1, (2000, 2000))
# filter = Surface((widthW, heightW))
# filter.fill(color.Color('#000000'))
# wigthLight = lightType1R1000.get_width()
# heightLight = lightType1R1000.get_height()


# filter.blit(lightType1R1000, (widthW//2 - wigthLight//2, heightW//2-heightLight//2))
# LightSlime.blit(LightSlime, (-1000, -1000), special_flags=BLEND_RGBA_SUB)
# LightSlime.blit(LightMap.MakeLight(), (0, 0), special_flags=BLEND_RGBA_SUB)
CheckTime = 0
showtext = 0
#Цикл игры
running=True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)

    # second=time.get_ticks()/1000
    # # second2=time.get_ticks()//1000+1
    # secendMES=0
    # if time.get_ticks()/1000>secondMes:



    # if second+1>time.get_ticks()//1000:
    #     second2=second//1000
    #     print(second,' ',second2)
    # # print(Second)

    

    # Очищаю экран от предыдущего освещённого кадра
    # LightMap.Clear()
    #Цикл для обработки нажатых клавиш игроком
    for event in pygame.event.get():
        #if для вызова меню в игре
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            Menu.MenuProcessing()

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
    


    
    slime.update(left,right,up,down,jump,platforms,CHECK,dieblocks,teleports,mon) #Для передвижения  и взаимодействия с игрой
    # Для параллакса
    TrueScroll[0] += int((slime.rect.centerx - widthW/2 - TrueScroll[0]))
    TrueScroll[1] += int((slime.rect.centery - heightW/2- TrueScroll[1]))
    scroll=TrueScroll.copy()
    # scroll
    # print(time.get_ticks(), ' ', slime.CurrentTime)
    monsters.update() #Рисуем монстра
    fires.update() #Рисуем огниd

    #Добавляю слайма в цель отслеживания камеры  
    # camera.update(slime)
    

    # # Левые верхние координаты экрана
    WindowRectx = slime.rect.x-widthW/2
    WindowRecty = slime.rect.y-heightW/2
    # # Rect экрана(видимой игроку области)
    # WindowRect = Rect(WindowRectx, WindowRecty, widthW,heightW)

    # Прорисовка текстур
    for e in bg_blocks:
        # Три разные настройки для прорисовки(окружность вокруг слизня, настраеваемый прямоугольник, прямоугольник всего экрана(прорисовывается всё, что есть на экране), прорисовывается весь уровень сразу)
        # if ((e.rect.x-slime.rect.centerx)**2+(e.rect.y-slime.rect.centery)**2 < (250**2)):
        #     screen.blit(e.image, (e.rect.x-TrueScroll[0],e.rect.y-TrueScroll[1]))

        if (e.rect.right > WindowRectx and (e.rect.left-15< (WindowRectx+widthW))) and (e.rect.top-10 <= (WindowRecty+heightW) and e.rect.bottom >= WindowRecty):
            screen.blit(e.image, (e.rect.x-TrueScroll[0],e.rect.y-TrueScroll[1]))

        # if (e.rect.right-500>WindowRectx and (e.rect.left+500<(WindowRectx+widthW))) and(e.rect.top+250<(WindowRecty+heightW) and e.rect.bottom-250>WindowRecty):
        #     screen.blit(e.image, camera.apply(e))

        # if WindowRect.colliderect(e):
        #     screen.blit(e.image, camera.apply(e))

        # screen.blit(e.image, camera.apply(e))

    #Отрисовываю все спрайты в области камеры
    for e in entities:
        # if ((e.rect.x-slime.rect.centerx)**2+(e.rect.y-slime.rect.centery)**2 < (450**2)):
        #     screen.blit(e.image, (e.rect.x-TrueScroll[0], e.rect.y-TrueScroll[1]))
        
        if (e.rect.right > WindowRectx and (e.rect.left-15< (WindowRectx+widthW))) and (e.rect.top-10 <= (WindowRecty+heightW) and e.rect.bottom >= WindowRecty):
            screen.blit(e.image, (e.rect.x-TrueScroll[0],e.rect.y-TrueScroll[1]))

        # if (e.rect.right-500>WindowRectx and (e.rect.left+500<(WindowRectx+widthW))) and(e.rect.top+250<(WindowRecty+heightW) and e.rect.bottom-250>WindowRecty):
        #     screen.blit(e.image, camera.apply(e))

        # if WindowRect.colliderect(e):
        #     screen.blit(e.image, camera.apply(e))

        # screen.blit(e.image, camera.apply(e))
    
        

    
    DrawScaleStamina(screen,widthW*0.6,heightW*0.9,slime.stamina)

    
    # Условия выигрыша и победы
    if slime.dead:

        done = True
        showtext = 2000

        while done:
            screen.fill((123, 132, 55))
            screen.blit(deadSurFaceObj, textRectObj)
            pygame.display.update()
            if time.get_ticks()-CheckTime > 1000:
                showtext -= 1000
                CheckTime = time.get_ticks()

            if showtext <= 0:
                showtext = 0
                done = False
        slime.dead = False
    
    if slime.win:

        done = True
        showtext = 2000

        while done:
            screen.fill((123, 132, 55))
            screen.blit(textSurfaceObj, textRectObj)
            pygame.display.update()
            if time.get_ticks()-CheckTime > 1000:
                showtext -= 500
                CheckTime = time.get_ticks()

            if showtext <= 0:
                showtext = 0
                done = False
        slime.win = False

    #display.update нужен для однократного показа всего, что нарисовано на экране за 1 кадр
    pygame.display.update()
    
#При завершении цикла игры окно игры закрывается
pygame.quit()
sys.exit()
