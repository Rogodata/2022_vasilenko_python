import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 800))


def make_girl(surface, x_pos, y_pos, width, height, mirror=False):
    '''
        Рисует левую девочку.
        surface - объект pygame.Surface
        x_pos, y_pos - координаты ладони левой руки
        width, height - ширина и высота изображения
        mirror - отзеркаливание изображения относительно вертикальной оси тела
    '''
    surface_girl_1 = pygame.Surface((1200, 800), pygame.SRCALPHA)
    surface_girl_0 = pygame.Surface((350, 550), pygame.SRCALPHA)
    pygame.draw.polygon(surface_girl_1, (239, 61, 255), ((800, 250), (700, 550), (900, 550)))
    pygame.draw.circle(surface_girl_1, (237, 204, 161), (800, 220), 60)
    pygame.draw.line(surface_girl_1, (0, 0, 0), (950, 300), (900, 360), 3)
    pygame.draw.line(surface_girl_1, (0, 0, 0), (820, 340), (900, 360), 3)
    pygame.draw.line(surface_girl_1, (0, 0, 0), (780, 340), (600, 410), 3)
    pygame.draw.line(surface_girl_1, (0, 0, 0), (750, 550), (750, 700), 3)
    pygame.draw.line(surface_girl_1, (0, 0, 0), (700, 700), (750, 700), 3)
    pygame.draw.line(surface_girl_1, (0, 0, 0), (820, 550), (820, 700), 3)
    pygame.draw.line(surface_girl_1, (0, 0, 0), (820, 700), (870, 700), 3)
    surface_girl_0.blit(surface_girl_1, area=[(600, 160), (950, 710)], dest=(0, 0))
    surface_girl_0 = pygame.transform.scale(surface_girl_0, (width, height))
    if mirror:
        surface_girl_0 = pygame.transform.flip(surface_girl_0, True, False)
    surface.blit(surface_girl_0, dest=(x_pos, y_pos))


def make_dude(surface, x_pos, y_pos, width, height, mirror=False):
    surface_dude_1 = pygame.Surface((1200, 800), pygame.SRCALPHA)
    surface_dude_0 = pygame.Surface((400, 580), pygame.SRCALPHA)
    pygame.draw.ellipse(surface_dude_1, (167, 141, 179), (300, 250, 150, 300))
    pygame.draw.circle(surface_dude_1, (237, 204, 161), (375, 200), 70)
    pygame.draw.line(surface_dude_1, (0, 0, 0), (340, 300), (210, 410), 3)
    pygame.draw.line(surface_dude_1, (0, 0, 0), (420, 300), (600, 410), 3)
    pygame.draw.line(surface_dude_1, (0, 0, 0), (330, 520), (250, 700), 3)
    pygame.draw.line(surface_dude_1, (0, 0, 0), (200, 700), (250, 700), 3)
    pygame.draw.line(surface_dude_1, (0, 0, 0), (400, 520), (480, 700), 3)
    pygame.draw.line(surface_dude_1, (0, 0, 0), (530, 700), (480, 700), 3)
    surface_dude_0.blit(surface_dude_1, area=[(200, 130), (600, 710)], dest=(0, 0))
    surface_dude_0 = pygame.transform.scale(surface_dude_0, (width, height))
    if mirror:
        surface_dude_0 = pygame.transform.flip(surface_dude_0, True, False)
    surface.blit(surface_dude_0, dest=(x_pos, y_pos))


def make_icecream(surface):
    pygame.draw.polygon(surface, (235, 152, 59), ((225, 425), (100, 400), (170, 330)))
    pygame.draw.circle(surface, (112, 87, 59), (110, 370), 30)
    pygame.draw.circle(surface, (255, 61, 87), (140, 340), 25)
    pygame.draw.circle(surface, (212, 252, 255), (110, 335), 20)


def make_balloon(surface):
    pygame.draw.polygon(surface, (255, 5, 55), ((920, 100), (1050, 140), (950, 250)))
    pygame.draw.circle(surface, (255, 5, 55), (960, 100), 40)
    pygame.draw.circle(surface, (255, 5, 55), (1025, 110), 40)
    pygame.draw.line(surface, (0, 0, 0), (950, 250), (940, 450), 3)


# background
pygame.draw.rect(screen, (122, 215, 255), (0, 0, 1200, 400))
pygame.draw.rect(screen, (91, 235, 111), (0, 400, 1200, 400))

'''
# make left girl
surface_girl_1 = pygame.Surface((1200, 800), pygame.SRCALPHA)
make_girl(surface_girl_1)
surface_girl_1 = pygame.transform.scale(surface_girl_1, (750, 500))
screen.blit(surface_girl_1, (0, 150))'''

make_girl(screen, 370, 250, 220, 340,)
make_girl(screen, 590, 250, 220, 340, mirror=True)

'''
# make right girl
surface_girl_2 = pygame.Surface((1200, 800), pygame.SRCALPHA)
make_girl(surface_girl_2)
surface_girl_2 = pygame.transform.scale(surface_girl_2, (750, 500))
surface_girl_2 = pygame.transform.flip(surface_girl_2, True, False)
screen.blit(surface_girl_2, (437, 150))


# make left dude
surface_dude_1 = pygame.Surface((1200, 800), pygame.SRCALPHA)
make_dude(surface_dude_1)
surface_dude_1 = pygame.transform.scale(surface_dude_1, (750, 500))
screen.blit(surface_dude_1, (0, 150))
'''

make_dude(screen, 120, 230, 250, 360)
make_dude(screen, 810, 230, 250, 360, mirror=True)

'''
# make right dude
surface_dude_2 = pygame.Surface((1200, 800), pygame.SRCALPHA)
make_dude(surface_dude_2)
surface_dude_2 = pygame.transform.scale(surface_dude_2, (750, 500))
surface_dude_2 = pygame.transform.flip(surface_dude_2, True, False)
screen.blit(surface_dude_2, (434, 150))
'''

# make right ice cream
surface_icecream_1 = pygame.Surface((1200, 800), pygame.SRCALPHA)
make_icecream(surface_icecream_1)
surface_icecream_1 = pygame.transform.scale(surface_icecream_1, (750, 500))
surface_icecream_1 = pygame.transform.rotate(surface_icecream_1, 270)
screen.blit(surface_icecream_1, (817, 268))

# make left balloon
surface_balloon = pygame.Surface((1200, 800), pygame.SRCALPHA)
make_balloon(surface_balloon)
surface_balloon = pygame.transform.scale(surface_balloon, (750, 500))
surface_balloon = pygame.transform.flip(surface_balloon, True, False)
screen.blit(surface_balloon, (-30, 130))

# make center ice cream
surface_icecream_2 = pygame.Surface((1200, 800), pygame.SRCALPHA)
make_icecream(surface_icecream_2)
surface_icecream_2 = pygame.transform.scale(surface_icecream_2, (1200, 800))
surface_icecream_2 = pygame.transform.rotate(surface_icecream_2, 300)
screen.blit(surface_icecream_2, (170, -200))
pygame.draw.line(screen, (0, 0, 0), (610, 200), (590, 345), 3)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
