# Bibliotecas importadas
import numpy as Num
import cv2 as OpenCV

# Abre a captura de vídeo pela WebCam (parâmetro = 0).
WebCam = OpenCV.VideoCapture(0)

while (True):
    # Captura os quadros da WebCam e Carrega na variável Frame.
    _, Frame = WebCam.read()

    # Converte a imagem do Frame de RGB para HSV.
    ImagemHSV = OpenCV.cvtColor(Frame, OpenCV.COLOR_BGR2HSV)

    # Envia para as variaveis os valores de Altura, Largura e os Canais de cores da imagem.
    (Altura, Largura, Canais) = ImagemHSV.shape

    # Declara os intervalos de cores Amarelas a serem detectadas.
    AmareloClaro = Num.array([23, 59, 119])
    AmareloEscuro = Num.array([54, 255, 255])

    # Declara os intervalos de cores Azuis a serem detectadas.
    AzulClaro = Num.array([97, 100, 117])
    AzulEscuro = Num.array([117, 255, 255])

    # Declara os intervalos de cores Vermelhas a serem detectadas.
    VermelhoClaro = Num.array([166, 84, 141])
    VermelhoEscuro = Num.array([186, 255, 255])


    # Identifica as diferenças de tonalidades Amarelas
    mAmarelo = OpenCV.inRange(ImagemHSV, AmareloClaro, AmareloEscuro)

    # Realiza as operações nas matrizes da imagem
    ResultadoAmarelo = OpenCV.bitwise_and(Frame, Frame, mask = mAmarelo)

    # Converte para escala de Cinza
    EscalaCinzaAmarelo = OpenCV.cvtColor(ResultadoAmarelo, OpenCV.COLOR_BGR2GRAY)

    # Converte para Preto e Branco (Usando o OTSU)
    _, EscalaCinzaAmarelo = OpenCV.threshold(EscalaCinzaAmarelo, 0, 255, OpenCV.THRESH_BINARY | OpenCV.THRESH_OTSU)

    # Constroi as curvas do contorno (Amarelo) 
    CurvaAmarelo, _ = OpenCV.findContours(EscalaCinzaAmarelo, OpenCV.RETR_TREE, OpenCV.CHAIN_APPROX_SIMPLE)


    # Identifica as diferenças de tonalidades Azuis
    mAzul = OpenCV.inRange(ImagemHSV, AzulClaro, AzulEscuro)

    # Realiza as operações nas matrizes da imagem
    ResultadoAzul = OpenCV.bitwise_and(Frame, Frame, mask = mAzul)

    # Converte para escala de Cinza
    EscalaCinzaAzul = OpenCV.cvtColor(ResultadoAzul, OpenCV.COLOR_BGR2GRAY)

    # Converte para Preto e Branco (Usando o OTSU)
    _, EscalaCinzaAzul = OpenCV.threshold(EscalaCinzaAzul, 0, 255, OpenCV.THRESH_BINARY | OpenCV.THRESH_OTSU)

    # Constroi as curvas do contorno (Azul)
    CurvaAzul, _ = OpenCV.findContours(EscalaCinzaAzul, OpenCV.RETR_TREE, OpenCV.CHAIN_APPROX_SIMPLE)


    # Identifica as diferenças de tonalidades Vermelhas
    mVermelho = OpenCV.inRange(ImagemHSV, VermelhoClaro, VermelhoEscuro)

    # Realiza as operações nas matrizes da imagem
    ResultadoVermelho = OpenCV.bitwise_and(Frame, Frame, mask = mVermelho)

    # Converte para escala de Cinza
    EscalaCinzaVermelho = OpenCV.cvtColor(ResultadoVermelho, OpenCV.COLOR_BGR2GRAY)

    # Converte para Preto e Branco (Usando o OTSU)
    _, EscalaCinzaVermelho = OpenCV.threshold(EscalaCinzaVermelho, 0, 255, OpenCV.THRESH_BINARY | OpenCV.THRESH_OTSU)

    # Constroi as curvas do contorno (Azul)
    CurvaVermelho, _ = OpenCV.findContours(EscalaCinzaVermelho, OpenCV.RETR_TREE, OpenCV.CHAIN_APPROX_SIMPLE)


    # Escreve na imagem da janela a mensagem de sair.
    OpenCV.putText(Frame, 'Aperte "q" para sair', (Largura-200, Altura-20), OpenCV.FONT_ITALIC, 0.5, (255, 255, 255), 2, OpenCV.LINE_AA, False)

    # Realiza a detecção de contornos Amarelos.
    if CurvaAmarelo:

        # Retorna a área em pixels do contorno Amarelo.
        AreaMaximaAmarelo = OpenCV.contourArea(CurvaAmarelo[0])
        CurvaIdAmarelo = 0
        i = 0
        for ContornoAmarelo in CurvaAmarelo:
            if AreaMaximaAmarelo < OpenCV.contourArea(ContornoAmarelo):
                AreaMaximaAmarelo = OpenCV.contourArea(ContornoAmarelo)
                CurvaIdAmarelo = i
            i += 1

        # Atribui a area em pixels do maior contorno Amarelo.
        ContornoAmarelo = CurvaAmarelo[CurvaIdAmarelo]

        # Define os valores dos pontos que serão desenhados entorno do objeto Amarelo.
        XAmarelo, YAmarelo, LarguraAmarelo, AlturaAmarelo = OpenCV.boundingRect(ContornoAmarelo)

        # Realiza o desenho do retangulo Amarelo caso o objeto detectado tenha mais de 100 pixels.
        if(AreaMaximaAmarelo > 100.0):

            # Desenha o retangulo Amarelo.
            OpenCV.rectangle(Frame, (XAmarelo, YAmarelo), (XAmarelo + LarguraAmarelo, YAmarelo + AlturaAmarelo), (0, 255, 255), 2)

            # Escreve a mensagem do objeto Amarelo na imagem.
            OpenCV.putText(Frame, 'Objeto Amarelo Detectado', (20, 25) , OpenCV.FONT_ITALIC, 0.5, (0, 255, 255), 2, OpenCV.LINE_AA, False) 
    
    # Realiza a detecção de contornos Azuis.
    if CurvaAzul:

        # Retorna a área em pixels do contorno Azul.
        AreaMaximaAzul = OpenCV.contourArea(CurvaAzul[0])
        CurvaIdAzul = 0
        j = 0
        for ContornoAzul in CurvaAzul:
            if AreaMaximaAzul < OpenCV.contourArea(ContornoAzul):
                AreaMaximaAzul = OpenCV.contourArea(ContornoAzul)
                CurvaIdAzul = j
            j += 1

        # Atribui a area em pixels do maior contorno Azul.
        ContornoAzul = CurvaAzul[CurvaIdAzul]

        # Define os valores dos pontos que serão desenhados entorno do objeto Azul.
        XAzul, YAzul, LarguraAzul, AlturaAzul = OpenCV.boundingRect(ContornoAzul)

        # Realiza o desenho do retangulo Azul caso o objeto detectado tenha mais de 100 pixels.
        if(AreaMaximaAzul > 100.0):

            # Desenha o retangulo Azul.
            OpenCV.rectangle(Frame, (XAzul, YAzul), (XAzul + LarguraAzul, YAzul + AlturaAzul), (255, 0, 0), 2)

            # Escreve a mensagem do objeto Azul na imagem.
            OpenCV.putText(Frame, 'Objeto Azul Detectado', (20, 45) , OpenCV.FONT_ITALIC, 0.5, (255, 0, 0), 2, OpenCV.LINE_AA, False)
    
    # Realiza a detecção de contornos Vermelhos.
    if CurvaVermelho:

        # Retorna a área em pixels do contorno Vermelho.
        AreaMaximaVermelho = OpenCV.contourArea(CurvaVermelho[0])
        CurvaIdVermelho = 0
        k = 0
        for ContornoVermelho in CurvaVermelho:
            if AreaMaximaVermelho < OpenCV.contourArea(ContornoVermelho):
                AreaMaximaVermelho = OpenCV.contourArea(ContornoVermelho)
                CurvaIdVermelho = k
            k = k + 1

        # Atribui a area em pixels do maior contorno Vermelho.
        ContornoVermelho = CurvaVermelho[CurvaIdVermelho]

        # Define os valores dos pontos que serão desenhados entorno do objeto Vermelho
        XVermelho, YVermelho, LarguraVermelho, AlturaVermelho = OpenCV.boundingRect(ContornoVermelho)

        # Realiza o desenho do retangulo Vermelho caso o objeto detectado tenha mais de 100 pixels.
        if(AreaMaximaVermelho > 100.0):

            # Desenha o retangulo Vermelho.
            OpenCV.rectangle(Frame, (XVermelho, YVermelho), (XVermelho + LarguraVermelho, YVermelho + AlturaVermelho), (0, 0, 255), 2)

            # Escreve a mensagem do objeto Vermelho na imagem.
            OpenCV.putText(Frame, 'Objeto Vermelho Detectado', (20, 65) , OpenCV.FONT_ITALIC, 0.5, (0, 0, 255), 2, OpenCV.LINE_AA, False)
    
    # Deixar em tela cheia
    OpenCV.namedWindow('Detector de Cores', OpenCV.WND_PROP_FULLSCREEN)
    OpenCV.setWindowProperty('Detector de Cores', OpenCV.WND_PROP_FULLSCREEN, OpenCV.WINDOW_FULLSCREEN)

    # Cria a janela na tela com as imagens.
    OpenCV.imshow('Detector de Cores', Frame)

    # Sai do loop ao apertar q.
    if (OpenCV.waitKey(1) & 0xFF == ord('q')):
        break

# Destroi as janelas.   
WebCam.release()
OpenCV.destroyAllWindows()