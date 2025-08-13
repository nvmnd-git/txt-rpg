import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("This might take a while.")

running = True
while running:
    for event in pygame.event.get():
        screen.fill((100,150,200))

        #screen shows on the surface, RGB, screen position, dimensions
        pygame.draw.rect(screen, (0, 225, 0), (20, 400, 200, 60))
        
        pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False