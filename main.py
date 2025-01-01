import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.init()
    game_loop(screen)
  

    
def game_loop(screen):
    while True:
    
    # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop by returning from the function

        # Game logic and rendering
        screen.fill("black")  # Fill the screen with black
        pygame.display.flip() # Update the display
   
if __name__ == "__main__":
    main()