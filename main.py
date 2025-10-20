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

# Game variables
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 60
PLAYER_SPEED = 10
PLAYER_JUMP_HEIGHT = 20
FRUIT_WIDTH = 30
FRUIT_HEIGHT = 30
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
GRAVITY = 1

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Fruit Dunk Challenge')

# Clock
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH - PLAYER_WIDTH) // 2
        self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT
        self.vel_y = 0
        self.is_jumping = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        if not self.is_jumping:
            if keys[pygame.K_SPACE]:
                self.is_jumping = True
                self.vel_y = -PLAYER_JUMP_HEIGHT
        else:
            self.vel_y += GRAVITY
            self.rect.y += self.vel_y
            if self.rect.y >= SCREEN_HEIGHT - PLAYER_HEIGHT:
                self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT
                self.is_jumping = False
                self.vel_y = 0

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Fruit class
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([FRUIT_WIDTH, FRUIT_HEIGHT])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - FRUIT_WIDTH)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - FRUIT_WIDTH)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([OBSTACLE_WIDTH, OBSTACLE_HEIGHT])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - OBSTACLE_WIDTH)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - OBSTACLE_WIDTH)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)

# Game setup
all_sprites = pygame.sprite.Group()
fruits = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(8):
    fruit = Fruit()
    all_sprites.add(fruit)
    fruits.add(fruit)

for i in range(8):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

score = 0
font = pygame.font.Font(None, 36)

def game_over_screen():
    screen.fill(BLACK)
    game_over_text = font.render("GAME OVER", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    restart_text = font.render("Press 'R' to Restart", True, WHITE)

    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False

# Game loop
game_over = False
running = True
while running:
    if game_over:
        game_over_screen()
        # Reset the game
        game_over = False
        all_sprites.empty()
        fruits.empty()
        obstacles.empty()
        player = Player()
        all_sprites.add(player)
        for i in range(8):
            fruit = Fruit()
            all_sprites.add(fruit)
            fruits.add(fruit)
        for i in range(8):
            obstacle = Obstacle()
            all_sprites.add(obstacle)
            obstacles.add(obstacle)
        score = 0


    # Keep loop running at the right speed
    clock.tick(60)

    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collisions with fruits
    fruit_hits = pygame.sprite.spritecollide(player, fruits, True)
    for hit in fruit_hits:
        score += 1
        fruit = Fruit()
        all_sprites.add(fruit)
        fruits.add(fruit)

    # Check for collisions with obstacles
    obstacle_hits = pygame.sprite.spritecollide(player, obstacles, False)
    if obstacle_hits:
        game_over = True

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
