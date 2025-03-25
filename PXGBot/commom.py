import pyautogui as gui
import time as tm
def checarBattleStats():
    try:
        return gui.locateOnScreen('bot_imgs/battle_region.png', confidence= 0.7)
    except gui.ImageNotFoundException:
        return None

def checarBattleStatsMeuPokemon():
    try:
        return gui.locateOnScreen('bot_imgs/battlestats_meupoke.png', confidence= 0.8)
    except gui.ImageNotFoundException:
        return None
def pokemonPreso():
    try:
        return gui.locateOnScreen('bot_imgs/pokemon_preso.png')
    except gui.ImageNotFoundException:
        return None
def soltarPokemon():
    with gui.hold('ctrl'):
        gui.press('1')
        gui.keyUp('ctrl')

def pokemonSolto():
    try:
        return gui.locateOnScreen('bot_imgs/pokemon_solto.png')
    except gui.ImageNotFoundException:
        return None

def prenderPokemon():
    if pokemonSolto is not None:
     gui.click('bot_imgs/pokemon_solto.png')

    
def callPokemon():
    with gui.hold('ctrl'):
        gui.press('1')
        gui.keyUp('ctrl')

def targetPokemon():
    gui.press('tab')
    gui.keyUp('tab')

def atacarPokemon():
    gui.press('1')
    gui.keyUp('1')
    tm.sleep(1)
    gui.press('2')
    gui.keyUp('2')
    tm.sleep(1)
    gui.press('3')
    gui.keyUp('3')
    tm.sleep(1)
    gui.press('4')
    gui.keyUp('4')
    tm.sleep(1)
    gui.press('5')
    gui.keyUp('5')
    tm.sleep(1)
    gui.press('6')
    gui.keyUp('6')
    tm.sleep(1)
    gui.press('7')
    gui.keyUp('7')
    tm.sleep(1)
    gui.press('8')
    gui.keyUp('8')
    tm.sleep(1)


