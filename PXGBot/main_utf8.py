import pyautogui as gui
import pesca as fish


def apresentar():
    gui.alert('Olá, seja bem-vindo ao meu programa!')

def opcoes():
    gui.alert('Vamos Pescar')

apresentar()
opcoes()
fish.pesca()    