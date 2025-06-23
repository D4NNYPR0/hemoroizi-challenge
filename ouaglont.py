import pygame as pag
import os

class Ou(pag.sprite.Sprite):
    def __init__(self, position, speed, screen_height):
        super().__init__()
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "smr eu grafici", "ou.png")
        self.image = pag.image.load(image_path)
        self.image = pag.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center = position)
        self.speed = speed
        self.screen_height = screen_height

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > self.screen_height + 15 or self.rect.y < 0:
            self.kill()