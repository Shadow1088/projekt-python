'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.8 #m/s**2 normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #m/s**2 měsíční gravitace
SPEED_OF_LIGHT = 2.99*10**9 #m/s rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #m/s rychlost zvuku při teplotě 20 °C v suchém vzduchu

def convertLightMsKmH():
    """
    Returns conversion from m/s to km/h.
    """
    return SPEED_OF_LIGHT/3.6


def convertSoundMsKmH():
    """
    Returns conversion from m/s to km/h.
    """
    return SPEED_OF_SOUND/3.6



def weightOnTheMoon(weight:int=1):
    """
    Returns your weight on the Moon.
    """
    return weight/EARTH_GRAVITY*MOON_GRAVITY

'''
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.
'''
