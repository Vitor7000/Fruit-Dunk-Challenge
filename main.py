import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fruit Dunk Challenge")

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 36)

# Load images
try:
    player_img = pygame.image.load("assets/player.png").convert_alpha()
    fruit_img = pygame.image.load("assets/banana.png").convert_alpha()
    obstacle_img = pygame.image.load("assets/fire.png").convert_alpha()
    images_loaded = True
except pygame.error as e:
    print("Unable to load images:", e)
    images_loaded = False

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if images_loaded:
            self.image = pygame.transform.scale(player_img, (50, 50))
        else:
            self.image = pygame.Surface([50, 50])
            self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0
        self.speed_y = 0
        self.gravity = 0.8
        self.super_power_active = False
        self.super_power_timer = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -8
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 8
        self.rect.x += self.speed_x
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.speed_y += self.gravity
        self.rect.y += self.speed_y

        if self.rect.bottom > SCREEN_HEIGHT -10:
            self.rect.bottom = SCREEN_HEIGHT -10
            self.speed_y = 0


        if self.super_power_active:
            self.super_power_timer -= 1
            if self.super_power_timer <= 0:
                self.super_power_active = False

    def jump(self):
        if self.rect.bottom >= SCREEN_HEIGHT -10:
            self.speed_y = -15

    def activate_super_power(self):
        self.super_power_active = True
        self.super_power_timer = 300 # 5 seconds at 60 FPS

# Fruit
class Fruit(pygame.sprite.Sprite):
    def __init__(self, speed_multiplier):
        super().__init__()
        if images_loaded:
            self.image = pygame.transform.scale(fruit_img, (30, 30))
        else:
            self.image = pygame.Surface([30, 30])
            self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 4) * speed_multiplier

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 4) * speed_multiplier

# Obstacle
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, speed_multiplier):
        super().__init__()
        if images_loaded:
            self.image = pygame.transform.scale(obstacle_img, (30, 30))
        else:
            self.image = pygame.Surface([30, 30])
            self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 4) * speed_multiplier

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 4) * speed_multiplier


all_sprites = pygame.sprite.Group()
fruits = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

speed_multiplier = 1.0

for i in range(8):
    fruit = Fruit(speed_multiplier)
    all_sprites.add(fruit)
    fruits.add(fruit)

for i in range(4):
    obstacle = Obstacle(speed_multiplier)
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

score = 0
fruit_collected_count = 0

# Game loop
running = True
game_over = False
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    if not game_over:
        all_sprites.update()

        # Check for collisions with fruits
        fruit_hits = pygame.sprite.spritecollide(player, fruits, True)
        for hit in fruit_hits:
            score += 1
            fruit_collected_count += 1
            if fruit_collected_count % 20 == 0:
                player.activate_super_power()

            if score % 10 == 0:
                speed_multiplier += 0.1

            fruit = Fruit(speed_multiplier)
            all_sprites.add(fruit)
            fruits.add(fruit)

        # Check for collisions with obstacles
        if not player.super_power_active:
            obstacle_hits = pygame.sprite.spritecollide(player, obstacles, False)
            if obstacle_hits:
                game_over = True

    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Display controls
    controls_text = font.render("Left/Right arrows to move, Space to jump", True, WHITE)
    screen.blit(controls_text, (10, SCREEN_HEIGHT - 40))

    if player.super_power_active:
        super_power_text = font.render("SUPER POWER!", True, YELLOW)
        screen.blit(super_power_text, (SCREEN_WIDTH // 2 - 100, 10))


    if game_over:
        game_over_text = font.render("GAME OVER", True, WHITE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))

    pygame.display.flip()

pygame.quit()
