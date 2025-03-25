import commom as cm
import time as tm

def areaPesca():
    try:
        return cm.gui.locateOnScreen('bot_imgs/area_pesca.png', confidence= 0.8)
    except cm.gui.ImageNotFoundException:
        return None

def boiaPescou():
    try:
        return cm.gui.locateOnScreen('bot_imgs/boia_pescou.png', confidence= 0.7)
    except cm.gui.ImageNotFoundException:
        return None

def pesca():
    while True:
        areaLivre = areaPesca()
        boiaPesca = boiaPescou()
        print(boiaPesca)
        if areaLivre is None:
            with cm.gui.hold('shift'):
                cm.gui.press('z')
                tm.sleep(1)
                cm.gui.moveTo(areaLivre)
                cm.gui.click(areaLivre)
                cm.gui.keyUp('shift')
            if boiaPesca is not None:
                tm.sleep(1)
                puxarVara()
        while True:
            is_battle = cm.checarBattleStats()
            meubattle_poke = cm.checarBattleStatsMeuPokemon()
            print(is_battle)
            if is_battle is None:
                cm.targetPokemon()
                print('Achou!')
                if cm.pokemonPreso() is None:
                    cm.callPokemon()
                    cm.atacarPokemon()
                    if meubattle_poke is not None:
                        cm.prenderPokemon()
                        break

def puxarVara():
    with cm.gui.hold('shift'):
        cm.gui.press('z')
        cm.gui.keyUp('shift')                                               