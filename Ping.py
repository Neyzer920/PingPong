from pygame import *
width = 1720
hight = 900
font.init()
font1 = font.Font(None,35)
lose1 = font1.render('PLAYER 1 LOSE!',True,(180,0,0))
lose2 = font1.render('PLAYER 2 LOSE!',True,(180,0,0))
window = display.set_mode((width,hight))
speed_x = 3
speed_y = 3
game = True
class Gamesprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_size_x,player_size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_size_x,player_size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Gamesprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < hight - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < hight - 80:
            self.rect.y += self.speed
platform_1 = Player('racket.png',1640,50,3,30,150)
platform_2 = Player('racket.png',50,50,3,30,150)
ball = Player('tenis_ball.png',300,50,1,50,50)
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.fill((22, 224, 117))        
        platform_1.reset()
        platform_2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > hight - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(platform_1,ball) or sprite.collide_rect(platform_2,ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
        if ball.rect.x > width:
            finish = True
            window.blit(lose2,(200,200))
        platform_1.update_r()
        platform_2.update_l()
        display.update()