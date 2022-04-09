import pygame
import sys

sc = pygame.display.set_mode((900, 800))

PlY = 333
PlX = 133
BotX = 250
BotY = 350
BotXX = 250
BotYY = 416
BotXXX = 546
BotYYY = 383
BotXXXX = 546
BotYYYY = 449

BotWord1 = "lf"
BotWord2 = "lk"

Game = True

while Game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        PlY -= 1
    if keys[pygame.K_s]:
        PlY += 1
    if keys[pygame.K_d]:
        PlX += 1
    if keys[pygame.K_a]:
        PlX -= 1

    if BotX == 546:
        BotWord1 = "pf"
    if BotWord1 == "pf":
        BotX -= 2
        BotXX -= 2
    if BotX == 250:
        BotWord1 = "lf"
    if BotWord1 == "lf":
        BotX += 2
        BotXX += 2

    if BotXXX == 250:
        BotWord2 = "pk"
    if BotWord2 == "pk":
        BotXXX += 2
        BotXXXX += 2
    if BotXXX == 546:
        BotWord2 = "lk"
    if BotWord2 == "lk":
        BotXXX -= 2
        BotXXXX -= 2

    sc.fill((148, 185, 230))

    pygame.draw.rect(sc, (164, 247, 169), (100, 300, 100, 200), )
    pygame.draw.rect(sc, (255, 255, 255), (200, 467, 66, 33), )
    pygame.draw.rect(sc, (255, 255, 255), (233, 333, 330, 134), )
    pygame.draw.rect(sc, (255, 255, 255), (530, 300, 66, 33), )
    pygame.draw.rect(sc, (164, 247, 169), (595, 300, 100, 200), )

    pygame.draw.rect(sc, (200, 25, 25), (PlX, PlY, 10, 10),)
    pygame.draw.rect(sc, (0, 0, 0), (PlX, PlY, 10, 10), 2)
    pygame.draw.circle(sc, (19, 6, 206), (BotX, BotY), 12)
    pygame.draw.circle(sc, (19, 6, 206), (BotXX, BotYY), 12)
    pygame.draw.circle(sc, (19, 6, 206), (BotXXX, BotYYY), 12)
    pygame.draw.circle(sc, (19, 6, 206), (BotXXXX, BotYYYY), 12)

    wallColl1 = pygame.Rect((50, 300), (50,200))
    wallColl2 = pygame.Rect((100, 500), (166, 50))
    wallColl3 = pygame.Rect((268, 467), (330, 33))
    wallColl3t = pygame.Rect((266, 467), (2, 33))
    wallColl4 = pygame.Rect((565, 333), (29, 132))
    wallColl4t = pygame.Rect((563, 333), (2, 132))
    wallColl4tt = pygame.Rect((594, 333), (2, 132))
    wallColl5 = pygame.Rect((464, 267), (1000, 33))
    wallColl6 = pygame.Rect((202, 300), (326, 33))
    wallColl6t = pygame.Rect((528, 300), (2, 33))
    wallColl7 = pygame.Rect((200, 300), (2, 165))
    wallColl7t = pygame.Rect((200, 465), (33, 2))
    wallColl7tt = pygame.Rect((231, 333), (2, 132))
    wallColl8 = pygame.Rect((100, 267), (100, 33))
    win = pygame.Rect((595, 300), (100, 200))

    PlColl = pygame.Rect((PlX, PlY), (10, 10))
    BotColl = pygame.Rect(((BotX - 12), (BotY - 12)), (24,24))
    BotColl1 = pygame.Rect(((BotXX - 12), (BotYY - 12)), (24,24))
    BotColl2 = pygame.Rect(((BotXXX - 12), (BotYYY - 12)), (24,24))
    BotColl3 = pygame.Rect(((BotXXXX - 12), (BotYYYY - 12)), (24,24))

    Coll1 = PlColl.colliderect(wallColl1)
    Coll2 = PlColl.colliderect(wallColl2)
    Coll3 = PlColl.colliderect(wallColl3)
    Coll3t = PlColl.colliderect(wallColl3t)
    Coll4 = PlColl.colliderect(wallColl4)
    Coll4t = PlColl.colliderect(wallColl4t)
    Coll4tt = PlColl.colliderect(wallColl4tt)
    Coll5 = PlColl.colliderect(wallColl5)
    Coll6 = PlColl.colliderect(wallColl6)
    Coll6t = PlColl.colliderect(wallColl6t)
    Coll7 = PlColl.colliderect(wallColl7)
    Coll7t = PlColl.colliderect(wallColl7t)
    Coll7tt = PlColl.colliderect(wallColl7tt)
    Coll8 = PlColl.colliderect(wallColl8)
    CollWin = PlColl.colliderect(win)
    
    CollRip = PlColl.colliderect(BotColl)
    CollRip1 = PlColl.colliderect(BotColl1)
    CollRip2 = PlColl.colliderect(BotColl2)
    CollRip3 = PlColl.colliderect(BotColl3)

    if Coll1 == 1:
        PlX += 1
    if Coll2 == 1:
        PlY -= 1
    if Coll3 == 1:
        PlY -= 1
    if Coll3t == 1:
        PlX -= 1
    if Coll4 == 1:
        PlY -= 1
    if Coll4t == 1:
        PlX -= 1
    if Coll4tt == 1:
        PlX += 1
    if Coll5 == 1:
        PlY += 1
    if Coll6 == 1:
        PlY += 1
    if Coll6t == 1:
        PlX += 1
    if Coll7 == 1:
        PlX -= 1
    if Coll7t == 1:
        PlY += 1
    if Coll7tt == 1:
        PlX += 1
    if Coll8 == 1:
        PlY += 1
    
    if CollWin == 1:
        Game = False 
        
    if CollRip == 1:
        PlY = 333
        PlX = 133
    if CollRip1 == 1:
        PlY = 333
        PlX = 133
    if CollRip2 == 1:
        PlY = 333
        PlX = 133
    if CollRip3 == 1:
        PlY = 333
        PlX = 133   
        
    pygame.display.update()
    pygame.time.delay(4)