import pygame

# EXP bar variables
exp_width = 0          # current width of the bar (starts empty)
exp_height = 50        # height of the bar
exp_max_width = 200    # full width of the bar
exp_x = 20             # x position
exp_y = 400            # y position

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("This might take a while.")

running = True
while running:
    for event in pygame.event.get():
        screen.fill((100,150,200))

        if event.type == pygame.KEYDOWN:  # detect key press
            if exp_width < exp_max_width:  # only grow if not full
                exp_width += 20           # increase width by 20 pixels


        #screen shows on the surface, RGB, screen position, dimensions
        pygame.draw.rect(screen, (225, 0, 0), (20, 400, 200, 50))
        
        # Draw the EXP bar (green)
        pygame.draw.rect(screen, (0, 255, 0), (exp_x, exp_y, exp_width, exp_height))

        pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False