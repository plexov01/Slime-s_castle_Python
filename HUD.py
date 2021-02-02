from pygame import *

def DrawScaleStamina(Surface,x,y,stamina):
    if stamina<0:
        stamina=0
    WidthBack=700
    HeightBack=50

    WidthScale=WidthBack-20
    HeightScale=HeightBack*0.9

    WidthFullness=(WidthScale-10)*(stamina/100)
    HeightFullness=HeightScale*0.9
    RectBack=Rect(x,y,WidthBack,HeightBack)

    RectStamina=Rect(x+(WidthBack-WidthScale)//2,y+(HeightBack-HeightScale)//2,WidthScale,HeightScale)

    RectFullness=Rect(x+(WidthBack-WidthScale)//2+5,y+(HeightBack-HeightScale)//2+(HeightScale-HeightFullness)//2,WidthFullness,HeightFullness)

    draw.rect(Surface,"#707070",RectBack)
    draw.rect(Surface,"#000000",RectStamina)
    draw.rect(Surface,"#ff8d18", RectFullness)

    lightning = image.load("image/HUD/lightning.png").convert_alpha()
    lightning=transform.scale(lightning,(150,150))
    RectLightning=lightning.get_rect(center=(RectBack.left+10,RectBack.centery))

    
    Surface.blit(lightning,RectLightning)
    # Surface.blit(image.load("image/HUD/lightning.png"),image.load("image/HUD/lightning.png").get_rect(centery=RectBack.centery,right=RectLightning.left))

def DrawScaleExperience(Surface,x,y,experience):

    WidthBack = display.Info().current_w*0.4
    HeightBack = 50

    WidthScale = WidthBack*0.99
    HeightScale = HeightBack*0.9

    WidthFullness = (WidthScale*0.99)*(experience/100)
    HeightFullness = HeightScale*0.9


    RectBack = Rect(x, y, WidthBack, HeightBack)

    RectExperience = Rect(x+(WidthBack-WidthScale)//2, y + (HeightBack-HeightScale)//2, WidthScale, HeightScale)

    RectFullness = Rect(x+(WidthBack-WidthScale)//2+5, y+(HeightBack-HeightScale)//2+(HeightScale-HeightFullness)//2, WidthFullness, HeightFullness)

    draw.rect(Surface, "#ff8d18", RectBack)
    draw.rect(Surface, "#000000", RectExperience)
    draw.rect(Surface, "#2ed132", RectFullness)

    Exp = image.load("image/HUD/Exp2.png").convert_alpha()
    Exp = transform.scale(Exp, (90, 84))
    RectExp=Exp.get_rect(right=RectBack.left+25, centery=(RectBack.centery-10))

    
    Surface.blit(Exp,RectExp)
    # lightning = image.load("image/HUD/lightning.png")
    # lightning = transform.scale(lightning, (84, 90))
    # RectLightning = lightning.get_rect(center=(RectBack.left+10, RectBack.centery))

    # Surface.blit(lightning, RectLightning)
