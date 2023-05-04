import pygame
import random


class Inimigo(pygame.sprite.Sprite):
    

    # Define uma posição aleatoria para a boa ação
    def posicao_aleatoria(self):
        largura_tela = pygame.display.get_surface().get_width()
        altura_tela = pygame.display.get_surface().get_height()
        x = random.randint(0, largura_tela - self.rect.width)
        y = random.randint(0, altura_tela - self.rect.height)
        return x, y

    def __init__(self):
        super().__init__()
        self.sheet = pygame.image.load('Imagens/mosquito.png')

        # Define o tamanho da área retangular que será recortada da imagem original e a obtém
        self.sheet.set_clip(pygame.Rect(0, 0, 87, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()

        # Define a posição aleatória da sprite na tela
        self.rect.x, self.rect.y = self.posicao_aleatoria()

        # Define a lista de clipes
        self.clips = [pygame.Rect(0, 0, 87, 76),
                      pygame.Rect(82, 0, 87, 76),
                      pygame.Rect(164, 0, 87, 76),
                      pygame.Rect(246, 0, 87, 76),
                      pygame.Rect(328, 0, 87, 76),
                      pygame.Rect(410, 0, 87, 76)]

        # Define o índice da sprite atual
        self.current_clip = 0

        # Define o intervalo de tempo entre as trocas de sprite (em milissegundos)
        self.intervalo = 100

        # Define o tempo da última troca de sprite
        self.last_update = pygame.time.get_ticks()

    def update(self):
        # Verifica se já passou o tempo suficiente para trocar a sprite
        now = pygame.time.get_ticks()

        # Verifica se já passou o tempo suficiente para trocar a sprite com base no intervalo definido
        # Se o tempo passado for maior que o intervalo, atualiza a sprite atual e redefine o tempo da última troca de sprite
        if now - self.last_update > self.intervalo:
            self.last_update = now

            # Atualiza a sprite atual
            self.current_clip += 1
            if self.current_clip >= len(self.clips):
                self.current_clip = 0
            self.sheet.set_clip(self.clips[self.current_clip])
            self.image = self.sheet.subsurface(self.sheet.get_clip())

        # Move o inimigo para baixo
        self.rect.y += 1
