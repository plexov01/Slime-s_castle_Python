import pygame
from pygame import * #Строчка,  чтобы каждый  раз не писать pygame
import slime #импорт кода, относящегося к слайму из другого файла
import blocks #импорт кода, относящегося к описанию стен
#Задаю ширину и высоту окна
widthW=1920
heightW=1080
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

# Создаю слайма и  задаю его начальное положение
slime = slime.Slime(1750, 1350)
left=right=False
jump=False
#Группируем все спрайты
entities=pygame.sprite.Group()
# Массив со всеми платформами, со всем во что будем врезаться
platforms=[]
# Добавим в slime в группу спрайтов
entities.add(slime)

#Создание пробного уровня(для отладки слайма)
level=[
    "-------------------------------------",
    "-                                   -",
    "-                                   -",
    "-                                   -",
    "---------                           -",
    "-                                   -",
    "-                                   -",
    "-       -----------------------------",
    "-                               --- -",
    "-                                   -",
    "-    ------                         -",
    "-                                   -",
    "-                                   -",
    "-                          ----  ----",
    "-                                   -",
    "-        --------                   -",
    "-                                   -",
    "-                 -------------- ----",
    "-                                   -",
    "-                                   -",
    "------------------------            -",
    "-                                   -",
    "-                          ----------",
    "-                                   -",
    "-   ---------------------------------",
    "-     -                             -",
    "-     -                             -",
    "-                                   -",
    "-------------------------------------"]


# #Координаты для отрисовки пробного уровня
x = y = 0
# Цикл, который добавляет в массив platforms все "твёрдые блоки", а также в отрисовку
for line in level:
    for col in line:
        if col == "-":
            # Создаём экземпляр класса
            pf = blocks.Platform(x, y)
            # Добавляем его к группе спрайтов
            entities.add(pf)
            # Добавляем в массив объектов, с которыми можно сталкиваться
            platforms.append(pf)
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
TotalWidth = len(level[0])*50
TotalHeight = len(level)*50
# Создаю  объект класса камера, для слежения за игроком
camera=Camera(cameraF,TotalWidth,TotalHeight)


#Цикл игры
running=True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)

    #Цикл для обработки нажатых клавиш игроком
    for event in pygame.event.get():
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
                
        if event.type==KEYUP and event.key==K_a:
            left=False
        if event.type==KEYUP and event.key==K_d:
            right=False
        if event.type==KEYUP and event.key==K_SPACE:
            jump=False

    #Заливка заднего фона чёрным цветом
    screen.fill(("#000000"))

    
    slime.update(left,right,jump,platforms) #Для передвижения

    #Добавляю слайма в цель отслеживания камеры
    camera.update(slime)

    #Отрисовываю все спрайты в области камеры
    for e in entities:
        screen.blit(e.image, camera.apply(e))

    #display.update нужен для однократного показа всего, что нарисовано на экране за 1 кадр
    pygame.display.update()
#При завершении цикла игры окно игры закрывается
pygame.quit()
