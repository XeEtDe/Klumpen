import Karten

class Spieler:
    def __init__(self, Name):
        self.Name = Name

First = Spieler("Spieler")

First.A_0 = (Karten.Klumpi, Karten.Klumpi.Punkte, Karten.Klumpi.Lebensraum)
print(First.A_0)