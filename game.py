import pygame
from pygame import * #Строчка,  чтобы каждый  раз не писать pygame
import slime #импорт кода, относящегося к слайму из другого файла
import blocks #импорт кода, относящегося к описанию стен
#Задаю ширину и высоту окна
widthW=850
heightW=600
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

# Создаю слайма
slime=slime.Slime(700,100)
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
    "-----------------",
    "-               -",
    "-               -",
    "-               -",
    "---------       -",
    "-               -",
    "-               -",
    "-   -------------",
    "-     -         -",
    "-     -         -",
    "-               -",
    "-----------------"]

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

#Цикл игры
running=True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS) 
    #Цикл для обнаружения нажатых клавиш игроком
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




    

    #Отрисовка слайма
    slime.update(left,right,jump,platforms) #Для передвижения
    entities.draw(screen) # Отрисовка всех спрайтов на нашем экране

    #flip нужен для однократного показа всего, что нарисовано на экране за 1 кадр
    pygame.display.update()
#При завершении цикла игры окно игры закрывается
pygame.quit()
