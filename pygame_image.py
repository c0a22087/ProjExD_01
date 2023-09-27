import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("./fig/pg_bg.jpg")
    gb_img = pg.transform.flip(bg_img,True,False)
    tmr = 0
    #こうかとん画像読み込み
    original_img = pg.image.load("./fig/3.png")
    #動きこうかとん
    kouka_hanten_img = pg.transform.flip(original_img,True,False)
    kouka_2_img = pg.transform.rotozoom(kouka_hanten_img,5,1.0)
    kouka_3_img = pg.transform.rotozoom(kouka_hanten_img,10,1.0)

    kouka_img=[kouka_hanten_img,kouka_2_img,kouka_3_img,kouka_2_img]
    x=0
    x2=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        #背景
        if x==-2400:
            x=800
        screen.blit(bg_img, [x, 0])

        if x2==-3200:
            x2==0
        screen.blit(gb_img,[x2+1600,0])
        #こうかとん
        screen.blit(kouka_img[tmr%4],[300,200])
        pg.display.update()
        x -= 1
        x2-= 1
        tmr += 1     
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()