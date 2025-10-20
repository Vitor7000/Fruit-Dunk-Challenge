import pygame
import random
import os

# Inicialização do Pygame
pygame.init()

# --- Configurações da Tela ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Fruit Dunk Challenge')

# --- Cores ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# --- Fontes ---
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

# --- Carregamento de Imagens ---
# O usuário irá colocar as imagens na pasta 'assets'
assets_path = 'assets'
player_img = None
fruit_img = None
obstacle_img = None

try:
    player_img = pygame.image.load(os.path.join(assets_path, 'player.png')).convert_alpha()
except (pygame.error, FileNotFoundError):
    print("Imagem 'player.png' não encontrada. Usando um retângulo azul.")

try:
    fruit_img = pygame.image.load(os.path.join(assets_path, 'fruit.png')).convert_alpha()
except (pygame.error, FileNotFoundError):
    print("Imagem 'fruit.png' não encontrada. Usando um retângulo verde.")

try:
    obstacle_img = pygame.image.load(os.path.join(assets_path, 'obstacle.png')).convert_alpha()
except (pygame.error, FileNotFoundError):
    print("Imagem 'obstacle.png' não encontrada. Usando um retângulo vermelho.")

# --- Classes do Jogo ---

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if player_img:
            self.image = pygame.transform.scale(player_img, (50, 70))
        else:
            self.image = pygame.Surface([50, 70])
            self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -8
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 8
        self.rect.x += self.speed_x
        # Manter o jogador dentro da tela
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if fruit_img:
            self.image = pygame.transform.scale(fruit_img, (30, 30))
        else:
            self.image = pygame.Surface([30, 30])
            self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 5)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if obstacle_img:
            self.image = pygame.transform.scale(obstacle_img, (40, 40))
        else:
            self.image = pygame.Surface([40, 40])
            self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(3, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(3, 8)

# --- Funções Auxiliares ---

def draw_text(surf, text, size, x, y, color):
    font_aux = pygame.font.Font(None, size)
    text_surface = font_aux.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def show_game_over_screen(score):
    screen.fill(BLACK)
    draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4, RED)
    draw_text(screen, f"Pontuação Final: {score}", 32, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, WHITE)
    draw_text(screen, "Pressione qualquer tecla para reiniciar", 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4, WHITE)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                waiting = False

# --- Loop Principal do Jogo ---

def game_loop():
    all_sprites = pygame.sprite.Group()
    fruits = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    for _ in range(8):
        fruit = Fruit()
        all_sprites.add(fruit)
        fruits.add(fruit)

    for _ in range(4):
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    score = 0
    running = True
    game_over = False
    clock = pygame.time.Clock()

    while running:
        if game_over:
            show_game_over_screen(score)
            game_over = False
            # Reiniciar o jogo
            all_sprites = pygame.sprite.Group()
            fruits = pygame.sprite.Group()
            obstacles = pygame.sprite.Group()

            player = Player()
            all_sprites.add(player)

            for _ in range(8):
                fruit = Fruit()
                all_sprites.add(fruit)
                fruits.add(fruit)

            for _ in range(4):
                obstacle = Obstacle()
                all_sprites.add(obstacle)
                obstacles.add(obstacle)

            score = 0

        # Manter o loop na velocidade certa
        clock.tick(60)

        # Processar eventos (input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualizar
        all_sprites.update()

        # Verificar colisão jogador com frutas
        fruit_hits = pygame.sprite.spritecollide(player, fruits, True)
        for hit in fruit_hits:
            score += 10
            fruit = Fruit()
            all_sprites.add(fruit)
            fruits.add(fruit)

        # Verificar colisão jogador com obstáculos
        obstacle_hits = pygame.sprite.spritecollide(player, obstacles, False)
        if obstacle_hits:
            game_over = True

        # Desenhar / Renderizar
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Desenhar placar e controles
        draw_text(screen, f"Pontuação: {score}", 28, SCREEN_WIDTH / 2, 10, WHITE)
        draw_text(screen, "Controles: <- (Esquerda) | -> (Direita)", 20, SCREEN_WIDTH / 2, 40, WHITE)

        # Depois de desenhar tudo, vira o display
        pygame.display.flip()

    pygame.quit()

# Iniciar o jogo
if __name__ == "__main__":
    game_loop()
