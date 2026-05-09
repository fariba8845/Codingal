import pygame
pygame.init()
screen= pygame.display.set_mode((640,480))
pygame.display.set_caption("My first game screen!")

font= pygame.font.Font(None,25)
text_surface = font.render('This is a red rectangle!', True, (0,0,0))

done= False

while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done=True
            
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (255, 0, 0), [270, 190, 100, 50])
    screen.blit(text_surface, (210, 160))
    
    pygame.display.flip()


