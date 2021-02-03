from pygame import *

# def TrueForMillisec(currentTime,millisec):
#     exTime


def clip(surf,x,y,x_size,y_size):
    handle_surf = surf.copy()
    clipR = Rect(x,y,x_size,y_size)
    handle_surf.set_clip(clipR)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()

class Font():
    def __init__(self, path,k=1):
        self.spacing = 1*k
        self.character_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']
        font_img = image.load('image/fonts/'+path+'.png').convert_alpha()
        current_char_width = 0
        self.characters = {}
        character_count = 0
        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            # print(x,' ',c[0])
            if c[0] == 127:
                char_img = clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                self.characters[self.character_order[character_count]] = transform.scale(char_img,(char_img.get_width()*k,char_img.get_height()*k))
                # print(self.character_order[character_count])
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters['A'].get_width()

    def render(self, surf, text, loc):
        x_offset = 0
        for char in text:
            if char != ' ':
                surf.blit(self.characters[char], (loc[0] + x_offset, loc[1]))
                x_offset += self.characters[char].get_width() + self.spacing
            else:
                x_offset += self.space_width + self.spacing


def FinishLevel(screen,slime,font):
    done = True
    showtext = 4000
    CheckTime=0
    while done:
        screen.fill((0, 0, 0))
        font[4].render(screen, "Win!", (display.Info().current_w//2-33, display.Info().current_h//10))
        font[1].render(screen, 'Wasted time on the level: '+ str(slime.LevelTime/1000)+' s', (display.Info().current_w//2-33, display.Info().current_h//5))
        # screen.blit(deadSurFaceObj, textRectObj)
        display.update()
        if time.get_ticks()-CheckTime > 1000:
            showtext -= 1000
            CheckTime = time.get_ticks()

        if showtext <= 0:
            showtext = 0
            done = False
        slime.win = False
        slime.StartLevelTime=time.get_ticks()


def DeadSlime(screen, slime, font):
    done = True
    showtext = 2000
    CheckTime = 0
    while done:
        screen.fill((0, 0, 0))
        font[4].render(screen, "Dead!", (display.Info().current_w//2-43, display.Info().current_h//2))

        display.update()
        if time.get_ticks()-CheckTime > 1000:
            showtext -= 1000
            CheckTime = time.get_ticks()

        if showtext <= 0:
            showtext = 0
            done = False
        slime.dead = False


    # if time.get_ticks()-CheckTimeExp > 10:
    #     CheckTimeExp = time.get_ticks()
    #     if ShowScaleExp:
    #         if t==-1:
    #             t=0
    #             c=-50
    #             a=3
    #         if t>=1 and t<a+1:
    #             ShowScaleExpCold=True
    #         else:
    #             ShowScaleExpCold=False

    #         if ShowScaleExpCold:
    #             y=50

    #         if t<1 and not ShowScaleExpCold:
    #             y = -70*(t-1)**2+50

    #         if t>=a+1:
    #             y = -70*(t-(a+1))**2+50

    #         DrawScaleExperience(screen,600,y,slime.SumExp)
    #         if t>=0:
    #             t+=1/FPS

    #         if t>a+2:
    #             t=-1
    #             ShowScaleExp=False
    #         # print(time.get_ticks()/1000)
