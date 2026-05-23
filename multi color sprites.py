import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGE_EVENT= pygame.USEREVENT+ 1
pygame.time.set_timer(SPRITE_COLOR_CHANGE_EVENT, 1000)

YELLOW= pygame.Color('yellow')
RED= pygame.Color('red')
GREEN= pygame.Color('green')
WHITE= pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def change_color(self):
        self.image.fill(random.choice([WHITE,GREEN,RED,YELLOW]))
    
all_sprites_list= pygame.sprite.Group()
sp1= Sprite(WHITE,20,30)
sp1.rect.x=250
sp1.rect.y=200
all_sprites_list.add(sp1)
sp2= Sprite(RED,20,30)
sp2.rect.x=100
sp2.rect.y=100
all_sprites_list.add(sp2)
pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
screen= pygame.display.set_mode((500,400))
pygame.display.set_caption("Color change game!")

bg_color= pygame.color.Color("yellow")
screen.fill(bg_color)

exit= False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit= True
        elif event.type== SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
            sp2.change_color()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
    
pygame.quit()
