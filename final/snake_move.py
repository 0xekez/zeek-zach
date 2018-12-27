import pygame
pygame.init()
MOVE_SPEED = 4
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SEG_WAIT = 1
DIST_SCALE = 0.25

class Segment():
    def __init__(self, lead = None, cords = None):
        self.lead = lead
        self.seg_wait = SEG_WAIT
        if self.lead:
            self.x = lead.x + 10
            self.y = lead.y
            self.move_speed = self.lead.move_speed
        elif cords:
            self.move_speed = MOVE_SPEED
            self.x = cords[0]
            self.y = cords[1]
        else:
            raise AttributeError('must provide either a lead segment or cords')
    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(self.x, self.y, 10,10))
    def move(self, direction = None):
        if self.lead:
            if self.lead.seg_wait:
                self.lead.seg_wait -= 1
            else:
                seperation_x = abs(self.lead.x - self.x)
                seperation_y = abs(self.lead.y - self.y)
                scale_x = seperation_x*DIST_SCALE
                scale_y = seperation_y*DIST_SCALE

                if self.lead.x > self.x:
                    self.x += self.move_speed + scale_x
                elif self.lead.x < self.y:
                    self.x -= self.move_speed + scale_x
                if self.lead.y > self.y:
                    self.y += self.move_speed + scale_y
                elif self.lead.y < self.y:
                    self.y -= self.move_speed + scale_y
                self.lead.seg_wait = SEG_WAIT
        else:
            if direction == UP:
                self.y -= self.move_speed
            elif direction == DOWN:
                self.y += self.move_speed
            elif direction == LEFT:
                self.x -= self.move_speed
            elif direction == RIGHT:
                self.x += self.move_speed
class Snake():
    def __init__(self):
        self.segments = []
    def add_segment(self, cords = None):
        if len(self.segments) == 0:
            assert cords, 'must pass cords for first segment in snake'
            self.segments.append(Segment(cords = cords))
        else:
            new = Segment(lead = self.segments[-1])
            self.segments.append(new)
    def update_segments(self):
        for segment in self.segments:
            segment.move()
    def draw_segments(self, screen):
        for segment in self.segments:
            segment.draw(screen)
    def move(self, direction):
        lead = self.segments[0]
        lead.move(direction=direction)cd

width = 500
height = 500
size = (width, height)
display = pygame.display.set_mode(size)
pygame.display.set_caption('snake move test')
go = True
bg_color = (255,255,255)
snake = Snake()
snake.add_segment((50,50))

while go:
    display.fill(bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.move(LEFT)
    if keys[pygame.K_RIGHT]:
        snake.move(RIGHT)
    if keys[pygame.K_DOWN]:
        snake.move(DOWN)
    if keys[pygame.K_UP]:
        snake.move(UP)
    if keys[pygame.K_a]:
        snake.add_segment()
    snake.update_segments()
    snake.draw_segments(display)
    pygame.display.update()
