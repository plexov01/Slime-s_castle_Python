# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3 <http://creativecommons.org/licenses/by/3.0/>
import pygame
import sys
import enemies  # Импорт кода для монстра
# import fire #Импорт кода для огня
from pygame import * #Строчка,  чтобы каждый  раз не писать pygame
import slime #импорт кода, относящегося к слайму из другого файла
import blocks #импорт кода, относящегося к описанию стен
import objects
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
# SoundJump=mixer.Sound('sounds/slime/jump.wav')
# SoundJump.play(-1)
from menu import Menu,punkts

#Задаю ширину и высоту окна
widthW=1920#1000
heightW=1080 #1080
#Частота кадров в секунду
FPS=60   
#Создаю игру и окно
pygame.init()
screen = pygame.display.set_mode((widthW, heightW), SCALED|FULLSCREEN)  # Окно игры

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

fontObj = pygame.font.Font('freesansbold.ttf', 50)
textSurfaceObj = fontObj.render('Win!', True, (20,30,40))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (widthW//2, heightW//2)
deadSurFaceObj = fontObj.render('Dead!', True, (20,30,40)) 

            

Menu = Menu(volume,music,punkts)
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

    
    slime.update(left,right,up,down,jump,platforms,CHECK,dieblocks,teleports,mon) #Для передвижения  и взаимодействия с игрой

    monsters.update() #Рисуем монстра
    fires.update() #Рисуем огни

    #Добавляю слайма в цель отслеживания камеры
    camera.update(slime)

    for e in bg_blocks:
        screen.blit(e.image, camera.apply(e))

    #Отрисовываю все спрайты в области камеры
    for e in entities:
        screen.blit(e.image, camera.apply(e))
    
    # if slime.win:
    #     screen.fill((123,132,55))
    #     screen.blit(textSurfaceObj, textRectObj)

    # if slime.dead:
    #     screen.fill((123,132,55))
    #     screen.blit(deadSurFaceObj, textRectObj)
        
    #display.update нужен для однократного показа всего, что нарисовано на экране за 1 кадр
    pygame.display.update()
#При завершении цикла игры окно игры закрывается
pygame.quit()
sys.exit()
