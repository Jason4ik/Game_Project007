import pygame

# Initialize Pygame
pygame.init()

# Set the size of the window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("My Top-View Game")

pygame.mixer.music.load("./Riders-on-the-Storm.mp3")
pygame.mixer.music.play()


while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        else:
            pygame.display.update()