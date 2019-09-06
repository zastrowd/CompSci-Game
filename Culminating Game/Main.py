import  pygame
from    math       import *
from    random     import *
from    settings   import *
from    classes    import *    
from    functions  import *
from    Maze       import generate
pygame.init()

screen = pygame.display.set_mode(RESOLUTION, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
clock = pygame.time.Clock()

mapList = [ [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1] ,
            [1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1] ,
            [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1] ,
            [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1] ,
            [1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1] ,
            [1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1] ,
            [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1] ,
            [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1] ,
            [1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1] ,
            [1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1] ,
            [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1] ,
            [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1] ,
            [1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1] ,
            [1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]

#mapList  = [[1 if x == 0 or y == 0 or x == 24 or y == 24 else 0 for x in range(25)] for y in range(25)]
mapList = generate(151,151)

tileMapList = mapList

mapDisplay   = pygame.Surface((len(mapList) * TILE_WIDTH, len(mapList[0]) * TILE_HEIGHT))

#             Gun([Angles for each bullet], gun name, rarity level(0-4), 
#                 speed, range, bounces, atk speed, deviation, damage, radius, slow, shot type)
spreadFire  = Gun([-10, 0, 10], "Spread Fire", 0,
                  0.4,  100,    2,  10, 0,  15,     0.2,    1,      "semi")
superSpread = Gun([i / 2 for i in range(-31, 30)], "Fan Shot", 0,
                  0.4,  80,     0,  12, 0,  2,      0.1,    1,      "semi")
burst       = Gun([i / 10 for i in range(-26,25)], "Burst Fire", 0,
                  0.5,  80,     0,  15, 0,  1,      0.2,    1,      "semi")
tripleBurst = Gun([i / 2 for i in range(-46, -35)] + [i / 2 for i in range(-9, 8)] + [i / 2 for i in range(34, 45)], "Triple Spread", 0,
                  0.3,  80,     0,  20, 0,  3,      0.1,    1,      "semi")
minigun     = Gun([0], "Minigun", 0,
                  0.4,  80,     1,  2,  3,  8,      0.1,    0.4,    "auto")
bouncey     = Gun([0], "Bounce Shot", 0,
                  0.3,  600,    12, 12, 2,  25,     0.4,    1,      "semi")
sniper      = Gun([0], "Sniper", 0,
                  1.5,  800,    0,  40, 0,  75,     0.1,    1,      "semi")
shotgun     = Gun([-3, -2, -1, -1, 0, 1, 1, 2, 3], "Shotgun", 0,
                  0.4,  20,     0,  60, 2,  15,     0.1,    1,      "semi")
lasergun    = Gun([0], "Laser Gun", 0,
                  0.25, 25,     0,  1,  0,  3,      0.2,    0.3,    "auto")
plasma      = Gun([i for i in range(-5, 5)], "Plasma Fire", 0,
                  0.25, 25,     0,  0,  0,  1,      0.3,    0,      "auto")

legendary   = Gun([0], "am monkey", 4,
                   0.4, 100,    2,  2.5, 2, 10,     0.15,   0.3,    "auto")

#players = [Player(1.2, 1.2, 0, 300), Player(9.5, 9.5, 1, 300), Player(11, 9.5, 2, 300), Player(12.5, 9.5, 3, 300), Player(14, 9.5, 4, 300), Player(15.5, 9.5, 5, 300)]
players = [Player(1.2, 1.2, 0, 300), Player(9.5, 9.5, 1, 300), Player(14, 9.5, 1, 300), Player(15.5, 9.5, 1, 300)]
currentCamera = Camera(0, 0)
    
def draw(grid, players, bullets, seeItems, guns, updated):
    global mapDisplay
    for i, player in enumerate(players):
        picture = player.screen
        if updated:
            mapDisplay = pygame.Surface((len(grid) * TILE_WIDTH, len(grid[0]) * TILE_HEIGHT))
            mapDisplay.fill(BLACK)
            for column in range(len(grid)):
                for row in range(len(grid[column])):
                    if grid[row][column] == 1:
                        colour = GREY
                    elif grid[row][column] == 0:
                        colour = BROWN
               
                    pygame.draw.rect(mapDisplay,  colour, (TILE_WIDTH * column, TILE_HEIGHT * row, TILE_WIDTH, TILE_HEIGHT))

        screen.fill(BLACK)
        screen.blit(mapDisplay, (-currentCamera.x, -currentCamera.y))

        for p in players:
            if p.worldX == player.worldX:
                pygame.draw.rect(screen,    WHITE, ((p.x * TILE_WIDTH) - currentCamera.x,
                                                           p.y * TILE_HEIGHT - currentCamera.y,
                                                           p.w * TILE_WIDTH, p.h * TILE_HEIGHT))
                pygame.draw.rect(screen,      RED, ((p.x + (p.w / 2)) * TILE_WIDTH - (p.w * TILE_WIDTH) - currentCamera.x,
                                                           p.y * TILE_HEIGHT + TILE_HEIGHT - currentCamera.y,
                                                           (p.w * TILE_WIDTH) + (p.w * TILE_WIDTH), 5))        
                pygame.draw.rect(screen,    GREEN, ((p.x + (p.w / 2)) * TILE_WIDTH - (p.w * TILE_WIDTH) - currentCamera.x,
                                                           p.y * TILE_HEIGHT + TILE_HEIGHT - currentCamera.y,
                                                           max(1, p.health * ((p.w * TILE_WIDTH + (p.w * TILE_WIDTH)) / p.maxHealth)), 5))

        for bullet in bullets:
            pygame.draw.circle(screen,  WHITE, (round(bullet.x *  TILE_WIDTH) - currentCamera.x,
                                                round(bullet.y * TILE_HEIGHT) - currentCamera.y),
                               round(bullet.r * TILE_WIDTH))

##        if seeItems:
##            for p in players:
##                screen.blit(p.gun.window, ((p.x * TILE_WIDTH) - currentCamera.x, (p.y * TILE_HEIGHT) - currentCamera.y))
##
##            rects = []
##            for g in guns:
##                x, y = g.pos
##                if g.state == 1:
##                    rect = pygame.Rect((x * TILE_WIDTH) - currentCamera.x, (y * TILE_HEIGHT) - currentCamera.y, 201, 120)
##                    for r in rects:
##                        if r.colliderect(rect): rect.x = r.x + 201; rect.y = r.y
##                    rects.append(rect)                
##                    screen.blit(g.window, (rect[0], rect[1]))
        
    pygame.display.update()

def startGame(mapList, tileMapList):
    screens = []
    for i in range(4):
        screens.append(Screen((i % 2) * HALF_RES[0], (i % 2) * HALF_RES[1], HALF_RES[0], HALF_RES[1]))

    for i, player in enumerate(players):
        player.screen = screens[i]

    tileMapList = initializeRooms(mapList)
    
def main():
    global TILE_WIDTH, TILE_HEIGHT
    player      = players[0]
    seeItems    = False
    xChange = 0; yChange = 0
    bullets     = []
    guns        = [minigun, spreadFire]
    #guns[1].pos = (10, 10)
    update      = False
    for p in players:
        p.gun   = minigun
    player.gun  = legendary
    player.computer = False
    firing = False
    draw(mapList, players, bullets, seeItems, guns, True)
    while True:
        draw(mapList, players, bullets, seeItems, guns, update)
        update = False
        removeQueue = []
        pygame.display.update()
        clock.tick(FPS_CAP)
        g = player.gun
        if currentCamera.locked:
            currentCamera.x = int((player.x * TILE_WIDTH)  - (RESOLUTION[0] / 2))
            currentCamera.y = int((player.y * TILE_HEIGHT) - (RESOLUTION[1] / 2))
        pygame.display.set_caption("{} FPS".format(int(clock.get_fps())))
        for p in players:
            if p.shotCooldown < p.gun.atkSpeed: p.shotCooldown += 1
        for event in pygame.event.get():
            if event.type    == pygame.QUIT: pygame.quit(); return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    for g in guns:
                        if g.state == 1:
                            if (int(player.x),int(player.y)) == (int(g.pos[0]),int(g.pos[1])):
                                playerGun = player.gun
                                player.gun = g
                                player.gun.state = 0
                                playerGun.state = 1
                                playerGun.pos = g.pos
                                guns.remove(g)

                                guns.append(playerGun)
                                break

                elif event.key == pygame.K_z:
                    if seeItems == True: seeItems = False
                    else: seeItems = True
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if g.fireType == "auto":    firing = True
                    else:
                        firing = False
                        pos = pygame.mouse.get_pos()
                        clickAngle = getAngle(((player.x + (player.w / 2)) * TILE_WIDTH),
                                              ((player.y + (player.h / 2)) * TILE_HEIGHT),
                                              pos[0] + currentCamera.x,
                                              pos[1] + currentCamera.y)
                        shoot(bullets, player, currentCamera, clickAngle)

                elif event.button == 4:
                    TILE_WIDTH  += 1
                    TILE_HEIGHT += 1
                    update = True
                
                elif event.button == 5 and TILE_WIDTH > 2 and TILE_HEIGHT > 2:
                    TILE_WIDTH  -= 1
                    TILE_HEIGHT -= 1
                    update = True
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    firing = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if not mapList[int((player.y + (player.h / 2)) - (player.h / 2))][int(player.x + (player.w / 2))]: player.y -= player.ms * player.slow

        if keys[pygame.K_s]:
            if not mapList[int((player.y + (player.h / 2)) + (player.h / 2))][int(player.x + (player.w / 2))]: player.y += player.ms * player.slow

        if keys[pygame.K_a]:
            if not mapList[int(player.y + (player.h / 2))][int((player.x + (player.w / 2)) - (player.w / 2))]: player.x -= player.ms * player.slow

        if keys[pygame.K_d]:
            if not mapList[int(player.y + (player.h / 2))][int((player.x + (player.w / 2)) + (player.w / 2))]: player.x += player.ms * player.slow
        
        if keys[pygame.K_LEFT]:         currentCamera.x -= 50
        if keys[pygame.K_RIGHT]:        currentCamera.x += 50
        if keys[pygame.K_UP]:           currentCamera.y -= 50
        if keys[pygame.K_DOWN]:         currentCamera.y += 50

        if keys[pygame.K_1]:            player.gun  = spreadFire
        if keys[pygame.K_2]:            player.gun  = minigun
        if keys[pygame.K_3]:            player.gun  = sniper
        if keys[pygame.K_4]:            player.gun  = bouncey
        if keys[pygame.K_5]:            player.gun  = shotgun
        if keys[pygame.K_6]:            player.gun  = lasergun
        if keys[pygame.K_7]:            player.gun  = superSpread
        if keys[pygame.K_8]:            player.gun  = burst
        if keys[pygame.K_9]:            player.gun  = tripleBurst
        if keys[pygame.K_0]:            player.gun  = plasma

        if keys[pygame.K_t]:
            for p in players:           p.health    = p.maxHealth
        if keys[pygame.K_y]:
            for p in players:           p.health        = 1
        if keys[pygame.K_k]:            player.health   = 1

        if keys[pygame.K_p]:
            if currentCamera.locked:    currentCamera.locked = False
            else:                       currentCamera.locked = True

        updateBullets(mapList, bullets, players)
        #updateMines(mines, players)
        if firing and g.fireType == "auto":
            pos = pygame.mouse.get_pos()
            clickAngle = getAngle(((player.x + (player.w / 2)) * TILE_WIDTH), ((player.y + (player.h / 2)) * TILE_HEIGHT), pos[0] + currentCamera.x, pos[1] + currentCamera.y)
            shoot(bullets, player, currentCamera, clickAngle)
            player.slow = g.slow
        else: player.slow = 1
        AI(players, mapList, currentCamera, bullets)

if __name__ == "__main__": main()#startGame(); main()
