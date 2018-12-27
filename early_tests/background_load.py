import pygame

class Whale(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.og_image = pygame.image.load(image_file)
        self.total_rotation_angle = 0
        self.image = self.og_image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    def rot_center(self, angle):
        """rotate an image while keeping its center"""
        self.total_rotation_angle += angle
        if self.total_rotation_angle > 360:
            self.total_rotation_angle -= 360
        self.image = pygame.transform.rotate(self.og_image, self.total_rotation_angle)
        self.rect = self.image.get_rect(center = self.rect.center)

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("my ass")

clock = pygame.time.Clock()
bg_img = pygame.image.load('blue.png')

my_shape = Whale('squarewhale.png', (0,0))

go = True
while go:
    clock.tick(40)
    screen.blit(bg_img, (0,0))

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            go = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        my_shape.rect.left -= 1
    if keys[pygame.K_RIGHT]:
        my_shape.rect.left += 1
    if keys[pygame.K_DOWN]:
        my_shape.rect.top += 1
    if keys[pygame.K_UP]:
        # my_shape.rect.top -= 1
        my_shape.rot_center(45)
    screen.blit(my_shape.image, my_shape.rect)

    pygame.display.update()
