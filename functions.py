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
            if c[0] == 127:
                char_img = clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                self.characters[self.character_order[character_count]] = transform.scale(char_img,(char_img.get_width()*k,char_img.get_height()*k))
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
