import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

pygame.draw.circle(screen, "yellow", (200, 200), 200)
pygame.draw.circle(screen, "red", (100, 150), 40)
pygame.draw.circle(screen, "red", (300, 150), 40)
pygame.draw.circle(screen, "black", (100, 150), 20)
pygame.draw.circle(screen, "black", (300, 150), 20)
pygame.draw.rect(screen, "black", (70, 300, 250, 30))
pygame.draw.line(screen, "black", (70, 70), (150, 120), 30)
pygame.draw.line(screen, "black", (330, 70), (250, 120), 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
