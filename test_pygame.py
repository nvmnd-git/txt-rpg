import pygame
import time

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame Test")

print("Pygame window should open now.")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((100, 150, 200))
    pygame.display.flip()

print("Exited game loop, quitting pygame.")
pygame.quit()
time.sleep(2)  # keep window open 2 seconds before closing console

