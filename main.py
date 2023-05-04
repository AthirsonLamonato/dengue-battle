import pygame
import random
from Player import Jogador
from Enemy import Inimigo
from GoodAction import BoasAcoes


def tela_inicial(tela, largura_tela, altura_tela, fundo_imagem):

    # Criação dos textos
    titulo_texto = pygame.font.SysFont(None, 50).render(
        "Dengue Battle", True, (255, 255, 255))
    jogar_texto = pygame.font.SysFont(None, 30).render(
        "Jogar", True, (255, 255, 255))
    sair_texto = pygame.font.SysFont(None, 30).render(
        "Sair", True, (255, 255, 255))

    # Cria dois objetos Rect que serão usados para posicionar textos na tela do jogo.
    jogar_rect = jogar_texto.get_rect(
        center=(largura_tela / 2, altura_tela / 2))
    sair_rect = sair_texto.get_rect(
        center=(largura_tela / 2, altura_tela / 2 + 70))

    # Loop principal da tela inicial
    while True:
        # Processamento dos eventos do Pygame
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if jogar_rect.collidepoint(evento.pos):
                    return "jogar"
                elif sair_rect.collidepoint(evento.pos):
                    pygame.quit()
                    quit()

        # Desenho dos sprites
        tela.blit(fundo_imagem, (0, 0))
        tela.blit(titulo_texto, (largura_tela / 2 -
                  titulo_texto.get_width() / 2, 100))

        tela.blit(jogar_texto, (jogar_rect.centerx - jogar_texto.get_width() /
                  2, jogar_rect.centery - jogar_texto.get_height()/2))
        tela.blit(sair_texto, (sair_rect.centerx - sair_texto.get_width() /
                  2, sair_rect.centery - sair_texto.get_height()/2))

        pygame.display.update()  # Atualiza a tela

