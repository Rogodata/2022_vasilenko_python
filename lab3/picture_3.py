import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 800))

# background
pygame.draw.rect(screen, (122, 215, 255), (0, 0, 1200, 400))
pygame.draw.rect(screen, (91, 235, 111), (0, 400, 1200, 400))

# left dude
pygame.draw.ellipse(screen, (167, 141, 179), (300, 250, 150, 300))
pygame.draw.circle(screen, (237, 204, 161), (375, 200), 70)
pygame.draw.polygon(screen, (235, 152, 59), ((225, 425), (100, 400), (170, 330)))
pygame.draw.circle(screen, (112, 87, 59), (110, 370), 30)
pygame.draw.circle(screen, (255, 61, 87), (140, 340), 25)
pygame.draw.circle(screen, (212, 252, 255), (110, 335), 20)
pygame.draw.line(screen, (0, 0, 0), (340, 300), (210, 410), 3)
pygame.draw.line(screen, (0, 0, 0), (420, 300), (600, 410), 3)
pygame.draw.line(screen, (0, 0, 0), (330, 520), (250, 700), 3)
pygame.draw.line(screen, (0, 0, 0), (200, 700), (250, 700), 3)
pygame.draw.line(screen, (0, 0, 0), (400, 520), (480, 700), 3)
pygame.draw.line(screen, (0, 0, 0), (530, 700), (480, 700), 3)

# girl
pygame.draw.polygon(screen, (239, 61, 255), ((800, 250), (700, 550), (900, 550)))
pygame.draw.circle(screen, (237, 204, 161), (800, 220), 60)
pygame.draw.polygon(screen, (255, 5, 55), ((920, 100), (1050, 140), (950, 250)))
pygame.draw.circle(screen, (255, 5, 55), (960, 100), 40)
pygame.draw.circle(screen, (255, 5, 55), (1025, 110), 40)
pygame.draw.line(screen, (0, 0, 0), (950, 250), (940, 450), 3)
pygame.draw.line(screen, (0, 0, 0), (950, 300), (900, 360), 3)
pygame.draw.line(screen, (0, 0, 0), (820, 340), (900, 360), 3)
pygame.draw.line(screen, (0, 0, 0), (780, 340), (600, 410), 3)
pygame.draw.line(screen, (0, 0, 0), (750, 550), (750, 700), 3)
pygame.draw.line(screen, (0, 0, 0), (700, 700), (750, 700), 3)
pygame.draw.line(screen, (0, 0, 0), (820, 550), (820, 700), 3)
pygame.draw.line(screen, (0, 0, 0), (820, 700), (870, 700), 3)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
