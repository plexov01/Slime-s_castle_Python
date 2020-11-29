import pygame
#Задаю ширину и высоту окна
widthW=360 
heightW=480
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

    #flip нужен для однократного показа всего, что нарисовано на экране за 1 кадр
    pygame.display.update()
#При завершении цикла игры окно игры закрывается
pygame.quit()

#34589735