def tela_game_over(tela, largura_tela, altura_tela, fundo_imagem, jogador):

    # Desenha o fundo na tela
    tela.blit(fundo_imagem, (0, 0))

    # Define a fonte e as mensagens de Game Over e Pontuação Final
    fonte_game_over = pygame.font.SysFont(None, 100)
    mensagem_game_over = fonte_game_over.render("Game Over", True, (255, 0, 0))
    mensagem_pontuacao = pygame.font.SysFont(None, 50).render(
        f"Pontuação: {jogador.pontos}", True, (255, 255, 255))

    # Define as opções de reiniciar ou sair do jogo
    mensagem_reiniciar = pygame.font.SysFont(None, 30).render(
        "Pressione R para reiniciar o jogo", True, (255, 255, 255))
    mensagem_sair = pygame.font.SysFont(None, 30).render(
        "Pressione Q para sair do jogo", True, (255, 255, 255))

    # Define as posições das mensagens na tela
    mensagem_game_over_rect = mensagem_game_over.get_rect()
    mensagem_game_over_rect.center = (
        largura_tela // 2, altura_tela // 2 - 100)

    mensagem_pontuacao_rect = mensagem_pontuacao.get_rect()
    mensagem_pontuacao_rect.center = (largura_tela // 2, altura_tela // 2)

    mensagem_reiniciar_rect = mensagem_reiniciar.get_rect()
    mensagem_reiniciar_rect.center = (largura_tela // 2, altura_tela // 2 + 50)

    mensagem_sair_rect = mensagem_sair.get_rect()
    mensagem_sair_rect.center = (largura_tela // 2, altura_tela // 2 + 100)

    # Desenha as mensagens na tela
    tela.blit(mensagem_game_over, mensagem_game_over_rect)
    tela.blit(mensagem_pontuacao, mensagem_pontuacao_rect)
    tela.blit(mensagem_reiniciar, mensagem_reiniciar_rect)
    tela.blit(mensagem_sair, mensagem_sair_rect)

    # Atualiza a tela
    pygame.display.update()

    # Aguarda o jogador pressionar as teclas de reiniciar ou sair do jogo
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    jogador.vidas = 3
                    jogador.pontos = 0
                    return "reiniciar"  # Reinicia o jogo
                elif evento.key == pygame.K_q:
                    pygame.quit()  # Sai do jogo
                    quit()
            elif evento.type == pygame.QUIT:
                pygame.quit()
                quit()

# Verifica se a posição vertical do sprite é maior que a altura da tela.
# Se for maior remove a sprite da tela
def remover_sprites_fora_da_tela(grupo_sprites, altura_tela):
    for sprite in grupo_sprites:
        if sprite.rect.y > altura_tela:
            sprite.kill()

# Verifica se existe colisão dentro do mesmo grupo de sprites
def colisao_grupo(sprite, grupo_sprites):
    for s in grupo_sprites:
        if pygame.sprite.collide_rect(sprite, s):
            return True
    return False

# Verifica se o numero de sprites no grupo é menor que dois, se for, gera uma quantidade de sprites aleatória entre 1 e 5
# Verifica se a sprite gerada colide com alguem do mesmo grupo, e move para outra posição
def gerar_sprites_aleatorios(sprite_grupo, sprite, largura_tela):
    if len(sprite_grupo.sprites()) < 2:
        quantidade = random.randint(1, 5)
        for i in range(quantidade):
            novo_sprite = sprite.__class__()
            novo_sprite.rect.x = random.randint(
                0, largura_tela - novo_sprite.rect.width)
            novo_sprite.rect.y = 0
            while colisao_grupo(novo_sprite, sprite_grupo):
                novo_sprite.rect.x = random.randint(
                    0, largura_tela - novo_sprite.rect.width)
            sprite_grupo.add(novo_sprite)

def jogo():

    # Inicialização do Pygame
    pygame.init()

    # Definição das dimensões da tela
    largura_tela = 1024
    altura_tela = 600
    tela = pygame.display.set_mode((largura_tela, altura_tela))

    # Carregamento da imagem de fundo
    fundo_imagem = pygame.image.load("Imagens/fundo.png").convert()

    # Chama a Tela Inicial do Jogo, que foi declarada acima
    tela_inicial(tela, largura_tela, altura_tela, fundo_imagem)

    # Criação dos personagens
    inimigo = Inimigo()
    acoes = BoasAcoes()
    jogador = Jogador(vidas=3, pontos=0)

    # Criação dos grupos de sprites
    grupo_inimigos = pygame.sprite.Group()
    grupo_jogador = pygame.sprite.Group()
    grupo_acoes = pygame.sprite.Group()

    grupo_inimigos.add(inimigo)
    grupo_jogador.add(jogador)
    grupo_acoes.add(acoes)

    # Configuração do relógio do jogo
    relogio = pygame.time.Clock()

    while True:

        # Processamento dos eventos do Pygame
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Captura das teclas pressionadas pelo jogador
        teclas_pressionadas = pygame.key.get_pressed()

        # Atualização dos sprites
        grupo_jogador.update(teclas_pressionadas, largura_tela, altura_tela)

        tela.blit(fundo_imagem, (0, 0))

        # Desenho dos sprites
        grupo_acoes.draw(tela)
        jogador.draw_Heart(tela)
        grupo_jogador.draw(tela)
        grupo_inimigos.draw(tela)

        # Verifica a colisão entre o jogador e os inimigos
        colisoes_inimigos = pygame.sprite.spritecollide(
            jogador, grupo_inimigos, True)
        for inimigos in colisoes_inimigos:
            jogador.vidas -= 1
            jogador.pontos -= 1

            if jogador.vidas <= 0:
                tela_game_over(tela, largura_tela, altura_tela,fundo_imagem, jogador)

        # Verifica a colisão entre o jogador e as boas ações
        colisoes_acoes = pygame.sprite.spritecollide(
            jogador, grupo_acoes, True)
        for acao in colisoes_acoes:
            jogador.pontos += 5

        # Atualiza os pontos do jogador na tela
        pontos_texto = pygame.font.SysFont(None, 30).render(
            f"Pontos: {jogador.pontos}", True, (255, 255, 255))
        tela.blit(pontos_texto, (10, 10))

        # Remoção de sprites que saíram da tela
        remover_sprites_fora_da_tela(grupo_acoes, altura_tela)
        remover_sprites_fora_da_tela(grupo_inimigos, altura_tela)

        # Geração de novos sprites aleatórios
        gerar_sprites_aleatorios(grupo_inimigos,  Inimigo(), largura_tela)
        gerar_sprites_aleatorios(grupo_acoes,  BoasAcoes(), largura_tela)

        # Atualização dos sprites que se movem
        grupo_inimigos.update()
        grupo_acoes.update()

        pygame.display.update()  # Atualiza a tela
        relogio.tick(60)  # Define a taxa de atualização do jogo


jogo()
