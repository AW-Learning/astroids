import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT 
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT /2
    player = Player(x,y)
    clock = pygame.time.Clock()

    while True:
        log_state()
        dt_ms = clock.tick(60)
        dt = dt_ms / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
