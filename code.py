import pygame
import sys
import random



pygame.init()
info = pygame.display.Info()
w, h = info.current_w, info.current_h
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.RESIZABLE)
pygame.display.set_caption('physics, math, code & fun')

pygame.mixer.init()
beep = pygame.mixer.Sound("beep.mp3")
font = pygame.font.SysFont('Arial', 30)


class Particles:
    def __init__(self, x, y):
        self.rect =  pygame.Rect(x, y, 20, 20)
        self.visible = True
        self.color = [30,255,30]
    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.color, self.rect)

particles = []
n = 300
for i in range(0, 300):
    particles.append(Particles(random.randint(0, w - 10), random.randint(0, h - 10)))
    
class Player:
    def __init__(self, x, y):
        self.rect =  pygame.Rect(x, y, 50, 50)
        self.color = [255,150,30]
        self.velocity = [0.7, 0.7]
   
    def change(self):
        v1 = random.randint(0,1)
        if v1 == 0:
            self.velocity[0] = -self.velocity[0]
        v2 = random.randint(0,1)
        if v2 == 0:
            self.velocity[1] = -self.velocity[1]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    def move(self):
        global n
        last_pos = [self.rect.x, self.rect.y]

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
        if((self.rect.x) <= 0 or (self.rect.x + self.rect.width) >= w):
            self.velocity[0] = -self.velocity[0]
            self.rect.x = last_pos[0]
        if((self.rect.y) <= 0 or (self.rect.y + self.rect.height) >= h):
            self.velocity[1] = -self.velocity[1]
            self.rect.y = last_pos[1]

        
        for l in particles:
            if l.rect.colliderect(self.rect):
                if l.visible:
                    l.visible = False
                    self.rect.width += 3
                    self.rect.height += 3
                    beep.play()
                    self.velocity[0] += (self.velocity[0] / abs(self.velocity[0])) * 0.01
                    self.velocity[1] += (self.velocity[1] / abs(self.velocity[1])) *0.01
                    self.change()
                    n -= 1
        
player = Player(random.randint(0, w), random.randint(0, h))


def Update(screen):
    screen.fill((0,0,0))
    
    for p in particles:
        p.draw(screen)
    
    player.draw(screen)
    player.move()

    text = font.render(str(n), True, (255,255,255))
    screen.blit(text, pygame.Rect(player.rect.x, player.rect.y, 400,300))

    pygame.display.flip()
    


isEnd = False
while not isEnd:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isEnd = True
            
    Update(screen)
    
pygame.quit()
sys.exit()
