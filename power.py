import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Car dimensions
CAR_WIDTH = 50
CAR_HEIGHT = 100

# Load car images
car_images = [pygame.image.load(os.path.join('images', 'carmmm-2.png')), pygame.image.load(os.path.join('images', 'carmmm-2.png'))]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")

clock = pygame.time.Clock()

# Car class
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, image_index):
        super().__init__()
        self.image = car_images[image_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -CAR_HEIGHT

# Player car class
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = car_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0

    def update(self):
        self.rect.x += self.speed

# Function to draw road
def draw_road():
    road_width = 200
    road_y = (SCREEN_HEIGHT - road_width) // 2
    pygame.draw.rect(screen, WHITE, (0, road_y, SCREEN_WIDTH, road_width))

# Function to handle events
def handle_events(player_car):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_car.speed = -5
            elif event.key == pygame.K_RIGHT:
                player_car.speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_car.speed = 0

# Main function
def main():
    all_sprites = pygame.sprite.Group()
    cars = pygame.sprite.Group()

    # Create player car
    player_car = PlayerCar(SCREEN_WIDTH // 2 - CAR_WIDTH // 2, SCREEN_HEIGHT - CAR_HEIGHT - 20)
    all_sprites.add(player_car)

    # Create random cars
    for i in range(3):
        car = Car(random.randint(0, SCREEN_WIDTH - CAR_WIDTH), random.randint(-SCREEN_HEIGHT, 0), random.randint(0, 1))
        all_sprites.add(car)
        cars.add(car)

    running = True
    while running:
        screen.fill(BLACK)
        draw_road()

        handle_events(player_car)

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
