# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListView,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QStackedWidget,
    QWidget,
)


class Ui_Janela(object):
    def setupUi(self, Janela):
        if not Janela.objectName():
            Janela.setObjectName('Janela')
        Janela.resize(800, 600)
        Janela.setMinimumSize(QSize(800, 600))
        Janela.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile('Ui/img/Logo.png', QSize(), QIcon.Normal, QIcon.Off)
        Janela.setWindowIcon(icon)
        Janela.setStyleSheet(
            'QFrame{\n'
            '	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(208, 149, 183, 255), stop:0.795455 rgba(88, 0, 239, 255));\n'
            '}\n'
            'QPushButton, QComboBox{\n'
            '	font: 700 italic 10pt "Arial";\n'
            '	background-color: rgba(154, 154, 231, 253);\n'
            '	border-radius: 5%;\n'
            '	border: 1px solid rgb(40, 42, 54);\n'
            '}\n'
            'QPushButton::hover, QComboBox::hover{\n'
            '	background-color: rgb(163, 163, 244);\n'
            '}\n'
            'QPushButton::pressed, QComboBox::pressed{\n'
            '	font: 700 italic 11pt "Arial";\n'
            '	border: 2px solid rgb(0, 0, 0);\n'
            '	background-color: rgb(170, 170, 255);\n'
            '}\n'
            'QLineEdit{\n'
            '	font: italic 10pt "Arial";\n'
            '	color: rgb(173, 82, 135);\n'
            '	background-color: rgba(68, 71, 90, 100);\n'
            '	border: none;\n'
            '	border-bottom: 2px solid rgb(170, 170, 255);\n'
            '}\n'
            'QLineEdit::hover{\n'
            '	border-bottom: 2px solid rgb(163, 163, 244);\n'
            '}\n'
            'QLineEdit::pressed{\n'
            '	border-bottom: 2px solid rgb(170, 170, 255);\n'
            '}\n'
            'QListWidget{\n'
            '	color: rgb(173, 82, 135);\n'
            '	bor'
            'der-radius: 5%;\n'
            '	background-color: rgb(82, 86, 109);\n'
            '}\n'
            'QProgressBar{\n'
            '	background-color: rgba(255, 255, 255, 0);\n'
            '	color: rgb(68, 71, 90);\n'
            '	border-radius: 5px;\n'
            '}\n'
            'QProgressBar::chunk{\n'
            '    border-radius: 5px;\n'
            '	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.443227, stop:0 rgba(208, 99, 162, 255), stop:0.988636 rgba(170, 163, 239, 255));\n'
            '}\n'
            'QStackedWidget{\n'
            '	background-color: rgba(255, 255, 255, 0);\n'
            '}'
        )
        self.centralwidget = QWidget(Janela)
        self.centralwidget.setObjectName('centralwidget')
        self.centralwidget.setStyleSheet('')
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName('frame')
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.wev_youtube = QWebEngineView(self.frame)
        self.wev_youtube.setObjectName('wev_youtube')
        self.wev_youtube.setGeometry(QRect(0, 0, 400, 600))
        self.wev_youtube.setUrl(QUrl('https://www.youtube.com/'))
        self.wev_youtube.setZoomFactor(0.900000000000000)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName('frame_2')
        self.frame_2.setStyleSheet('')
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.le_link = QLineEdit(self.frame_2)
        self.le_link.setObjectName('le_link')
        self.le_link.setGeometry(QRect(4, 230, 341, 22))
        self.le_link.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.pb_baixar = QPushButton(self.frame_2)
        self.pb_baixar.setObjectName('pb_baixar')
        self.pb_baixar.setGeometry(QRect(162, 270, 75, 24))
        font = QFont()
        font.setFamilies(['Arial'])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.pb_baixar.setFont(font)
        self.cb_formt_aqrv = QComboBox(self.frame_2)
        self.cb_formt_aqrv.addItem('')
        self.cb_formt_aqrv.addItem('')
        self.cb_formt_aqrv.setObjectName('cb_formt_aqrv')
        self.cb_formt_aqrv.setGeometry(QRect(348, 230, 51, 22))
        self.paginas = QStackedWidget(self.frame_2)
        self.paginas.setObjectName('paginas')
        self.paginas.setGeometry(QRect(9, 299, 381, 291))
        self.download_unitario = QWidget()
        self.download_unitario.setObjectName('download_unitario')
        self.l_thumbnail = QLabel(self.download_unitario)
        self.l_thumbnail.setObjectName('l_thumbnail')
        self.l_thumbnail.setGeometry(QRect(20, 50, 341, 211))
        self.l_thumbnail.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.l_thumbnail.setScaledContents(True)
        self.l_thumbnail.setAlignment(Qt.AlignCenter)
        self.l_minutos = QLabel(self.download_unitario)
        self.l_minutos.setObjectName('l_minutos')
        self.l_minutos.setGeometry(QRect(310, 242, 49, 20))
        font1 = QFont()
        font1.setFamilies(['Arial'])
        font1.setPointSize(10)
        font1.setBold(True)
        self.l_minutos.setFont(font1)
        self.l_minutos.setStyleSheet(
            'color: rgb(173, 82, 135);\n'
            'background-color: rgba(255, 255, 255, 0);'
        )
        self.l_minutos.setAlignment(Qt.AlignCenter)
        self.pgsbar_unitario = QProgressBar(self.download_unitario)
        self.pgsbar_unitario.setObjectName('pgsbar_unitario')
        self.pgsbar_unitario.setGeometry(QRect(134, 268, 131, 23))
        self.pgsbar_unitario.setFont(font1)
        self.pgsbar_unitario.setStyleSheet('')
        self.pgsbar_unitario.setValue(0)
        self.pgsbar_unitario.setAlignment(Qt.AlignCenter)
        self.pgsbar_unitario.setTextVisible(True)
        self.pgsbar_unitario.setTextDirection(QProgressBar.TopToBottom)
        self.paginas.addWidget(self.download_unitario)
        self.download_playlist = QWidget()
        self.download_playlist.setObjectName('download_playlist')
        self.lw_playlist_musicas = QListWidget(self.download_playlist)
        self.lw_playlist_musicas.setObjectName('lw_playlist_musicas')
        self.lw_playlist_musicas.setGeometry(QRect(20, 50, 341, 211))
        font2 = QFont()
        font2.setFamilies(['Georgia'])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(True)
        self.lw_playlist_musicas.setFont(font2)
        self.lw_playlist_musicas.setAutoScroll(False)
        self.lw_playlist_musicas.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        self.lw_playlist_musicas.setLayoutMode(QListView.SinglePass)
        self.lw_playlist_musicas.setSpacing(1)
        self.lw_playlist_musicas.setUniformItemSizes(False)
        self.lw_playlist_musicas.setItemAlignment(Qt.AlignHCenter)
        self.paginas.addWidget(self.download_playlist)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName('label')
        self.label.setGeometry(QRect(0, 80, 401, 101))
        self.label.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.label.setPixmap(QPixmap('Ui/img/nome.png'))
        self.label.setScaledContents(True)
        self.label.setOpenExternalLinks(True)
        self.pb_abrir_pasta_download = QPushButton(self.frame_2)
        self.pb_abrir_pasta_download.setObjectName('pb_abrir_pasta_download')
        self.pb_abrir_pasta_download.setGeometry(QRect(1, 574, 20, 24))
        self.pb_abrir_pasta_download.setStyleSheet(
            'QPushButton{\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '	border: 0px solid rgb(40, 42, 54);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	background-color: rgb(163, 163, 244);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	font: 700 italic 11pt "Arial";\n'
            '	border: 2px solid rgb(0, 0, 0);\n'
            '	background-color: rgb(170, 170, 255);\n'
            '}'
        )

        self.horizontalLayout.addWidget(self.frame_2)

        Janela.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela)

        self.paginas.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Janela)

    # setupUi

    def retranslateUi(self, Janela):
        Janela.setWindowTitle(
            QCoreApplication.translate('Janela', 'VYTDownload', None)
        )
        self.pb_baixar.setText(
            QCoreApplication.translate('Janela', 'Baixar', None)
        )
        self.cb_formt_aqrv.setItemText(
            0, QCoreApplication.translate('Janela', 'MP4', None)
        )
        self.cb_formt_aqrv.setItemText(
            1, QCoreApplication.translate('Janela', 'MP3', None)
        )

        self.l_thumbnail.setText('')
        self.l_minutos.setText('')
        # if QT_CONFIG(tooltip)
        self.pb_abrir_pasta_download.setToolTip(
            QCoreApplication.translate(
                'Janela', 'Abrir pasta de download', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.pb_abrir_pasta_download.setText('📁')

    # retranslateUi
