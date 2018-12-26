#Regeln
def Regeln():
    print("Jeder Spieler erhält jede Runde einige Karten folgender Arten: Lebensräume, Lebewesen und Elemente. Die erhaltenen Karten befinden sich nun in deiner Ablage.")
    print("Lebensräume werden auf dem Feld platziert. Danach kannst du Lebewesen in ihnen leben lassen. Nur diese Lebewesen werden am Ende gewertet.")
    print("Um Lebewesen zu verbessern, kannst du sie mit Elementen oder mit anderen Lebewesen kombinieren. Lebensräume kannst du unter anderem durch das Element Magie verbessern.")
    print("Lebewesen kannst du nur innerhalb des Feldes oder innerhalb der Ablage kombinieren. Lebensräume kannst du auch zwischen Ablage und Feld kombinieren, darfst dafür aber nicht zwei genau gleiche Lebensräume auf dem Feld haben.")
    print("Einige Lebewesen haben Extrafunktionen. Platziere diese Lebewesen zuerst in Lebensräumen auf dem Feld, um diese zu nutzen.")
    print("Allerdings kannst du nur eine dieser Aktionen pro Zug ausführen. Davor kannst du beliebig viele Lebewesen auf dem Feld bewegen.")

    #Vor jeder Reihe von Zügen/pro Runde einmal
    print("\nTippe \"Karten Name 1 + Karten Name 2\" um zwei Karten zu kombinieren. Damit kannst du auch Lebewesen in Lebensräumen auf dem Feld platzieren.")
    print("Tippe den Namen eines Lebensraums in deiner Ablage, um diesen im Feld zu platzieren.")
    print("Vor diesen Aktionen kannst du beliebig viele Lebewesen innerhalb des Feldes bewegen (ebenfalls mit \"+\").")
    print("Für Extrafunktionen, die mit anderen Karten (nicht mit Spielern) interagieren: Um  die Extrafunktion zu nutzen, tippe ein \"+\" hinter deine Eingabe. Wenn beide Karten Extrafunktionen haben, tippe zuerst die, die du nutzen willst.")
    print("Um weitere Regeln zu sehen, tippe \"Regeln\". Um den Zug zu übersprigen, drücke Enter.")

#Ausgabe
def Ausgabe(Ort):
    #Ausgabe von Verbesserungen
    elif Ort == Ende_LW[Spieler]:
        for Karte in CDS:
            CDS[Karte] = False
            if Karte in Ende_LW[Spieler]:
                CDS[Karte] = True

