import pygame
import random


class BoasAcoes(pygame.sprite.Sprite):

    # Define uma posição aleatoria para a boa ação
    def posicao_aleatoria(self):
        largura_tela = pygame.display.get_surface().get_width()
        altura_tela = pygame.display.get_surface().get_height()
        x = random.randint(0, largura_tela - self.rect.width)
        y = random.randint(0, altura_tela - self.rect.height)
        return x, y
    
    def __init__(self, clip=None):
        super().__init__()
        self.sheet = pygame.image.load('Imagens/acoes.png')

        # Define a lista de posições das sprites
        self.clips = [
            pygame.Rect(8, 21, 120, 119),
            pygame.Rect(170, 21, 120, 119),
            pygame.Rect(337, 21, 120, 119),
            pygame.Rect(506, 21, 120, 119),
            pygame.Rect(8, 211, 120, 119),
            pygame.Rect(170, 211, 120, 119),
            pygame.Rect(337, 211, 120, 119),
            pygame.Rect(506, 211, 120, 119),
        ]
        # Verifica se uma posição de sprite foi passada como argumento, se não define uma aleatória
        if clip is not None:
            self.clip = clip
        else:
            self.clip = random.randint(0, len(self.clips) - 1)

        # define a sprite atual a partir da posição self.clip   
        self.sheet.set_clip(self.clips[self.clip])
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()


        # Define a posição aleatória da sprite na tela
        self.rect.x, self.rect.y = self.posicao_aleatoria()

        # Define o intervalo de tempo entre as trocas de sprite (em milissegundos)
        self.intervalo = 100

        # Define o tempo da última troca de sprite
        self.last_update = pygame.time.get_ticks()

    def update(self):

        # Verifica se já passou o tempo suficiente para trocar a sprite
        now = pygame.time.get_ticks()

        # Verifica se já passou o tempo suficiente para trocar a sprite
        # Se o tempo desde a última atualização for maior do que o intervalo definido,
        # então a sprite atual deve ser atualizada
        if now - self.last_update > self.intervalo:
            
            # Atualiza o tempo da última atualização para o tempo atual
            self.last_update = now

            # Define o recorte (clip) da sprite atual
            self.sheet.set_clip(self.clips[self.clip])
            self.image = self.sheet.subsurface(self.sheet.get_clip())

        # Move a ação para baixo
        self.rect.y += 1