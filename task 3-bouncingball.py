
import pygame

pygame.init()
(width, height) = (500, 500)
x = 225
y = 474
p = 250
q = 250
spd = 20
dirx = 1
diry = 1
bspdx = 8
bspdy = 8
score = 0
count = 0
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong.exe")
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("PONG", True, (0, 128, 0))
textRect = text.get_rect()
textRect.center = (500//2, 50)

win.blit(text, textRect)

run1 = True
run = True
while run:
    pygame.time.delay(120)

    #paddle movement
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0:
         x -= spd 
         
    if keys[pygame.K_RIGHT] and x < 450:
         x += spd
    win.fill((0, 0, 0))

    ball = pygame.draw.rect(win, (255, 255, 255), (p, q, 5, 5))
    paddle = pygame.draw.rect(win, (255, 50, 0), (x, y, 50, 2))

    #ball movent
    
    p += bspdx * dirx
    q += bspdy * diry

    if p > 495:
        dirx = -1
    if p < 0:
        dirx = 1
    if q > 500:
        p = 250
        q = 250
        count += 1

        
    if q < 300:
        diry = 1
    if ball.colliderect(paddle):
        diry = -1
        score = score + 1

    if count == 3:
        run = False
        
        


    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render("PONG", True, (255,105,180))
    textRect = text.get_rect()
    textRect.center = (500//2, 50)
    win.blit(text, textRect)

    text2 = font.render(str(score), True, (0,255,255))
    text2Rect = text2.get_rect()
    text2Rect.center = (250,100)
    win.blit(text2, text2Rect)
    pygame.display.update()



pygame.quit()







    
   

