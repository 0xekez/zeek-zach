FRAME_RATE = 2
WIDTH = 1000
HEIGHT  = 1000

import pygame
from image_utils import resize_image
pygame.init()

# names of images here
# they should be inside quotes and comma seperated
# ex images = ['image1', 'image2']
images = ['hardest_left_fin','hardest_left','hard_left_fin','hard_left','center_left','center','center_right','hard_right_right','hard_right',
            'hard_right_left','hard_right','hardest_right_fin','hardest_right']
images = ['movement_images/v3/'+im+'.png' for im in images]
# images = [resize_image(im,(250,250)) for im in images]
images = [pygame.image.load(im) for im in images]

def image_getter():
    i = 0
    while True:
        for i in range(0, len(images)):
            yield images[i]
        for i in range(len(images)-2, 0, -1):
            yield images[i]

bg_color = (0,0,0)
size = (WIDTH, HEIGHT)
display = pygame.display.set_mode(size)
pygame.display.set_caption('movement annimation test')
clock = pygame.time.Clock()
go = True
getter = image_getter()

while go:
    display.fill(bg_color)
    display.blit(next(getter), (500-250/2, 500-250/2))
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            go = False
    clock.tick(FRAME_RATE)
    pygame.display.update()
