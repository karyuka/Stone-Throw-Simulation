import pygame as pg
import math
import random
pg.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Kast av Stein")
font = pg.font.SysFont("monospace", 15)


BLUE = (0, 153, 255)
BROWN = (102, 51, 0)
BLACK = (0, 0 ,0)

GAMA = 6.67428e-11
SCALE = 250    # 1 m = 100 px
dt = 0.04

DATABREAK = pg.USEREVENT + 1  #FOr the name of the planet in the future


class Stone:

    stones = []

    def __init__(self, vinkel, fart):
        self.r = 5
        self.x = 0
        self.y = HEIGHT - 120
        self.vinkel = math.radians(vinkel)
        self.ay = -9.81
        self.v = fart
        self.vx = self.v * math.cos(self.vinkel)
        self.vy = self.v * math.sin(self.vinkel)
        self.path = []
        self.xm = 0
        self.ym = HEIGHT
        self.name = f"stone {len(self.stones) + 1}"
        self.stones.append(self)
        self.topp = None
        self.fall = None
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    def kast(self, stones):
        pg.draw.circle(WIN, GREY, (self.x, self.y), 5)
        if len(self.path) > 2:
            pg.draw.lines(WIN, GREY, False, self.path, 2)

        self.path.append((self.x, self.y))

        self.vy += self.ay * dt

        self.x += self.vx * dt
        self.y -= self.vy * dt 


    def mark_topp(self):
        if self.topp is not None:
            TOPP = font.render(f"Topp:{round(self.topp[0], 2), round(self.topp[1], 2)}", 1, self.color)
            WIN.blit(TOPP, (self.topp[0] - 30, self.topp[1] - 30))


    def mark_fall(self):
        if self.fall is not None:
            FALL = font.render(f"Fall:{round(self.fall[0], 2), round(self.fall[1], 2)}", 1, self.color)
            WIN.blit(FALL, (self.fall[0] - 30, self.fall[1] - 30))


    def kast2(self):
        pg.draw.circle(WIN, self.color, (self.x, self.y), self.r)
        if len(self.path) > 2:
            pg.draw.lines(WIN, self.color, False, self.path, 2)

        self.path.append((self.x, self.y))

        stone_name = font.render(f"{self.name}", 1, self.color)
        WIN.blit(stone_name, (self.x, self.y - 30))


        self.vy += self.ay * dt
        self.x += self.vx * dt
        self.y -= self.vy * dt

        if int(self.vy) == 0 and self.topp is None:
            self.topp = (self.x ,self.y)


        if int(self.y) == HEIGHT - 100 - self.r + 1:
            self.vy = 0
            self.ay = 0
            self.vx = 0
            self.fall = (self.x, self.y)

        # if len(self.path) > 100 and round(self.y, 1) == 500:    # Cheick if the stone did fall, self.ay og self.v må bli lik null for at den skal stoppe å bevege seg
        #     for i in range(0, len(self.stones)):
        #         if self.stones[i].name == self.name:
        #             self.stones.pop(i)
        #             break
        #         FALL = font.render(f"({self.x}, {self.y})", 1, BLACK)
        #         WIN.blit(FALL, (self.x, self.y))



    def kast3(self):
        pg.draw.circle(WIN, GREY, (self.x, self.y), 5)


        self.vy += self.ay * dt
        self.xm += self.vx * dt
        self.ym += self.vy * dt

        self.x += self.xm / SCALE
        self.y += self.ym / SCALE



def draw_window():
    GROUND = pg.Rect(0, HEIGHT - 100, WIDTH, 100)
    pg.draw.rect(WIN, BROWN, GROUND)
    pg.display.update()






stone1 = Stone(50, 40)
stone2 = Stone(60, 15)
stone3 = Stone(45, 20)
stone4 = Stone(40, 45)
stone5 = Stone(16, 70)
stone6 = Stone(25, 100)
stone7 = Stone(35, 120)



def main():
    clock = pg.time.Clock()

    stones = Stone.stones
    fot = font.render("gsdgds", 1, BLACK)

    run = True
    while run:
        clock.tick(60)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        WIN.fill(BLUE)
        for stone in stones:
            stone.kast2()
            stone.mark_topp()
            stone.mark_fall()

        draw_window()
    pg.quit()


main()