#später für Züge
def Zug(Spieler):
    #Aussetzen?
    if Frost_Dict[Spieler] > 0:
        Frost_Dict[Spieler] -= 1
        print("Du musst diesen Zug aussetzen.")
        Aus = False
        Spieler_Zug = True
    #Input
    while Spieler_Zug == False:
        #Kombi
        elif "+" in Input:
            Add(Input)
        #Schwarzer Trank
        elif Input == "Schwarzer Trank" or Input == "schwarzer Trank" or Input == "Schwarzer trank" or Input== "schwarzer Trank":
            if Schwarzer_Trank in Ablage[Spieler]:
                while True:
                    Gegner = random.choice(Alle_Spieler)
                    if not Spieler == Gegner:
                        break
                print("Ausgewählter Spieler: " + Gegner)
                VG = Verbesserung[Gegner]
                Gegner_LW = []
                for LW in Ablage[Gegner]:
                    if LW in Alle_Lebewesen:
                        Gegner_LW.append(LW)
                Feld_Gegner = Feld[Gegner]
                for LR in Feld_Gegner:
                    for LW in Feld_Gegner[LR]:
                        Gegner_LW.append(LW)
                LW = random.choice(Gegner_LW)
                print("Ausgewähltes Lebewesen:\n")
                if LW in Verbesserung[Gegner]:
                    VGK = VG[LW]
                    LW.Punkte += VGK["Punkte"]
                    LW.Angriff += VGK["Angriff"]
                    LW.Verteidigung += VGK["Verteidigung"]
                    for LR in VGK["Lebensräume"]:
                        LWLR = LW.Lebensraum
                        LWLR.append(LR)
                if Modus == "1":
                    repr(LW)
                elif Modus == "2":
                    str(LW)
                if LW in Verbesserung[Gegner]:
                    VGK = VG[LW]
                    LW.Punkte -= VGK["Punkte"]
                    LW.Angriff -= VGK["Angriff"]
                    LW.Verteidigung -= VGK["Verteidigung"]
                    for LR in VGK["Lebensräume"]:
                        LWLR = LW.Lebensraum
                        LWLR.remove(LR)
                print("\n------->\n")
                if not LW in Verbesserung_Spieler:
                    Counter_Dict[Gegner].update({LW:False})
                    Einmal_Dict[Gegner].update({LW:False})
                    Verbesserung[Gegner].update({LW:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                VGK = VG[LW]
                VGK["Punkte"] -= 5
                VGK["Angriff"] -= 5
                VGK["Verteidigung"] -= 5
                if (LW.Punkte + VGK["Punkte"]) < 0:
                    VGK["Punkte"] = 0 - LW.Punkte
                if (LW.Angriff + VGK["Angriff"]) < 0:
                    VGK["Angriff"] = 0 - LW.Angriff
                if (LW.Verteidigung + VGK["Verteidigung"]) < 0:
                    VGK["Verteidigung"] = 0 - LW.Verteidigung
                LW.Punkte += VGK["Punkte"]
                LW.Angriff += VGK["Angriff"]
                LW.Verteidigung += VGK["Verteidigung"]
                for LR in VGK["Lebensräume"]:
                    LWLR = LW.Lebensraum
                    LWLR.append(LR)
                if Modus == "1":
                    repr(LW)
                elif Modus == "2":
                    str(LW)
                LW.Punkte -= VGK["Punkte"]
                LW.Angriff -= VGK["Angriff"]
                LW.Verteidigung -= VGK["Verteidigung"]
                for LR in VGK["Lebensräume"]:
                    LWLR = LW.Lebensraum
                    LWLR.remove(LR)
                Spieler_Zug = True
                Ablage[Spieler].remove(Schwarzer_Trank)
            else:
                print("Du besitzt diese Karte nicht.")
    #Drachenei brüten
    #Werte minus 1 und Drachenei in Drachen nach einem Zug
    D = False
    for Wert in Drachenei_Dict[Spieler]:
        Drachenei_Dict[Spieler].remove(Wert)
        Wert -= 1
        Drachenei_Dict[Spieler].append(Wert)
        if Wert == 0:
            Drachenei_Dict[Spieler].remove(Wert)
            for LR in Feld_Spieler:
                for LW in Feld_Spieler[LR]:
                    if LW.Name == "Drachenei":
                        Feld_Spieler[LR].remove(LW)
                        for Karte in Alle_Karten:
                            if Karte.Name == "Drache":
                                Feld_Spieler[LR].append(Karte)
                                break
                        D = True
                        break
                if D == True:
                    break
    #Neue Counter für neue Dracheneier
    Counter = 0
    for LR in Feld_Spieler:
        for LW in Feld_Spieler[LR]:
            if LW.Name == "Drachenei":
                Counter += 1
    while Counter > len(Drachenei_Dict[Spieler]):
        Drachenei_Dict[Spieler].append(1)
    #Verbesserung nicht kleiner 0
    Verbesserung_Spieler = Verbesserung[Spieler]
    for Karte in Verbesserung_Spieler:
        VSK = Verbesserung_Spieler[Karte]
        if (Karte.Punkte + VSK["Punkte"]) < 0:
            VSK["Punkte"] = 0 - Karte.Punkte
        if (Karte.Angriff + VSK["Angriff"]) < 0:
            VSK["Angriff"] = 0 - Karte.Angriff
        if (Karte.Verteidigung + VSK["Verteidigung"]) < 0:
            VSK["Verteidigung"] = 0 - Karte.Verteidigung
    #Werteverbesserungskarten
    for WV_Karte in Werteverbesserung_Anzahl[Spieler]:
        Jetzt_Anzahl = 0
        for LR in Feld[Spieler]:
            for LW in Feld_Spieler[LR]:
                if LW == WV_Karte:
                    if (LW == Friedensengel) or (LW == Diebische_Elster):
                        Jetzt_Anzahl += 3
                    else:
                        Jetzt_Anzahl += 1   
        WASK = WAS[WV_Karte] #Werteverbesserung_Anzahl[Spieler[Karte]] -> [0] = Unverbrauchte/Mögliche, [1] = letzte Anzahl
        WASK[0] += (Jetzt_Anzahl - WASK[1])
        WASK[1] = Jetzt_Anzahl
        if WASK[0] < 0 or WASK[1] < 0:
            print("Fehler Werteverbesserungskarten, Dict Werte negativ")
        
#Spielkern
#Runden

while Runden_Counter < Runden:
    #Karten für Runde
    if not Runden_Counter == 1:
        #Auswahlstapel
        if len(Alle_Spieler) <= 5:
            Anzahl_Auswahl_Karten = 2 * len(Alle_Spieler)
        elif len(Alle_Spieler) > 5:
            Anzahl_Auswahl_Karten = 4 * len(Alle_Spieler)
        Auswahl = []
        while Anzahl_Auswahl_Karten > 0:
            Auswahl.append(random.choice(random.choice(Alle_Start_Karten)))
            Anzahl_Auswahl_Karten -= 1
        #zufällige Reihenfolge
        Alle_Spieler_Kopie = Alle_Spieler.copy()
        Reihenfolge = []
        #Marienkäfer Extrafunktion
        Marienkäfer_Dict = {}
        for Spieler in Alle_Spieler:
            Counter = 0
            Feld_Spieler = Feld[Spieler]
            for LR in Feld[Spieler]:
                for LW in Feld_Spieler[LR]:
                    if LW.Name == "Marienkäfer":
                        Counter += 1
            if not Counter == 0:
                Marienkäfer_Dict.update({Spieler:Counter})
        Werte = []
        for Spieler in Marienkäfer_Dict:
            if not Marienkäfer_Dict[Spieler] in Werte:
                Werte.append(Marienkäfer_Dict[Spieler])
        Werte.sort(reverse = True)
        for Wert in Werte:
            Liste = []
            for Spieler in Marienkäfer_Dict:
                if Marienkäfer_Dict[Spieler] == Wert:
                    Liste.append(Spieler)
            S = random.choice(Liste)
            Reihenfolge.append(S)
            Alle_Spieler_Kopie.remove(S)
        while len(Alle_Spieler_Kopie) > 0:
            SP = random.choice(Alle_Spieler_Kopie)
            Reihenfolge.append(SP)
            Alle_Spieler_Kopie.remove(SP)
        #Erklärung
        print("\nAlle Spieler wählen in zufälliger Reihenfolge je eine Karte bis der Auswahlstapel leer ist.")
        print("\nAuswahlstapel:")
        Ausgabe(Auswahl)
        print("\nReihenfolge:")
        for S in Reihenfolge:
            print(S)
        #Auswahl
        while len(Auswahl) > 0:
            #Spieler
            for Spieler in Reihenfolge:
                print("\nAblage:")
                Ausgabe(Ablage[Spieler])
                print("\nFeld:")
                Ausgabe_Feld()
                #bis richtige Eingabe
                while True:
                    Wahl_Karte = input("\n" + Spieler + ": Wähle eine Karte. Tippe dazu ihren Namen.\n")
                    Durchgang_Counter = 0
                    for Karte in Auswahl:
                        Durchgang_Counter += 1
                        #Karte geben und aus Auswahl entfernen
                        if Karte.Name == Wahl_Karte:
                            Ablage[Spieler].append(Karte)
                            Auswahl.remove(Karte)
                            Done = True
                            break
                        #Nicht in Stapel
                        elif Durchgang_Counter == len(Auswahl):
                            print("Die Karte befindet sich nicht im Auswahlstapel.")
                            Done = False
                    #nächster Spieler oder nochmal weil falsch
                    if Done == True:
                        if not len(Auswahl) == 0:
                            print("\nAuswahlstapel:")
                            Ausgabe(Auswahl)
                        break
    #Extrakarten
    Extraprint = False
    for Spieler in Alle_Spieler:
        Feld_Spieler = Feld[Spieler]
        Dict = {}
        for LR in Feld[Spieler]:
            for LW in Feld_Spieler[LR]:
                if LW in Extrakarten:
                    Dict.update({LW:random.choice(Extrakarten[LW])})
        if not Dict == {}:
            if Extraprint == False:
                Extraprint = True
                print("\nExtrakarten\n")
            print(Spieler + ":\n")
            for Karte in Dict:
                Ablage[Spieler].append(Dict[Karte])
                print("durch " + Karte.Name + ":")
                print(Dict[Karte])
            
#Auswertung
#Punkte
if Modus == "1":
    print("Ende\n")
    #Punkte addieren
    Auswertung = {}
    for Spieler in Alle_Spieler:
        MDS = Magisch_Dict[Spieler]
        SDS = Stärker_Dict[Spieler]
        Auswertung.update({Spieler:0})
        #Verbesserung durch LR
        for Karte in MDS:
            MDS[Karte] = 0
        for Karte in SDS:
            SDS[Karte] = 0
        for LR in Feld_Spieler:
            for LW in Feld_Spieler[LR]:
                if "Magisch" in LR.Name:
                    if LW in MDS:
                        MDS[LW] += 1
                    else:
                        MDS.update({LW:1})
                if LW in Stärker_LR[LR.Art]:
                    if not LW in SDS:
                        SDS.update({LW:1})
                    else:
                        SDS[LW] += 1                
        #Lebensraum
        for LR in Feld_Spieler:
            Auswertung[Spieler] += LR.Punkte
            #Lebewesen darin
            for LW in Feld_Spieler[LR]:
                Ende_Punkte = LW.Punkte
                if LW in Verbesserung_Spieler:
                    VSK = Verbesserung_Spieler[LW]
                    Add_Punkte = VSK["Punkte"]
                    if Add_Punkte < 0:
                        Add_Punkte = 0
                    Ende_Punkte += Add_Punkte
                    Verbesserung_Spieler.remove(LW)
                if LW in MDS:
                    if MDS > 0:
                        Ende_Punkte += 1
                        MSD -= 1
                if LW in SDS:
                    if SDS > 0:
                        Ende_Punkte += 2
                        SDS -= 1
                Auswertung[Spieler] += Ende_Punkte
    #Sortieren
    Werte = []
    for Spieler in Auswertung:
        if not Auswertung[Spieler] in Werte:
            Werte.append(Auswertung[Spieler])
    Werte.sort(reverse = True)
    Counter = 0
    #Ausgeben
    for Wert in Werte:
        Counter += 1
        print("\nPlatz " + str(Counter))
        for Spieler in Auswertung:
            if Auswertung[Spieler] == Wert:
                Druck = str(Auswertung[Spieler]) + " Punkte"
                if Wert == 1:
                    Druck = str(Auswertung[Spieler]) + " Punkt"
                print(Spieler + " - " + Druck)
#Kampf
elif Modus == "2":
    print("Ende der Aufbauphase\n")
    print("Kampfphase\n")
    input()
    #Lebewesen auf Feld in Liste
    for Spieler in Alle_Spieler:
        print("\n" + Spieler + "s Lebewesen:")
        for LR in Feld_Spieler:
            for LW in Feld_Spieler[LR]:
                Ende_LW[Spieler].append(LW)
        Ausgabe(Ende_LW[Spieler])
