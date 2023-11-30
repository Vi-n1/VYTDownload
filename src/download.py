# -*- coding: utf-8 -*-
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QProgressBar, QLabel, QListWidget
from PySide6.QtGui import QPixmap
from requests import get
import pytube as yt

from io import BufferedWriter
from time import strftime, gmtime
from os import rename, remove, mkdir
from os.path import exists


class YouTube(QThread):
    """
    Classe responsável por fazer os downloads
    """

    def __init__(self):
        super().__init__()
        # Tipo do arqv(MP4 ou MP3).
        self._tipo = None

        # Quantidade de arqv, 1 para playlist ou 0 para vídeo/música.
        self._quantidade = None

        # Barra que representa a porcentagem do download.
        self._barra_progresso = None

        # Url do vídeo/música ou da playlist.
        self._link = None

        # QLabel que irá conter a thumbnail.
        self._thumbnail = None

        # Duração do vídeo/música .
        self._minutos = None

        # QListWidget que irá conter as músicas.
        self._lista_widgets = None

        # Path padão de cada tipo.
        self._PATH_MUSICAS = 'Musicas'
        self._PATH_VIDEOS = 'Vídeos'
        self._PATH_PLAYLIST = 'PlayList'
        self._criar_pastas()

        # Objetivo do YouTube
        self._objeto_yt = None

    def _criar_pastas(self):
        """
        Cria os paths padrões.
        """
        if not exists(self._PATH_MUSICAS):
            mkdir(self._PATH_MUSICAS)

        if not exists(self._PATH_VIDEOS):
            mkdir(self._PATH_VIDEOS)

        if not exists(self._PATH_PLAYLIST):
            mkdir(self._PATH_PLAYLIST)

    def _criar_pasta_autor(self, path_base: str, autor: str) -> str:
        """
        Cria uma pasta no path padrão com o nome do autor.

        Args:
            path_base (str): Path padrão.
            autor (str): Nome do autor.

        Returns:
            str: Path do autor
        """
        path_autor = path_base + '/' + autor
        if not exists(path_autor):
            mkdir(path_autor)
        return path_autor

    def set_tipo(self, tipo: str):
        """
        Define o tipo do arqv.

        Args:
            tipo (str): MP4 ou MP3.
        """
        if isinstance(tipo, str):
            self._tipo = tipo

    def set_quantidade(self, quantidade: int):
        """
        Define se é unitário ou variados.

        Args:
            quantidade (int): 1 para playlist ou 0 para vídeo/música.
        """
        if isinstance(quantidade, int):
            self._quantidade = quantidade

    def set_link(self, url: str):
        """
        Define a Url do vídeo/música ou playlist.

        Args:
            url (str): Url do vídeo/música ou playlist.
        """
        if isinstance(url, str):
            self._link = url

    def set_barra_progresso(self, barra_progresso: QProgressBar):
        """
        Define o widget que exibe a barra de progresso.

        Args:
            barra_progresso (QProgressBar): Widget que exibe o progresso do download.
        """
        if isinstance(barra_progresso, QProgressBar):
            self._barra_progresso = barra_progresso

    def set_thumbnail(self, thumbnail: QLabel):
        """
        Define o widget que exibe a thumbnail.

        Args:
            thumbnail (QLabel): Widget que exibe a miniatura da imagem do vídeo.
        """
        if isinstance(thumbnail, QLabel):
            self._thumbnail = thumbnail

    def set_minutos(self, minutos: QLabel):
        """
        Define o widget que exibe os minutos.

        Args:
            minutos (QLabel): Widget que exibe os minutos.
        """
        if isinstance(minutos, QLabel):
            self._minutos = minutos

    def set_lista_widgets(self, lista_widgets: QListWidget):
        """
        Define o widget que exibe as músicas baixadas.

        Args:
            lista_widgets (QListWidget): Widget que exibe as músicas baixadas.
        """
        if isinstance(lista_widgets, QListWidget):
            self._lista_widgets = lista_widgets

    def _baixar_musica(self):
        """
        Faz o download da música.
        """
        # Obtendo o path.
        path = self._criar_pasta_autor(
            self._PATH_MUSICAS, self._objeto_yt.author
        )

        # Inicia o download.
        nome_arqv_mp4 = self._objeto_yt.streams.get_audio_only().download(
            output_path=path
        )

        # Renomeando a extensão do arqv de mp4 para mp3.
        nome_arqv_mp3 = nome_arqv_mp4.replace('mp4', 'mp3')
        rename(nome_arqv_mp4, nome_arqv_mp3)

    def _baixar_video(self):
        """
        Faz o download de vídeo.
        """
        # Obtendo o path.
        path = self._criar_pasta_autor(
            self._PATH_VIDEOS, self._objeto_yt.author
        )

        # Inicia o download.
        self._objeto_yt.streams.get_highest_resolution().download(
            output_path=path
        )

    def _baixar_playlist(self):
        """
        Faz o download da playlist.
        """
        # Limpando a exibição.
        self._lista_widgets.clear()

        # Obtendo o path.
        path = self._criar_pasta_autor(
            self._PATH_PLAYLIST, self._objeto_yt.videos[0].author
        )

        for objeto_yt_musica in self._objeto_yt.videos:
            # Inicia o download.
            nome_arqv_mp4 = objeto_yt_musica.streams.get_audio_only().download(
                output_path=path
            )

            # Renomeando a extensão do arqv de mp4 para mp3.
            nome_arqv_mp3 = nome_arqv_mp4.replace('mp4', 'mp3')
            rename(nome_arqv_mp4, nome_arqv_mp3)

            # Adicionado as música baixadas na exibição.
            self._lista_widgets.addItem(objeto_yt_musica.title)

    def _porcentagem_baixada(
        self, stream: BufferedWriter, chunk: bytes, bytes_remaining: int
    ):
        """
        Atualiza o widget com a porcentagem do download.

        Args:
            stream (BufferedWriter): Identificador do arquivo no qual a mídia está sendo gravada.
            chunk (bytes): Segmento de dados binários de arquivos de mídia, ainda não gravados no disco.
            bytes_remaining (int): Delta entre o tamanho total do arquivo em bytes e a quantidade já baixada.
        """
        size = stream.filesize
        progress = int(
            (float(abs(bytes_remaining - size) / size)) * float(100)
        )
        self._barra_progresso.setValue(progress)

    def run(self):
        """
        Execução inicial dos downloads.
        """
        unitario = 0

        # Verificando se é um vídeo ou uma playlist.
        if self._quantidade == unitario:

            # Objeto YouTube.
            self._objeto_yt = yt.YouTube(
                url=self._link, on_progress_callback=self._porcentagem_baixada
            )

            # Atribuindo os minutos no formato 00:00:00.
            self._minutos.setText(
                f'{str(strftime("%H:%M:%S", gmtime(int(self._objeto_yt.length))))}'
            )

            # Fazendo o download da thumbnail.
            thumbnail_baixada = get(self._objeto_yt.thumbnail_url)

            # Nome temporário da thumbnail.
            nome_thumbnail = 'T.jpg'

            # Escrevendo os bytes da thumbnail.
            with open(nome_thumbnail, 'wb') as thumbnail:
                thumbnail.write(thumbnail_baixada.content)

            # Exibindo a thumbnail na aplicação e removendo o arqv local.
            self._thumbnail.setPixmap(QPixmap(nome_thumbnail))
            self._thumbnail.setScaledContents(True)
            remove(nome_thumbnail)

            # Verificação para identificar o tipo do arqv e iniciar o download.
            if self._tipo == 'MP3':
                self._baixar_musica()
            else:
                self._baixar_video()

        else:
            # Instância do objeto Playlist.
            self._objeto_yt = yt.Playlist(self._link)

            # Iniciando o download.
            self._baixar_playlist()
