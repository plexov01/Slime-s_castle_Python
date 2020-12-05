import pygame
from pygame import * #Строчка,  чтобы каждый  раз не писать pygame
import slime #импорт кода, относящегося к слайму из другого файла
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
slime=slime.Slime(750,500)
left=right=False

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
        if event.type==KEYDOWN and event.key==K_LEFT:
            left=True
        if event.type==KEYDOWN and event.key==K_RIGHT:
            right=True

        if event.type==KEYUP and event.key==K_LEFT:
            left=False
        if event.type==KEYUP and event.key==K_RIGHT:
            right=False

    #Заливка заднего фона чёрным цветом
    screen.fill(("#000000"))

    #Координаты для отрисовки пробного уровня
    x=y=0
    for line in level:
        for col in line:
            if col=="-":
                #Если элемент блок, то создаём, заливаем его цветом и рисуем его
                pf=Surface((50,50))
                pf.fill(Color("#123456"))
                screen.blit(pf,(x,y))
            x+=50
        y+=50
        x=0




    

    #Отрисовка слайма
    slime.update(left,right) #Для передвижения
    slime.draw(screen) # Отрисовка слайма на нашем экране

    #flip нужен для однократного показа всего, что нарисовано на экране за 1 кадр
    pygame.display.update()
#При завершении цикла игры окно игры закрывается
pygame.quit()
