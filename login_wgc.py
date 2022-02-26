from PyQt5 import uic, QtWidgets
import sqlite3


def logout():
    segunda_tela.close()
    primeira_tela.show()


def abre_tela_cadastro():
    tela_cadastro.show()


primeira_tela.show()
app.exec()
