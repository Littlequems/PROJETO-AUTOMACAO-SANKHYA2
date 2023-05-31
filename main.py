# Escrever a lógica que a gente vai construir em português passo a passo
import pyautogui
import subprocess
import time
import cv2

pyautogui.FAILSAFE = True


# função para procurar e retornar posicionamento da imagem
def encontrar_imagem(imagem):
    while not pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9):
        time.sleep(1)
    encontrou = pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
    return encontrou


# função para clicar a direita
def direita(posicoes_imagem):
    return posicoes_imagem[0] + posicoes_imagem[2], posicoes_imagem[1] + posicoes_imagem[3]/2

#função para clicar embaixo
#x, y, largura, altura
def inferior(posicao_imagem):
    return posicao_imagem[0] + posicao_imagem[2] - 0.2, posicao_imagem[1] + [3]

# Abrir o ERP (SANKHYA)
# Coordenadas do botão "Abrir ERP" na tela
x = 928
y = 1046

# Mover o mouse para as coordenadas e clicar
pyautogui.moveTo(x, y)
pyautogui.click()

# COLOCAR MINHA SENHA NO SANKHYA (Tip2022.)

# encontrou = None
# encontrou = x, y, largura, altura
encontrou = encontrar_imagem("arquivo.png")

# sankhya ta aberto
#clicar na box de colocar a senha
encontrou = encontrar_imagem("boxsenha.png")
pyautogui.click(pyautogui.center(encontrou))

#inserir senha Tip2022.
pyautogui.write("Tip2022.")
encontrou = encontrar_imagem("prosseguirsenha.png")
pyautogui.click(pyautogui.center(encontrou))

#abrir tela de mov. financeira
encontrou = encontrar_imagem("pesquisar.png")
pyautogui.click(pyautogui.center(encontrou))

# CLICAR EM PESQUISAR E ABRIR MOVIMENTAÇÃO FINANCEIRA
encontrou = encontrar_imagem("movimentacao_financeira.png")
pyautogui.click(pyautogui.center(encontrou))
encontrou = encontrar_imagem("cancelatelaparametros.png")
pyautogui.click(pyautogui.center(encontrou))

# a função direita clica na direita no final da foto
encontrou = encontrar_imagem("procuratef.png")
pyautogui.click(pyautogui.center(encontrou))
encontrou = encontrar_imagem("processatef.png")
pyautogui.click(pyautogui.center(encontrou))

# PREENCHER DATA NEGOCIAÇÃO DIA ANTERIOR E PRIMEIRO COLOCAR NATUREZA 1030200
encontrou = encontrar_imagem("datainiciotef.png")
pyautogui.click(direita(encontrou))
pyautogui.write("30052023")
encontrou = encontrar_imagem("datafimtef.png")
pyautogui.click(direita(encontrou))
pyautogui.write("30052023")
encontrou = encontrar_imagem("toptef.png")
pyautogui.click(direita(encontrou))
pyautogui.write("5")
encontrou = encontrar_imagem("naturezatef.png")
pyautogui.click(direita(encontrou))
pyautogui.write("1030200")
encontrou = encontrar_imagem("datanegociacaotef.png")
pyautogui.click(direita(encontrou))
pyautogui.write("31052023")
encontrou = encontrar_imagem("oktef.png")
pyautogui.click(pyautogui.center(encontrou))

#fecha o aviso de enviada para portal de vendas
encontrou = encontrar_imagem("informacaook.png")
pyautogui.click(pyautogui.center(encontrou))

#manda para o portal de vendas
encontrou = encontrar_imagem("pesquisar2.png")
pyautogui.click(pyautogui.center(encontrou))
encontrou = encontrar_imagem("portaldevendas.png")
pyautogui.click(pyautogui.center(encontrou))

#muda para pedido de venda
encontrou = encontrar_imagem("mudaparapedidodevenda.png")
time.sleep(3)
pyautogui.click(pyautogui.center(encontrou))
encontrou = encontrar_imagem("pedidodevenda.png")
pyautogui.click(pyautogui.center(encontrou))

#insere data no pedido de venda
encontrou = encontrar_imagem("dtnegociacaopedidovenda.png")
pyautogui.click(pyautogui.center(encontrou))
pyautogui.write("31052023")

#preenche a parte 2 da data para filtro
encontrou = encontrar_imagem("dtnegociacaofimpedidovenda.png")
time.sleep(2)
pyautogui.click(direita(encontrou))
pyautogui.write("31052023")

#clica em aplicar
encontrou = encontrar_imagem("aplicafiltro.png")
pyautogui.click(pyautogui.center(encontrou))

#insere filtro de natureza para pesquisar
encontrou = encontrar_imagem("pesquisanatureza.png")
pyautogui.doubleClick(direita(encontrou))
pyautogui.write("1030200")

#clica em filtrar
encontrou = encontrar_imagem("aplicar.png")
pyautogui.click(pyautogui.center(encontrou))

##############################################################################################

# Encontra a primeira nota fiscal
encontrou = encontrar_imagem("naoenf.png")
posicao_inicial = inferior(encontrou)

# Clica na primeira nota fiscal
pyautogui.click(posicao_inicial)

# Simula o pressionamento das teclas Shift+End para selecionar todas as notas fiscais
pyautogui.hotkey('shift', 'end')

# Rola o scroll do mouse até o limite para encontrar as demais notas fiscais
while True:
    pyautogui.scroll(-1)  # Rola o scroll para cima (valor negativo para rolar para baixo)
    encontrou = encontrar_imagem("naoenf.png")
    if encontrou is None:
        break
    pyautogui.click(inferior(encontrou))


##############################################################################################


#confirmar para faturar
time.sleep(4)
encontrou = encontrar_imagem("confirmaantesfaturar.png")
pyautogui.click(direita(encontrou))
encontrou = encontrar_imagem("confirmaprafatura.png")
pyautogui.click(pyautogui.center(encontrou))
encontrou = encontrar_imagem("fechaconfirma.png")
pyautogui.click(pyautogui.center(encontrou))
encontrou = encontrar_imagem("cancelafatura.png")
pyautogui.click(pyautogui.center(encontrou))

#faturar notas
encontrou = encontrar_imagem("faturar.png")
pyautogui.click(pyautogui.center(encontrou))
encontrou = encontrar_imagem("dtfaturamento.png")
pyautogui.click(direita(encontrou))
pyautogui.write("31052023")
#proximo
encontrou = encontrar_imagem("proximo.png")
pyautogui.click(pyautogui.center(encontrou))

#preencher dados de faturamento
encontrou = encontrar_imagem("topfatura.png")
pyautogui.doubleClick(direita(encontrou))
pyautogui.write("21")
pyautogui.press('tab')
pyautogui.write("14")
pyautogui.press('tab')
pyautogui.write("31052023")
#marca um pra cada nota
encontrou = encontrar_imagem("marca1cadanota.png")
pyautogui.click(direita(encontrou))
#conclui faturamento
encontrou = encontrar_imagem("concluifaturamento.png")
pyautogui.click(pyautogui.center(encontrou))



# Obter as coordenadas do mouse
# coordenadas = pyautogui.position()
# print(coordenadas)
