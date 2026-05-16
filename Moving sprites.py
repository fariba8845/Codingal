import pygame
pygame.init()

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    
all_sprites_list= pygame.sprite.Group()
sp1= Sprite((255,0,0),20,30)
sp1.rect.x= 250
sp1.rect.y= 200
all_sprites_list.add(sp1)

sp2= Sprite((0,0,255),20,30)
sp2.rect.x= 50
sp2.rect.y= 100
all_sprites_list.add(sp2)

screen= pygame.display.set_mode((500,400))
pygame.display.set_caption(("Moving sprite with arrow keys"))

bg_color= pygame.Color("black")
exit=False
clock= pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit= True
        elif event.type== pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                sp1.rect.x-= 5
            elif event.key== pygame.K_RIGHT:
                sp1.rect.x+= 5
            elif event.key== pygame.K_UP:
                sp1.rect.y-= 5
            elif event.key== pygame.K_DOWN:
                sp1.rect.y+= 5
                
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    