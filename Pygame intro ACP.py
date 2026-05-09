import pygame
pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500 
screen_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first Game Screen!")

bg_image = pygame.image.load(r'C:\Users\Hp\.gemini\antigravity\scratch\pygame_project\images\DSC00006.JPG')
bg_image = pygame.transform.scale(bg_image, (300, 300))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen_display.blit(bg_image, (0, 0))
    pygame.display.flip()

pygame.quit()
