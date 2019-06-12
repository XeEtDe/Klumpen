class Spieler():
    def __init__(self, Name):
        self.Name = Name

First = Spieler("A")

First.A_0 = ([0])
First.A_1 = (1)

import Karten
Liste = [[Karten.Klumpi, Karten.Klumpi.Punkte, Karten.Klumpi.Lebensraum], [Karten.Wald, Karten.Wald.Punkte, Karten.Wald.Punkte], [Karten.Drache]]
def getkey(List):
    return List[0].Name
Liste.sort(key = getkey)
print(Liste)

[0, 1, 2] #3
[3, 4, 5] #3 -> 6