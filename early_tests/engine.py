import pygame

class Thing(pygame.sprite.Sprite):
    def __init__(self, images, location):
        pygame.sprite.Sprite.__init__(self)
        # initialize the sprite to the first image in the list of images
        self.images = [pygame.image.load(image) for image in images]
        self.current_image = 0
        # the image that will be shown
        self.display_image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    def rot_center(self, angle):
        '''
        rotate Thing to new angle
        IN : angle to rotate image to
        '''
        self.display_image = pygame.transform.rotate(self.images[self.current_image], angle)
        self.rect = self.display_image.get_rect(center = self.rect.center)

'''
need to work out a way to abstract away which image corresponds to which
motion / activity
'''
