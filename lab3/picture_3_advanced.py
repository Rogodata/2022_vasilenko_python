import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 800))


def make_girl(surface, x_pos, y_pos, width, height, mirror=False):
    '''
    Рисует девочку
    :param surface - объект pygame.Surface
    :param x_pos координата x ладони несогнутой руки(она слева относительно нас)
    :param y_pos - координата y ладони несогнутой руки(она слева относительно нас)
    :param width - ширина изображения
    :param height - высота изображения
    :param mirror - отзеркаливание изображения относительно вертикальной оси тела
    Это для правой девочки
    '''
    y_pos = y_pos - height * 260 // 550
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
    '''
    Рисует мальчика.
    :param surface - объект pygame.Surface
    :param x_pos координатa x левой (относительно смотрящего) руки левого мальчика
    :param y_pos координатa y левой (относительно смотрящего) руки левого мальчика
    :param width - ширина изображения
    :param height - высота изображения
    :param mirror - отзеркаливание изображения относительно вертикальной оси тела
    :param Это для правого мальчика
    '''
    y_pos = y_pos - height // 2
    surface_dude_1 = pygame.Surface((1200, 800), pygame.SRCALPHA)
    surface_dude_0 = pygame.Surface((400, 573), pygame.SRCALPHA)
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


def make_icecream(surface, x_pos, y_pos, width, height, angle=0, mirror=False):
    '''
    Рисует мороженое.
    :param surface - объект pygame.Surface
    :param x_pos координата x правого нижнего угла прямоугольника, стороны которого параллельны осям координат, в который вписано мороженое
    :param y_pos координата y правого нижнего угла прямоугольника, стороны которого параллельны осям координат, в который вписано мороженое
    :param width - ширина изображения
    :param height - высота изображения
    :param mirror - отзеркаливание изображения относительно вертикальной оси симметрии прямоугольника
    :param angle - поворот изображения относительно x_pos y_pos (правого верхнего угла изображения)
    '''
    y_pos = y_pos - height
    x_pos = x_pos - width
    surface_icecream_1 = pygame.Surface((1200, 800), pygame.SRCALPHA)
    surface_icecream_0 = pygame.Surface((90, 105), pygame.SRCALPHA)
    pygame.draw.polygon(surface_icecream_1, (235, 152, 59), ((225, 425), (100, 400), (170, 330)))
    pygame.draw.circle(surface_icecream_1, (112, 87, 59), (110, 370), 30)
    pygame.draw.circle(surface_icecream_1, (255, 61, 87), (140, 340), 25)
    pygame.draw.circle(surface_icecream_1, (212, 252, 255), (110, 335), 20)
    surface_icecream_0.blit(surface_icecream_1, area=[(80, 315), (170, 425)], dest=(0, 0))
    surface_icecream_0 = pygame.transform.rotate(surface_icecream_0, angle)
    surface_icecream_0 = pygame.transform.scale(surface_icecream_0, (width, height))
    if mirror:
        surface_icecream_0 = pygame.transform.flip(surface_icecream_0, True, False)
    surface.blit(surface_icecream_0, dest=(x_pos, y_pos))


def make_balloon(surface, x_pos, y_pos, width, height, mirror=False):
    '''
    Рисует шарик.
    :param surface - объект pygame.Surface
    :param x_pos координата x левого верхнего угла прмоугольника, стороны которого параллельны осям координат, в который вписан шарик
    :param y_pos координата y левого верхнего угла прмоугольника, стороны которого параллельны осям координат, в который вписан шарик
    :param width - ширина изображения
    :param height - высота изображения
    :param mirror - отзеркаливание изображения относительно вертикальной оси симметрии прямоугольника
    '''
    surface_balloon_1 = pygame.Surface((1200, 800), pygame.SRCALPHA)
    surface_balloon_0 = pygame.Surface((145, 190), pygame.SRCALPHA)
    pygame.draw.polygon(surface_balloon_1, (255, 5, 55), ((920, 100), (1050, 140), (950, 250)))
    pygame.draw.circle(surface_balloon_1, (255, 5, 55), (960, 100), 40)
    pygame.draw.circle(surface_balloon_1, (255, 5, 55), (1025, 110), 40)
    surface_balloon_0.blit(surface_balloon_1, area=[(920, 60), (1065, 250)], dest=(0, 0))
    surface_balloon_0 = pygame.transform.scale(surface_balloon_0, (width, height))
    if mirror:
        surface_balloon_0 = pygame.transform.flip(surface_balloon_0, True, False)
    surface.blit(surface_balloon_0, dest=(x_pos, y_pos))


# background
pygame.draw.rect(screen, (122, 215, 255), (0, 0, 1200, 400))
pygame.draw.rect(screen, (91, 235, 111), (0, 400, 1200, 400))

# making girls
make_girl(screen, 370, 410, 220, 340, )
make_girl(screen, 590, 410, 220, 340, mirror=True)

# making dudes
make_dude(screen, 120, 410, 250, 360)
make_dude(screen, 810, 410, 250, 360, mirror=True)

# making ice creams
make_icecream(screen, 1110, 410, 80, 180, angle=290)
make_icecream(screen, 650, 210, 80, 180, angle=320)
pygame.draw.line(screen, (0, 0, 0), (610, 200), (590, 345), 3)

# making balloon
make_balloon(screen, 40, 130, 80, 120, mirror=True)
pygame.draw.line(screen, (0, 0, 0), (130, 400), (100, 250), 3)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
