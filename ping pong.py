import pygame

pygame.init()

def game_loop():
    # COLOR
    white = (255, 255, 255)
    black = (0, 0, 0)

    # SCREEN
    dis = pygame.display.set_mode((600, 400))

    # FPS
    frame = 30
    clock = pygame.time.Clock()

    # player 1
    player1 = {
        "x": 75,
        "y": 200,
        "vectory": 0,
        "score": 0
    }

    # player 2
    player2 = {
        "x": 525,
        "y": 200,
        "vectory": 0,
        "score": 0
    }

    # ball
    ball = {
        "x": 300,
        "y": 200,
        "vector2": [-3, -1]
    }

    # Font
    font_style = pygame.font.SysFont(None, 25)

    def score_Player1():
        value = font_style.render("Player1: " + str(player1["score"]), True, white)
        dis.blit(value, [10, 0])

    def score_Player2():
        value = font_style.render("Player2: " + str(player2["score"]), True, white)
        dis.blit(value, [500, 0])

    game_over = False

    speed = 5

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:  # PLAYER1: MOVE
                if event.key == pygame.K_w:
                    player1["vectory"] = -speed
                elif event.key == pygame.K_s:
                    player1["vectory"] = speed
            else:
                player1["vectory"] = 0

            if event.type == pygame.KEYDOWN:  # PLAYER2: MOVE
                if event.key == pygame.K_UP:
                    player2["vectory"] = -speed
                elif event.key == pygame.K_DOWN:
                    player2["vectory"] = speed
            else:
                player2["vectory"] = 0

        if (ball["x"] > player1["x"] - 20 and ball["x"] < player1["x"] + 20) and (
                ball["y"] < player1["y"] + 70 and ball["y"] > player1["y"] - 20):  # PLAYER1: COLLISION
            ball["vector2"][0] *= -1.08

        elif (ball["x"] < player2["x"] + 20 and ball["x"] > player2["x"] - 10) and (
                ball["y"] < player2["y"] + 70 and ball["y"] > player2["y"] - 20):  # PLAYER2: COLLISION
            ball["vector2"][0] *= -1.08

        # BALL COLLISION
        if ball["y"] <= 0 or ball["y"] >= 390:
            ball["vector2"][1] *= -1

        elif ball["x"] <= 0:
            player2["score"] += 1

            ball["x"] = 300
            ball["y"] = 200
            ball["vector2"][1] = -1
            ball["vector2"][0] = -3

        elif ball["x"] >= 590:
            player1["score"] += 1

            ball["x"] = 300
            ball["y"] = 200
            ball["vector2"][1] = 1
            ball["vector2"][0] = 3


        ball["x"] += ball["vector2"][0]
        ball["y"] += ball["vector2"][1]
        player1["y"] += player1["vectory"]
        player2["y"] += player2["vectory"]

        dis.fill(black)
        score_Player1()
        score_Player2()

        pygame.draw.rect(dis, white, [player1["x"], player1["y"], 20, 70])
        pygame.draw.rect(dis, white, [player2["x"], player2["y"], 20, 70])
        pygame.draw.rect(dis, white, [ball["x"], ball["y"], 10, 10])
        pygame.display.update()
        clock.tick(frame)
    pygame.quit()
    quit()

game_loop()






