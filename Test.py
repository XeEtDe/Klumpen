def Sortieren(self):
    Test = len(self.__dict__)
    #Positionen aus __dict__, als Listen [F/A, Nummer, Nummer wenn Lw (Platz im Lr)]
    Positionen = {}
    Neue_Positionen = {}
    for Pos, Karte in self.__dict__.items():
        if not Pos == SP_Name and not Pos == Aussetzen:
            Pos = Pos.spit("_")
            Positionen.update({tuple(Pos):Karte})
    Store = Positionen.copy() #später zum löschen
    #Ablage sortieren
    Num = 0
    for Art_Liste in [Karten.Alle_Lebewesen, Karten.Alle_Lebensraum, Karten.Alle_Elemente]:
        Liste = []
        for Pos, Karte in Positionen.items():
            if Karte[0] in Art_Liste and "A" in Pos:
                Liste.append(Karte)
        Liste.sort(key = lambda Dings: Dings[0].Name)
        for Karte in Liste:
            Neue_Positionen.update({"A_" + str(Num)})
    for Pos in Positionen.copy():
        if "A" in Pos:
            del Positionen[Pos]
    #Feld sortieren
    Lrs = {}
    #Lrs sortieren in eigenem Dict
    for Pos, Karte in Positionen.copy().items():
        if len(Pos) <= 2:
            Lrs.update({tuple(Karte):Pos})
            del Positionen[Pos]
    sorted(Lrs, key = lambda Dings: Dings[0].Name)
    #Lrs und Lws dazu in Neue_Positionen
    for Lr_Num, (Karte, Pos) in enumerate(Lrs.items()):
        Neue_Positionen.update({"F_" + str(Lr_Num):list(Karte)})
        Lw_Num = 0
        for Pos_Lw, Karte_Lw in Positionen:
            if Pos[1] == Pos_Lw[1]:
                Neue_Positionen.update({"F_" + str(Lr_Num) + "_" + str(Lw_Num)})
                Lw_Num += 1
    #Fertig
    Löschen = set(Store.keys()).difference(set(Neue_Positionen.keys()))
    for Pos in Löschen:
        delattr(self, Pos)
    for Pos, Karte in Neue_Positionen.items():
        setattr(self, Pos, Karte)
    if not Test == len(self.__dict__):
        print("!fehlerfehlerfehler!")