import pygame


class Jogador(pygame.sprite.Sprite):
    def __init__(self, vidas, pontos):
        super().__init__()

        self.sheet = pygame.image.load('Imagens/personagem.png')  # carrega imagem

        self.sheet.set_clip(pygame.Rect(88, 36, 76, 145))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()

        self.up_states = {0: (351, 228, 76, 145), 1: (607, 228, 76, 145)}
        self.down_states = {0: (351, 228, 76, 145), 1: (607, 0, 76, 145)}

        self.right_states = {0: (351, 36, 76, 145), 1: (607, 36, 76, 145), 2: (865, 36, 76, 145)}
        self.left_states = {0: (351, 280, 76, 145), 1: (607, 280, 76, 145), 2: (865, 280, 76, 145)}

        # Define as variáveis ​​de pulo
        self.velocidade_y = 120
        self.pulando = False

        # Define as variáveis de vidas e corações
        self.vidas = vidas
        self.vidas_iniciais = vidas
        self.coracao_vazio = pygame.transform.scale(pygame.image.load("Imagens/coracao_vazio.png").convert_alpha(), (20, 20))
        self.coracao_cheio = pygame.transform.scale(pygame.image.load("Imagens/coracao_cheio.png").convert_alpha(), (20, 20))

        # Cria a lista de corações
        self.coracoes = []

        # Adiciona corações vazios à lista
        for i in range(self.vidas):
            self.coracoes.append(self.coracao_vazio)

        # Define a direção inicial do jogador
        self.direcao = "direita"
        self.estado = "parado"
        self.frame_atual = 0
        self.frame_delay = 5
        self.frame_tempo = self.frame_delay

        # Vidas do Jogador
        self.vidas = 3

        # Pontos do Jogador
        self.pontos = 0

    def update(self, keys, width, height):

        # Define as constantes do jogador
        JOGADOR_VELOCIDADE = 5
        JOGADOR_GRAVIDADE = 0.5
        JOGADOR_FORCA_PULO = 12

        # Verifica se o jogador pressionou a tecla de pulo
        if keys[pygame.K_UP]:
            if not self.pulando:
                self.pulando = True
                self.velocidade_y = -JOGADOR_FORCA_PULO

        # Posição Inicial
        self.velocidade_y += JOGADOR_GRAVIDADE
        self.rect.y += self.velocidade_y

        # Verifica se o jogador atingiu o chão
        if self.rect.bottom >= height - 120:
            self.rect.bottom = height - 120
            self.velocidade_y = 0
            self.pulando = False

        # Verifica se o jogador saiu da tela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
            self.rect.right = width


        # Cria as direções do personagem
        if keys[pygame.K_LEFT]:
            self.rect.x -= JOGADOR_VELOCIDADE
            self.direcao = "esquerda"
            self.estado = "andando"
        elif keys[pygame.K_RIGHT]:
            self.rect.x += JOGADOR_VELOCIDADE
            self.direcao = "direita"
            self.estado = "andando"
        else:
            self.estado = "parado"

        # Atualiza imagem do sprite
        self.frame_tempo -= 1
        if self.frame_tempo == 0:
            self.frame_tempo = self.frame_delay
            self.frame_atual = (self.frame_atual + 1) % len(self.right_states)

        # Define a Posição da Sprite
        if self.estado == "andando":
            if self.direcao == "direita":
                self.sheet.set_clip(pygame.Rect(
                    *self.right_states[self.frame_atual]))
            else:
                self.sheet.set_clip(pygame.Rect(
                    *self.left_states[self.frame_atual]))
        else:
            if self.direcao == "direita":
                self.sheet.set_clip(pygame.Rect(88, 36, 76, 145))
            else:
                self.sheet.set_clip(pygame.Rect(88, 280, 76, 145))

        self.image = self.sheet.subsurface(self.sheet.get_clip())


    # Desenha os corações na tela
    def draw_Heart(self, tela):
        coracao_x = 924
        coracao_y = 10
        coracao_tamanho = 20

        for i in range(self.vidas):
            coracao = self.coracao_cheio
            coracao_rect = coracao.get_rect()
            coracao_rect.x = coracao_x - i * coracao_tamanho
            coracao_rect.y = coracao_y
            tela.blit(coracao, coracao_rect)

        for i in range(self.vidas, self.vidas_iniciais):
            coracao = self.coracao_vazio
            coracao_rect = coracao.get_rect()
            coracao_rect.x = coracao_x - i * coracao_tamanho
            coracao_rect.y = coracao_y
            tela.blit(coracao, coracao_rect)
