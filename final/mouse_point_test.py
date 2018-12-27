from engine import Thing
import pygame
from image_utils import resize_image
pygame.init()

WIDTH = 1000
HEIGHT = 1000
FRAME_RATE = 2

# images = ['hard_left_small.png', 'left_small.png', 'small.png', 'right_small.png', 'hard_right_small.png']
images = ['hardest_left.png', 'hardest_left_fin.png','harder_left.png','harder_left_fin.png','left.png','left_fin.png',
            'center_left.png','center.png','center_right.png','right.png','right_fin.png','hard_right.png','hard_right_fin.png',
                'hardest_right.png','hardest_right_fin.png']
images = ['movement_images/v2/'+im for im in images]
images = [resize_image(im,(250,250)) for im in images]
images = [pygame.image.load(im) for im in images]

my_thing = Thing(images, (250+250/2,250+250/2))

bg_color = (0,0,0)
size = (WIDTH, HEIGHT)
display = pygame.display.set_mode(size)
pygame.display.set_caption('Thing class test')
clock = pygame.time.Clock()
go = True

while go:
    display.fill(bg_color)
    mouse_cords = pygame.mouse.get_pos()
    my_thing.point_at_cords(mouse_cords)
    my_thing.move(mouse_cords)
    my_thing.update()
    my_thing.draw(display=display)
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            go = False
    clock.tick(FRAME_RATE)
    pygame.display.update()
