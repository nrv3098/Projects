def main():
    import pygame
    from random import randint

    black = (0,0,0)
    white = (255,255,255)
    green = (0,255,0)
    red = (255,0,0)
    #blue = (0,0,255)

    birdimg = pygame.image.load('download.png')
    background = pygame.image.load('background.png')
    pygame.init()

    size = 700,500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Flappy Bird")

    done = False
    clock = pygame.time.Clock()

    def ball(x,y):
        screen.blit(birdimg,(x,y))
        


    def gameover():
        font = pygame.font.SysFont(None, 75)
        text = font.render("Game over", True, black)
        screen.blit(text, [150, 250])
        pygame.time.delay(3000)
        screen.blit(background,[0,0])
        text1 = font.render("Play Again?", True, red)
        screen.blit(text1, [150, 250])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    main()
        

    def obstacle(xloc, yloc, xsize, ysize):
        pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])
        pygame.draw.rect(screen, green, [xloc, int(yloc+ysize+space), xsize, ysize+500])


    def Score(score):
        font = pygame.font.SysFont(None, 75)
        text = font.render("Score: "+str(score), True, black)
        screen.blit(text, [0,0])

    x = 350
    y = 250
    x_speed = 0
    y_speed = 0
    ground = 477
    ciel = 20
    xloc = 700
    yloc = 0
    xsize = 70
    ysize = randint(0,350)
    space = 150
    obspeed = 2.5
    score = 0


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_speed = -10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_speed = 5

        
        screen.blit(background,[0,0])
        #screen.fill(blue)
        obstacle(xloc, yloc, xsize, ysize)
        ball(x,y)
        Score(score)
        
        y += y_speed
        xloc -= obspeed
        
        if y > ground or y < ciel:
            gameover()
            y_speed = 0
            obspeed = 0

        if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
            gameover()
            obspeed = 0
            y_speed = 0

        if x+20 > xloc and y+20 > ysize+space and x-15 < xsize+xloc:
            gameover()
            obspeed = 0
            y_speed = 0

        if xloc < -80:
            xloc = 700
            ysize = randint(0,350)

        if x > xloc and x < xloc+3:
            score = (score + 1)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
main()
