import pygame as pag
import os
from ouaglont import Ou

class Gainaplayer(pag.sprite.Sprite):
    def __init__(self, WIDTH=1000, HEIGHT=1000):
        super().__init__()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "smr eu grafici", "gaina_player.png")
        self.image = pag.image.load(image_path)
        
        self.image = pag.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(midbottom=(self.WIDTH // 2, self.HEIGHT))
        self.speed = 9
        self.oul = pag.sprite.Group()
        self.ou_pregatit = True
        self.timp_ou = 0
        self.delay_ou = 300

    def movement(self):
        keys = pag.key.get_pressed()
        
        if keys[pag.K_d]:
            self.rect.x += self.speed
        
        if keys[pag.K_a]:
            self.rect.x -= self.speed  
        
        if keys[pag.K_SPACE] and self.ou_pregatit:
            self.ou_pregatit = False
            ou = Ou(self.rect.center, 10, self.HEIGHT)
            self.oul.add(ou)
            self.timp_ou = pag.time.get_ticks()
            
    def update(self):
        self.movement()
        self.limitare()
        self.oul.update()
        self.incarcare_oul()
        
    def limitare(self):
        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
    def incarcare_oul(self):
        if not self.ou_pregatit:
            current_time = pag.time.get_ticks()
            if current_time - self.timp_ou >= self.delay_ou:
                self.ou_pregatit = True
                self.timp_ou = current_time