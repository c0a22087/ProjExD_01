import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    tmr = 0
    #こうかとん画像読み込み
    original_img = pg.image.load("ex01/fig/3.png")
    #動きこうかとん
    kouka_hanten_img = pg.transform.flip(original_img,True,False)
    kouka_naname_img = pg.transform.rotozoom(kouka_hanten_img,10,1.0)

    kouka_img=[kouka_hanten_img,kouka_naname_img]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(kouka_img[tmr%2],[300,200])
        pg.display.update()
        tmr += 1
        if tmr==1600:
            tmr=0        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()