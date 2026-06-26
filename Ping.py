from pygame import *
width = 700
hight = 500
window = display.set_mode((width,hight))
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
platform_1 = Player('racket.png',620,50,1,30,150)
platform_2 = Player('racket.png',50,50,1,30,150)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((22, 224, 117))        
    platform_1.reset()
    platform_2.reset()
    platform_1.update_r()
    platform_2.update_l()
    display.update()