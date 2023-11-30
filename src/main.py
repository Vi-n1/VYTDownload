# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QUrl
from PySide6.QtGui import QMovie
from sys import exit, argv

from Ui.janela_ui import Ui_Janela
from download import YouTube


class VYTDownload(QMainWindow, Ui_Janela):
    """
    Classe principal
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Capitura o link da pagina clicada.
        self.wev_youtube.urlChanged.connect(
            lambda url: self.Autocompletar_url(url)
        )

        # Inicia o processo de download ao ser clicado.
        self.pb_baixar.clicked.connect(self.baixar)

        # Instância da classe responsável pelo o download.
        self.youtube = YouTube()

        # Carrega o gif na memória e aplica como "background" no widget l_backgroud_gif.
        self.gif = QMovie(r'Ui\gif\background.gif')
        self.l_backgroud_gif.setMovie(self.gif)
        self.gif.start()

    def Autocompletar_url(self, link: QUrl) -> None:
        """
        Capitura o link do vídeo clicado e defini como o texo do widget :obj:`le_link`.

        Args:
            link (QUrl): Url da página atual do YouTube.
        """
        url = link.url()
        if self.is_valido(url):
            self.le_link.setText(url)

    def reiniciar_cofg(self):
        """
        Reinicia os widgets para o estado "inalterado".
        """
        self.l_minutos.setText('')
        self.pgsbar_unitario.setValue(0)

    def baixar(self):
        """
        Baixa o video/playlist informado.
        """
        # Reinicia os widget que contém informações sobre o download anterior.
        self.reiniciar_cofg()

        # Obtendo o link do vídeo.
        link = self.le_link.text()

        # Obtendo o formato selecionado MP4/MP3.
        tipo = self.cb_formt_aqrv.currentText()

        # unitario == 0, variado == 1.
        unitario_ou_variado = self.unitario_ou_playlist()

        # Verificar se o link é válido.
        if self.is_valido(link):
            unitario = 0

            # Atribuindo as informações do vídeo/playlist para realização do download.
            self.youtube.set_link(link)
            self.youtube.set_tipo(tipo)
            self.youtube.set_quantidade(unitario_ou_variado)

            # Verificando se é um vídeo ou uma playlist.
            if unitario_ou_variado == unitario:
                # Alterando para a visualização de um único vídeo.
                self.paginas.setCurrentIndex(0)

                # Atribuindo as informações do vídeo.
                self.youtube.set_barra_progresso(self.pgsbar_unitario)
                self.youtube.set_thumbnail(self.l_thumbnail)
                self.youtube.set_minutos(self.l_minutos)

                # Iniciando o download.
                self.youtube.start()

            else:
                # Alterando para a visualização de uma playlist.
                self.paginas.setCurrentIndex(1)

                # Atribuindo o widget que exibi os arquivos baixados.
                self.youtube.set_lista_widgets(self.lw_playlist_musicas)

                # Iniciando o download.
                self.youtube.start()

    def is_valido(self, link: str) -> bool:
        """
        Verifica se o linke é válido.

        Args:
            link (str): Url da página atual.

        Returns:
            bool: Validez.
        """
        return link.count('watch') == 1

    def unitario_ou_playlist(self) -> int:
        """
        Verifica se o link é de um vídeo ou de uma playlist.

        Returns:
            int: 1 para playlist ou 0 para vídeo
        """
        link = self.le_link.text()
        if link.count('list') == 1:
            return 1
        else:
            return 0


if __name__ == '__main__':
    app = QApplication(argv)
    janela = VYTDownload()
    janela.show()
    exit(app.exec())
