# import pygame
# pygame.init()

# screenWidth = 500
# win = pygame.display.set_mode((500, 480))

# walkRight = [pygame.image.load('./Game/R1.png'), pygame.image.load('./Game/R2.png'), pygame.image.load('./Game/R3.png'), pygame.image.load('./Game/R4.png'), pygame.image.load('./Game/R5.png'), pygame.image.load('./Game/R6.png'), pygame.image.load('./Game/R7.png'), pygame.image.load('./Game/R8.png'), pygame.image.load('./Game/R9.png')]
# walkLeft = [pygame.image.load('./Game/L1.png'), pygame.image.load('./Game/L2.png'), pygame.image.load('./Game/L3.png'), pygame.image.load('./Game/L4.png'), pygame.image.load('./Game/L5.png'), pygame.image.load('./Game/L6.png'), pygame.image.load('./Game/L7.png'), pygame.image.load('./Game/L8.png'), pygame.image.load('./Game/L9.png')]
# bg = pygame.image.load('./Game/bg.jpg')
# char = pygame.image.load('./Game/standing.png')

# pygame.display.set_caption("Yayayy")

# clock  = pygame.time.Clock()

# x = 50
# y = 425
# width = 64
# height = 64
# vel = 5

# isJump = False
# jumpCount = 10

# left = False
# right = False
# walkCount = 0

# run = True

# def redrawGameWindow():
#     global walkCount
#     win.blit(bg, (0,0))

#     if walkCount + 1 >= 27:
#         walkCount = 0

#     if left:
#         win.blit(walkLeft[walkCount//3], (x,y))
#         walkCount += 1
#     elif right:
#         win.blit(walkRight[walkCount//3], (x,y))
#         walkCount += 1
#     else:
#         win.blit(char, (x,y))
#     pygame.display.update()


# while run:
#     clock.tick(27)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and x > 0:
#         x -= vel
#         left = True
#         right = False
#     elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
#         x += vel
#         left = False
#         right = True
#     else:
#         left = False
#         right = False
#         walkCount = 0
#     if not isJump:
#         if keys[pygame.K_SPACE]:
#             isJump = True
#             right = False
#             left = False
#             walkCount  = 0
#     else:
#         if jumpCount >= -10:
#             neg = 1
#             if jumpCount < 0:
#                 neg = -1
#             y -= (jumpCount ** 2) * 0.5 * neg
#             jumpCount -= 1

#         else:
#             isJump = False
#             jumpCount = 10

#     redrawGameWindow()

# pygame.quit()


import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('./Game/R1.png'), pygame.image.load('./Game/R2.png'), pygame.image.load('./Game/R3.png'), pygame.image.load('./Game/R4.png'), pygame.image.load('./Game/R5.png'), pygame.image.load('./Game/R6.png'), pygame.image.load('./Game/R7.png'), pygame.image.load('./Game/R8.png'), pygame.image.load('./Game/R9.png')]
walkLeft = [pygame.image.load('./Game/L1.png'), pygame.image.load('./Game/L2.png'), pygame.image.load('./Game/L3.png'), pygame.image.load('./Game/L4.png'), pygame.image.load('./Game/L5.png'), pygame.image.load('./Game/L6.png'), pygame.image.load('./Game/L7.png'), pygame.image.load('./Game/L8.png'), pygame.image.load('./Game/L9.png')]
bg = pygame.image.load('./Game/bg.jpg')
char = pygame.image.load('./Game/standing.png')

clock = pygame.time.Clock()


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class enemy(object):
    walkRight = [pygame.image.load('./Game/R1E.png'), pygame.image.load('./Game/R2E.png'), pygame.image.load('./Game/R3E.png'), pygame.image.load('./Game/R4E.png'), pygame.image.load('./Game/R5E.png'), pygame.image.load('./Game/R6E.png'), pygame.image.load('./Game/R7E.png'), pygame.image.load('./Game/R8E.png'), pygame.image.load('./Game/R9E.png'), pygame.image.load('./Game/R10E.png'), pygame.image.load('./Game/R11E.png')]
    walkLeft = [pygame.image.load('./Game/L1E.png'), pygame.image.load('./Game/L2E.png'), pygame.image.load('./Game/L3E.png'), pygame.image.load('./Game/L4E.png'), pygame.image.load('./Game/L5E.png'), pygame.image.load('./Game/L6E.png'), pygame.image.load('./Game/L7E.png'), pygame.image.load('./Game/L8E.png'), pygame.image.load('./Game/L9E.png'), pygame.image.load('./Game/L10E.png'), pygame.image.load('./Game/L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount //3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount //3], (self.x,self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
            


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        print("HI")


def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


man = player(200, 400, 64,64)
goblin = enemy(100, 405, 64, 64, 450)
shotLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if shotLoop > 0:
        shotLoop += 1
    if shotLoop > 3:
        shotLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shotLoop == 0:
        if man.left:
            facing = -1
        else:
            facing  = 1
        if len(bullets) <  3:
             bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))
        
        shotLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()


