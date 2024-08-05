def inGameMainMenu():
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   GAMES  \033[1;32;40m  ║")
    print("║                     ║")
    print("║ 1-Snake Game        ║")
    print("║ 2-Flappy Bird       ║")
    print("║ 3-NONE              ║")
    print("║ 4-NONE              ║")
    print("║                     ║")
    print("║ What is your choose?║")
    print("╚═════════════════════╝")
    choose = int(input("What is your choose?"))
    import SnakeGame
    import FlappyBird
    if choose == 1:
        SnakeGame.inSnakeGame()
    elif choose == 2:
        FlappyBird.inFlappyBird()
