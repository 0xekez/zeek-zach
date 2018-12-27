import pygame
# for angle calculations
from math import atan2

def next_image_generator(self):
    '''
    moves up and down the list of images yielding them one at a time
    '''
    i = 0
    while True:
        for i in range(0, len(self.images)):
            self.current_image_index = i
            yield self.images[i]
        for i in range(len(self.images)-2, 0, -1):
            self.current_image_index = i
            yield self.images[i]

class Thing(pygame.sprite.Sprite):
    def __init__(self, image_files, location):
        '''
        initialize a new Thing
        IN : image_files -> filenames of images to cycle through in order
             location -> (x, y)
        '''
        pygame.sprite.Sprite.__init__(self)
        # initialize the sprite to the first image in the list of images
        self.images = []
        for image in image_files:
            print(image)
            self.images.append(pygame.image.load(image))
        #self.images = [pygame.image.load(image) for image in image_files]
        self.current_image_index = 0
        # the image that will be shown
        self.display_image = self.images[0]
        self.rect = self.display_image.get_rect()
        self.rect.left, self.rect.top = location
        self.angle = 0
        self.image_getter = next_image_generator(self)
    def set_rotation(self, angle):
        '''
        rotate Thing to new angle
        IN : angle to rotate Thing to
        '''
        self.angle = angle
        self.display_image = pygame.transform.rotate(self.images[self.current_image_index], self.angle)
        self.rect = self.display_image.get_rect(center = self.rect.center)
    def draw(self, display):
        display.blit(self.display_image, self.rect.topleft)
    def point_at_cords(self, cords):
        '''
        point the center of the top of the Thing's rect at cords
        IN : cords -> (x, y) to point the Thing at
        '''
        x, y = self.rect.center
        delta_y = cords[1] - y
        delta_x = cords[0] - x
        angle_rads = atan2(delta_y, delta_x)
        self.angle = 270 - 57.29578*angle_rads
    def move(self, target_cords):
        x, y = self.rect.center
        t_x, t_y = target_cords
        if t_x > x:
            x += 6
        elif t_x < x:
            x -= 6
        if t_y > y:
            y += 6
        elif t_y < y:
            y -= 6
        self.rect.center = (x, y)
    def update(self):
        self.display_image = next(self.image_getter)
        self.set_rotation(self.angle)
