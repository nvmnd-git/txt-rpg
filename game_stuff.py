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

Clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # detect key press
            if exp_width < exp_max_width:  # only grow if not full
                exp_width += 20           # increase width by 20 pixels

        screen.fill((100,150,200))

        #screen shows on the surface, RGB, screen position, dimensions
        pygame.draw.rect(screen, (225, 0, 0), (20, 400, 200, 50))
        
        # Draw the EXP bar (green)
        pygame.draw.rect(screen, (0, 255, 0), (exp_x, exp_y, exp_width, exp_height))

        # Calculate EXP as a number
        exp_value = int((exp_width / exp_max_width) * 100) # percentage

        # Render the text
        exp_text = font.render(f"{exp_value}%", True, (255, 255, 255)) # white text

        # Get the text rectangle and center in the bar
        text_rect = exp_text.get_rect(center=(exp_x + exp_max_width // 2, exp_y + exp_height // 2))

        # Draw the text on the screen
        screen.blit(exp_text, text_rect)


        pygame.display.flip()
        Clock.tick(60)


