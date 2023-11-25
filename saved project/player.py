import pygame


class Player():
    def __init__(self, dimensions, color, health, delay, controls):
        self.x = dimensions[0]
        self.y = dimensions[1]
        self.wi = dimensions[2]
        self.he = dimensions[3]
        self.color = color
        self.rec = dimensions
        self.vel = 3
        self.health = health
        self.max_health = health
        self.delay = delay
        self.controls = controls

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rec)
        pygame.draw.line(win, (255, 0, 0), (self.x-25, self.y-30),
                         (self.x-25+50*(self.health/self.max_health), self.y-30), 3)
        if (self.health < self.max_health):
            pygame.draw.line(win, (255, 255, 255),
                             (self.x-25+50*(self.health/self.max_health)+1, self.y-30), (self.x+25, self.y-30), 3)

    def Update(self):
        self.rec = (self.x - self.wi/2, self.y - self.he/2, self.wi, self.he)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[self.controls[2]]:
            self.x -= self.vel
            if self.x < 0:
                self.x = 0
            elif self.x > 500:
                self.x = 500

        if keys[self.controls[3]]:
            self.x += self.vel
            if self.x < 0:
                self.x = 0
            elif self.x > 500:
                self.x = 500

        if keys[self.controls[0]]:
            self.y -= self.vel
            if self.y < 0:
                self.y = 0
            elif self.y > 500:
                self.y = 500

        if keys[self.controls[1]]:
            self.y += self.vel
            if self.y < 0:
                self.y = 0
            elif self.y > 500:
                self.y = 500
        self.Update()
