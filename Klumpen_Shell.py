#Regeln
def Regeln():
    print("Jeder Spieler erhält jede Runde einige Karten folgender Arten: Lebensräume, Lebewesen und Elemente. Die erhaltenen Karten befinden sich nun in deiner Ablage.")
    print("Lebensräume werden auf dem Feld platziert. Danach kannst du Lebewesen in ihnen leben lassen. Nur diese Lebewesen werden am Ende gewertet.")
    print("Um Lebewesen zu verbessern, kannst du sie mit Elementen oder mit anderen Lebewesen kombinieren. Lebensräume kannst du unter anderem durch das Element Magie verbessern.")
    print("Lebewesen kannst du nur innerhalb des Feldes oder innerhalb der Ablage kombinieren. Lebensräume kannst du auch zwischen Ablage und Feld kombinieren, darfst dafür aber nicht zwei genau gleiche Lebensräume auf dem Feld haben.")
    print("Einige Lebewesen haben Extrafunktionen. Platziere diese Lebewesen zuerst in Lebensräumen auf dem Feld, um diese zu nutzen.")
    print("Allerdings kannst du nur eine dieser Aktionen pro Zug ausführen. Davor kannst du beliebig viele Lebewesen auf dem Feld bewegen.")

#Ausgabe
def Ausgabe(Ort):
    #Ausgabe von Verbesserungen
    elif Ort == Ende_LW[Spieler]:
        for Karte in CDS:
            CDS[Karte] = False
            if Karte in Ende_LW[Spieler]:
                CDS[Karte] = True

def Ausgabe_Feld():
    global Modus
    #Ausgabe von Verbesserungen
    CDS = Counter_Dict[Spieler]
    Feld_Spieler = Feld[Spieler]
    MDS = Magisch_Dict[Spieler]
    SDS = Stärker_Dict[Spieler]
    for Karte in CDS:
        CDS[Karte] = False
        for LR in Feld[Spieler]:
            if Karte == LR or Karte in Feld_Spieler[LR]:
                CDS[Karte] = True
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
    #Ausgabe
    if len(Feld[Spieler]) == 0:
        print("/")
    elif Modus == "1":
        for Karte in Feld_Spieler:
            if "Klein" in Karte.Name:
                print(repr(Karte))
                if Feld_Spieler == []:
                    print("\n")
                Dings = 0
                for LW in Feld_Spieler[Karte]:
                    print("-> " + repr(LW))
                    Dings += 1
                    if Dings == len(Feld_Spieler[Karte]):
                        print("\n")
        for Karte in Feld_Spieler:
            if not "Klein" in Karte.Name and not "Groß" in Karte.Name:
                print(repr(Karte))
                if Feld_Spieler == []:
                    print("\n")
                Dings = 0
                for LW in Feld_Spieler[Karte]:
                    print("-> " + repr(LW))
                    Dings += 1
                    if Dings == len(Feld_Spieler[Karte]):
                        print("\n")
        for Karte in Feld_Spieler:
            if "Groß" in Karte.Name:
                print(repr(Karte))
                if Feld_Spieler == []:
                    print("\n")
                Dings = 0
                for LW in Feld_Spieler[Karte]:
                    print("-> " + repr(LW))
                    Dings += 1
                    if Dings == len(Feld_Spieler[Karte]):
                        print("\n")
    elif Modus == "2":
        for Karte in Feld_Spieler:
            if "Klein" in Karte.Name:
                print(Karte)
                if Feld_Spieler[Karte] == []:
                    print("\n")
                Dings = 0
                for LW in Feld_Spieler[Karte]:
                    print("->")
                    print(LW)
                    Dings += 1
                    if Dings == len(Feld_Spieler[Karte]):
                        print("\n")
        for Karte in Feld_Spieler:
            if not "Klein" in Karte.Name and not "Groß" in Karte.Name:
                print(Karte)
                if Feld_Spieler[Karte] == []:
                    print("\n")
                Dings = 0
                for LW in Feld_Spieler[Karte]:
                    print("->")
                    print(LW)
                    Dings += 1
                    if Dings == len(Feld_Spieler[Karte]):
                        print("\n")
        for Karte in Feld[Spieler]:
            if "Groß" in Karte.Name:
                print(Karte)
                if Feld_Spieler[Karte] == []:
                    print("\n")
                Dings = 0
                for LW in Feld_Spieler[Karte]:
                    print("->")
                    print(LW)
                    Dings += 1
                    if Dings == len(Feld_Spieler[Karte]):
                        print("\n")

#später für Züge
def Zug(Spieler):
    global Aus
    global Spieler_Zug
    Aus = True
    Spieler_Zug = False
    Ablage_Spieler = Ablage[Spieler]
    Feld_Spieler = Feld[Spieler]
    Ablage_Spieler = Ablage[Spieler]
    WAS = Werteverbesserung_Anzahl[Spieler]
    #Ablage und Feld ausgeben
    print("\n\n" + Spieler + "s Zug (" + Str_Übrig + ")")
    print("\nAblage:")
    Ausgabe(Ablage[Spieler])
    print("\nFeld:")
    Ausgabe_Feld()
    #Aussetzen?
    if Frost_Dict[Spieler] > 0:
        Frost_Dict[Spieler] -= 1
        print("Du musst diesen Zug aussetzen.")
        Aus = False
        Spieler_Zug = True
    #Input
    while Spieler_Zug == False:
        Input_ = input("\n")
        Input = Input_.strip()
        #Überspringen/Beenden
        if Input == "":
            Spieler_Zug = True
            Aus = False
        #Regeln
        elif Input == "Regeln":
            Regeln()
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
        #Lebensraum auf Feld
        else:
            Counter_Input = 0
            for Karte in Ablage[Spieler]:
                Counter_Input += 1
                if Input == Karte.Name:
                    if Karte in Alle_Lebensraum:
                        if Karte not in Feld[Spieler]:
                            Ablage[Spieler].remove(Karte)
                            Feld[Spieler].update({Karte:[]})
                            Spieler_Zug = True
                            break
                        else:
                            print("Du kannst nur einmal denselben Lebensraum auf dem Feld haben.")
                            break
                    else:
                        print("Du kannst nur Lebensräume auf dem Feld platzieren.")
                        break
                elif Counter_Input == len(Ablage[Spieler]):
                    print("Du besitzt diese Karte nicht.")
        #Ablage und Feld ausgeben
        if not Aus == False:
            print("\nAblage:")
            Ausgabe(Ablage[Spieler])
            print("\nFeld:")
            Ausgabe_Feld()
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
            
#Kombi
def Add(Karten):
    global Spieler_Zug
    global Spieler
    Ablage_Spieler = Ablage[Spieler]
    Feld_Spieler = Feld[Spieler]
    Neue_Karte = False
    EDS = Einmal_Dict[Spieler]
    for Karte in EDS:
        EDS[Karte] = True
    WAS = Werteverbesserung_Anzahl[Spieler]
    Verbesserung_Spieler = Verbesserung[Spieler]
    Extra = False
    #Karten und Namen
    Karten_Liste = Karten.split("+")
    if len(Karten_Liste) == 3:
        if Karten_Liste[2] == "":
            Extra = True
            Karten_Liste.remove(Karten_Liste[2])
    Name_Karte_1 = Karten_Liste[0].strip()
    Name_Karte_2 = Karten_Liste[1].strip()
    Karte_1 = False
    Karte_2 = False
    for Karte in Alle_Karten:
        if Name_Karte_1 == Karte.Name:
            Karte_1 = Karte
        if Name_Karte_2 == Karte.Name:
            Karte_2 = Karte
    if (not Karte_1 == False) and (not Karte_2 == False):
        Gesuchte_Kombi_1 = Karte_1.Name + "+" + Karte_2.Name
        Gesuchte_Kombi_2 = Karte_2.Name + "+" + Karte_1.Name
        #Ort und Besitz?
        LR_1 = False
        LR_2 = False
        LR_Neu = False
        #Karte_1
        Ort_1 = False
        for Liste in Feld_Spieler:
            if Karte_1 in Feld_Spieler[Liste]:
                LR_1 = Liste
                Ort_1 = Feld_Spieler[Liste]
                break
        if Ort_1 == False:
            if Karte_1 in Feld[Spieler]:
                Ort_1 = Feld[Spieler]
        if Ort_1 == False:
            if Karte_1 in Ablage[Spieler]:
                Ort_1 = Ablage[Spieler]
        #Karte_2
        Ort_2 = False
        #Doppelte Karte/Karte 1 = Karte 2
        if Karte_1 == Karte_2:
            for Liste in Feld_Spieler:
                if Karte_2 in Feld_Spieler[Liste]:
                    if not Ort_1 == Feld_Spieler[Liste]:
                        LR_2 = Liste
                        Ort_2 = Feld_Spieler[Liste]
                        break
                    else:
                        Counter = 0
                        for Krt in Feld_Spieler[Liste]:
                            if Krt == Karte_2:
                                Counter += 1
                        if Counter >= 2:
                            LR_2 = Liste
                            Ort_2 = Feld_Spieler[Liste]
                            break
            if Ort_2 == False:
                if Karte_2 in Feld[Spieler]:
                    if not Ort_1 == Feld[Spieler]:
                        Ort_2 = Feld[Spieler]
                    else:
                        Counter = 0
                        for Krt in Feld[Spieler]:
                            if Krt == Karte_2:
                                Counter += 1
                        if Counter >= 2:
                            Ort_2 = Feld[Spieler]
            if Ort_2 == False:
                if Karte_2 in Ablage[Spieler]:
                    if not Ort_1 == Ablage[Spieler]:
                        Ort_2 = Ablage[Spieler]
                    else:
                        Counter = 0
                        for Krt in Ablage[Spieler]:
                            if Krt == Karte_2:
                                Counter += 1
                        if Counter >= 2:
                            Ort_2 = Ablage[Spieler]
        #Nicht doppelt
        else:
            for Liste in Feld_Spieler:
                if Karte_2 in Feld_Spieler[Liste]:
                    LR_2 = Liste
                    Ort_2 = Feld_Spieler[Liste]
                    break
            if Ort_2 == False:
                if Karte_2 in Feld[Spieler]:
                    Ort_2 = Feld[Spieler]
            if Ort_2 == False:
                if Karte_2 in Ablage[Spieler]:
                    Ort_2 = Ablage[Spieler]
        #Besitz?/andere Fehler
        if len(Karten_Liste) > 2 or len(Karten_Liste) < 2:
            print("Du kannst nur zwei Karten kombinieren.")
        elif Karte_1 == False or Karte_2 == False:
            print("Diese Karten existieren nicht.")
        elif Ort_1 == False or Ort_2 == False:
            print("Du besitzt eine oder beide Karten nicht.")
        #Extrafunktionen
        elif Extra == True:
            Counter = 0
            Reihe = [Karte_1, Karte_2]
            Test = False
            for E_Karte in Reihe:
                Counter += 1
                if E_Karte == Karte_1:
                    Andere_Karte = Karte_2
                    Ort = Ort_1
                    Anderer_Ort = Ort_2
                    Anderer_LR = LR_2
                else:
                    Andere_Karte = Karte_1
                    Ort = Ort_2
                    Anderer_Ort = Ort_1
                    Anderer_LR = LR_1
                if E_Karte in WAS:
                    WASK = WAS[E_Karte]
                #Parasit
                if E_Karte == Parasit:
                    if Andere_Karte in Alle_Lebewesen:
                        if WASK[0] > 0:
                            if not E_Karte in Verbesserung_Spieler:
                                Counter_Dict[Spieler].update({E_Karte:False})
                                Einmal_Dict[Spieler].update({E_Karte:False})
                                Verbesserung_Spieler.update({E_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                            VSK = Verbesserung_Spieler[E_Karte]
                            VSK["Punkte"] += Andere_Karte.Punkte
                            VSK["Angriff"] += Andere_Karte.Angriff
                            VSK["Verteidigung"] += Andere_Karte.Verteidigung
                            if not Andere_Karte in Verbesserung_Spieler:
                                Counter_Dict[Spieler].update({Andere_Karte:False})
                                Einmal_Dict[Spieler].update({Andere_Karte:False})
                                Verbesserung_Spieler.update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                            VSK = Verbesserung_Spieler[Andere_Karte]
                            VSK["Punkte"] -= 4
                            VSK["Angriff"] -= 4
                            VSK["Verteidigung"] -= 4
                            WASK[0] -= 1
                            Spieler_Zug = True
                        else:
                            print("Fähigkeit kann nur einmal angewandt werden, Parasit muss auf dem Feld platziert sein.")
                    else:
                        print("Kann nur die Werte von Lebewesen aufnehmen.")
                #Werteverbesserungskarte
                elif E_Karte in Werteverbesserung_Übersicht:
                    if Andere_Karte in Alle_Lebewesen:
                        if WASK[0] > 0:
                            if not Andere_Karte in Verbesserung_Spieler:
                                Counter_Dict[Spieler].update({Andere_Karte:False})
                                Einmal_Dict[Spieler].update({Andere_Karte:False})
                                Verbesserung_Spieler.update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                            VSK = Verbesserung_Spieler[Andere_Karte]
                            VSK["Punkte"] += Werteverbesserung_Übersicht[E_Karte]
                            VSK["Angriff"] += Werteverbesserung_Übersicht[E_Karte]
                            VSK["Verteidigung"] += Werteverbesserung_Übersicht[E_Karte]
                            WASK[0] -= 1
                            Spieler_Zug = True
                        else:
                            print("Fähigkeit kann nur einmal angewandt werden, Karte muss auf dem Feld platziert sein.")
                    else:
                        print("Kann nur die Werte von Lebewesen verbessern.")
                #Mehr Lebensräume
                elif E_Karte in ExtraLRs:
                    if Andere_Karte in Alle_Lebewesen:
                        if not Ort == Ablage[Spieler]:
                            #Alle?
                            Gesamt_LRs = []
                            for LR in Andere_Karte.Lebensraum:
                                Gesamt_LRs.append(LR)
                            if Andere_Karte in Verbesserung_Spieler:
                                VSK = Verbesserung_Spieler[Andere_Karte]
                                for LR in VSK["Lebensräume"]:
                                    Gesamt_LRs.append(LR)
                            if "Alle" in Gesamt_LRs:
                                print("Dieses Lebewesen kann bereits in allen Lebensräumen leben.")
                            else:
                                #Zufall
                                if ExtraLRs[E_Karte] == "Zufall":
                                    LRs_Kopie = LRs.copy()
                                    for LR in Gesamt_LRs:
                                        if not LR == "Wonderland":
                                            LRs_Kopie.remove(LR)
                                    Neu = random.choice(LRs_Kopie)
                                else:
                                    Neu = ExtraLRs[E_Karte]
                                if not Andere_Karte in Verbesserung_Spieler:
                                    Counter_Dict[Spieler].update({Andere_Karte:False})
                                    Einmal_Dict[Spieler].update({Andere_Karte:False})
                                    Verbesserung_Spieler.update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                                VSK = Verbesserung_Spieler[Andere_Karte]
                                VSK["Lebensräume"].append(Neu)
                                Test_Liste = []
                                for LR in Andere_Karte.Lebensraum:
                                    if not LR == "Wonderland":
                                        Test_Liste.append(LR)
                                for LR in VSK["Lebensräume"]:
                                    Test_Liste.append(LR)
                                if len(Test_Liste) >= 4:
                                    VSK["Lebensräume"] = ["Alle"]
                        else:
                            print("Platziere Lebewesen auf dem Feld, um ihre Extrafunktion zu nutzen.")
                    else:
                        print("Kann nur auf Lebewesen angewandt werden.")
                #Friedensengel
                elif E_Karte == Friedensengel:
                    if Andere_Karte in Alle_Lebensraum:
                        if WASK[0] > 0:
                            if "Klein" in Andere_Karte.Name:
                                if "Magisch" in Andere_Karte.Name:
                                    Neue_Karte = Magisches_Kleines_Wonderland
                                else:
                                    Neue_Karte = Kleines_Wonderland
                            elif "Groß" in Andere_Karte.Name:
                                if "Magisch" in Andere_Karte.Name:
                                    Neue_Karte = Magisches_Großes_Wonderland
                                else:
                                    Neue_Karte = Großes_Wonderland
                            else:
                                if "Magisch" in Andere_Karte.Name:
                                    Neue_Karte = Magisches_Wonderland
                                else:
                                    Neue_Karte = Wonderland
                            if Andere_Karte in Feld[Spieler]:
                                Feld_Spieler.update({Neue_Karte:[]})
                                for LW in Feld_Spieler[Andere_Karte]:
                                    Feld_Spieler[Neue_Karte].append(LW)
                                del Feld_Spieler[Andere_Karte]
                            elif Andere_Karte in Ablage[Spieler]:
                                Ablage[Spieler].append(Neue_Karte)
                                Ablage[Spieler].remove(Andere_Karte)
                            Spieler_Zug = True
                            WASK[0] -= 1
                        else:
                            print("Muss auf dem Feld platziert sein und kann nur 3 Mal angewandt werden.")
                    else:
                        print("Extrafunktion kann nur auf Lebensräume angewandt werden.")
                #Zauberer
                elif E_Karte == Zauberer:
                    if Andere_Karte in Alle_Elemente:
                        if not Ort == Ablage[Spieler]:
                            for Trank in Tränke_Kombi:
                                if Andere_Karte in Tränke_Kombi[Trank]:
                                    Neue_Karte = Trank
                                    break
                            Ablage_Spieler.append(Neue_Karte)
                            Ablage_Spieler.remove(Andere_Karte)
                            Spieler_Zug = True
                        else:
                            print("Platziere den Zauberer im Feld um seine Funktion zu nutzen.")
                    else:
                        print("Zauberer kann nur Elemente in Tränke verwandeln.")
                #Dunkler Magier
                elif E_Karte == Dunkler_Magier:
                    if Andere_Karte in Alle_Elemente:
                        if not Ort == Ablage[Spieler]:
                            for Gift in Gifte_Kombi:
                                if Andere_Karte in Gifte_Kombi[Gift]:
                                    Neue_Karte = Gift
                                    break
                            Ablage_Spieler.append(Neue_Karte)
                            Ablage_Spieler.remove(Andere_Karte)
                            Spieler_Zug = True
                        else:
                            print("Platziere den Dunklen Magier im Feld um seine Funktion zu nutzen.")
                    else:
                        print("Dunkler Magier kann nur Elemente in Gifte verwandeln.")
                #Urwolf
                elif E_Karte == Urwolf:
                    if Andere_Karte in Alle_Lebewesen:
                        if WASK[0] > 0:
                            Weiter = True
                            if Andere_Karte.Punkte > Werwolf.Punkte:
                                print("Die Karte ist bereits besser als eine Werwolf-Karte.")
                                Input = input("Trotzdem tauschen?")
                                if Input == "Ja" or input == "ja":
                                    Weiter = True
                                else:
                                    Weiter = False
                            if not Anderer_Ort == Ablage[Spieler]:
                                if not Anderer_LR.Art == "Wald":
                                    print("Der Lebensraum ist für einen Werwolf nicht geeignet. Wähle ein Lebewesen in einem Wald oder in der Ablage.")
                                    Weiter = False
                            if Weiter == True:
                                Anderer_Ort.remove(Andere_Karte)
                                Anderer_Ort.append(Werwolf)
                                if Andere_Karte in Verbesserung_Spieler:
                                    if not Werwolf in Verbesserung_Spieler:
                                        Counter_Dict[Spieler].update({Werwolf:False})
                                        Einmal_Dict[Spieler].update({Werwolf:False})
                                        Verbesserung_Spieler.update({Werwolf:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                                    VSK = Verbesserung_Spieler[Werwolf]
                                    VSK["Punkte"] += Werteverbesserung_Übersicht[Andere_Karte]
                                    VSK["Angriff"] += Werteverbesserung_Übersicht[Andere_Karte]
                                    VSK["Verteidigung"] += Werteverbesserung_Übersicht[Andere_Karte]
                                    del Verbesserung_Spieler[Andere_Karte]
                                Spieler_Zug = True
                                WASK[0] -= 1
                        else:
                            print("Kann nur einmal im Spiel angewandt werden, Karte muss auf dem Feld platziert sein.")
                    else:
                        print("Kann nur auf Lebewesen angewandt werden.")
                else:
                    Test = True
                if Counter == 1 and Test == False:
                    break
                elif Counter == 2 and Test == True:
                    print("Keine der Karten hat eine Extrafunktion.")
        #LW bewegen
        elif (Karte_1 in Alle_Lebensraum and Karte_2 in Alle_Lebewesen) or (Karte_2 in Alle_Lebensraum and Karte_1 in Alle_Lebewesen):
            if Karte_1 in Alle_Lebensraum:
                LR_Karte = Karte_1
                LW_Karte = Karte_2
            else:
                LR_Karte = Karte_2
                LW_Karte = Karte_1
            #LR auf Feld
            Feld_Test = False
            if LR_Karte in Feld_Spieler:
                Feld_Test = True
            else:
                print("Platziere den Lebensraum erst auf dem Feld.")
            #Größe
            Voll_Test = False
            Art_Test = False
            if Feld_Test == True:
                Alte_LW = Feld_Spieler[LR_Karte]
                Größe = LR_Karte.Größe
                if LR_Karte in EDS:
                    if EDS[LR_Karte] == True:
                        Add_Größe = Verbesserung_Spieler[LR_Karte]
                        Größe = LR_Karte.Größe + Add_Größe                    
                if len(Alte_LW) < Größe:
                    Voll_Test = True
                else:
                    print("Dieser Lebensraum ist bereits voll.")
                #Art
                Art_Test = False
                Zusatz_LR = []
                if LW_Karte in EDS:
                    if EDS[LW_Karte] == True:
                        VSK = Verbesserung_Spieler[LW_Karte]
                        for LR in VSK["Lebensräume"]:
                            Zusatz_LR.append(LR)
                for LR in LW_Karte.Lebensraum:
                    if LR == LR_Karte.Art or LR == "Alle":
                        Art_Test = True
                        break
                for LR in Zusatz_LR:
                    if LR == LR_Karte.Art or LR == "Alle":
                        Art_Test = True
                        break
                if Art_Test == False:
                    print("Dieser Lebensraum ist für das Lebewesen nicht geeignet.")
            #Hinzufügen?
            if Voll_Test == True and Art_Test == True and Feld_Test == True:
                if LW_Karte in Ablage_Spieler:
                    Spieler_Zug = True
                if LW_Karte == Karte_1:
                    A = Karte_1
                    B = Karte_2
                    Ort = Ort_1                    
                elif LW_Karte == Karte_2:
                    A = Karte_2
                    B = Karte_1
                    Ort = Ort_2
                Feld_Spieler[B].append(A)
                if A in Ablage[Spieler]:
                    Ablage[Spieler].remove(A)
                else:
                    Ort.remove(A)
        #Tränke
        elif "Trank" in Karte_1.Name or "Trank" in Karte_2.Name:
            if "Trank" in Karte_1.Name:
                Trank_Karte = Karte_1
                Andere_Karte = Karte_2
            else:
                Trank_Karte = Karte_2
                Andere_Karte = Karte_1
            #Lebensraum-Tränke
            if "Lebensraum" in Trank_Karte.Beschreibung or "Duftender Trank" == Trank_Karte.Name:
                if Andere_Karte in Alle_Lebensraum:
                    #Vergrößerungs-Trank
                    if Trank_Karte.Name == "Vergrößerungs-Trank":
                        if not Andere_Karte in Verbesserung_Spieler:
                            Counter_Dict[Spieler].update({Andere_Karte:False})
                            Einmal_Dict[Spieler].update({Andere_Karte:False})
                            Verbesserung_Spieler.update({Andere_Karte:0})
                        Verbesserung_Spieler[Andere_Karte] += 1
                        Spieler_Zug = True
                        Ablage[Spieler].remove(Trank_Karte)
                    #Duftender Trank
                    elif Trank_Karte.Name == "Duftender Trank":
                        if "Klein" in Andere_Karte.Name:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Magisches_Kleines_Wonderland
                            else:
                                Neue_Karte = Kleines_Wonderland
                        elif "Groß" in Andere_Karte.Name:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Magisches_Großes_Wonderland
                            else:
                                Neue_Karte = Großes_Wonderland
                        else:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Magisches_Wonderland
                            else:
                                Neue_Karte = Wonderland
                        if Andere_Karte in Feld[Spieler]:
                            Feld_Spieler.update({Neue_Karte:[]})
                            for LW in Feld_Spieler[Andere_Karte]:
                                Feld_Spieler[Neue_Karte].append(LW)
                            del Feld_Spieler[Andere_Karte]
                        elif Andere_Karte in Ablage[Spieler]:
                            Ablage[Spieler].append(Neue_Karte)
                            Ablage[Spieler].remove(Andere_Karte)
                        Spieler_Zug = True
                        Ablage[Spieler].remove(Trank_Karte)
                else:
                    print("Du kannst diesen Trank nur auf Lebensräume anwenden.")
            #Lebewesen-Tränke     
            elif "Lebewesen" in Trank_Karte.Beschreibung:
                if Andere_Karte in Alle_Lebewesen:
                    Mehr_LRs_Tränke = ["Heißer Trank", "Wässriger Trank", "Matschiger Trank", "Blubbernder Trank", "Verkohlter Trank"]
                    Werte_Tränke = ["Güldener Trank", "Level-Up Trank", "Glitzernder Trank", "Himmlischer Trank"]
                    #Mehr LR Tränke
                    if Trank_Karte.Name in Mehr_LRs_Tränke:
                        if Trank_Karte.Name == "Heißer Trank":
                            LR = "Wüste"
                        elif Trank_Karte.Name == "Wässriger Trank":
                            LR = "See"
                        elif Trank_Karte.Name == "Matschiger Trank":
                            LR = "Wald"
                        elif Trank_Karte.Name == "Blubbernder Trank":
                            LR = "Berge"
                        elif Trank_Karte.Name == "Verkohlter Trank":
                            LR = "Alle"
                        if not Andere_Karte in Verbesserung_Spieler:
                            Counter_Dict[Spieler].update({Andere_Karte:False})
                            Einmal_Dict[Spieler].update({Andere_Karte:False})
                            Verbesserung_Spieler.update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                        VSK = Verbesserung_Spieler[Andere_Karte]
                        if not LR in VSK["Lebensräume"]:
                            VSK["Lebensräume"].append(LR)
                        Spieler_Zug = True
                        Ablage[Spieler].remove(Trank_Karte)
                    #Werte Tränke
                    elif Trank_Karte.Name in Werte_Tränke:
                        if Trank_Karte.Name == "Güldener Trank":
                            Wert = 3
                        elif Trank_Karte.Name == "Level-Up Trank":
                            Wert = 5
                        elif Trank_Karte.Name == "Glitzernder Trank":
                            Wert = 7
                        elif Trank_Karte.Name == "Himmlischer Trank":
                            Wert = 10
                        if not Andere_Karte in Verbesserung_Spieler:
                            Counter_Dict[Spieler].update({Andere_Karte:False})
                            Einmal_Dict[Spieler].update({Andere_Karte:False})
                            Verbesserung_Spieler.update({Andere_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                        VSK = Verbesserung_Spieler[Andere_Karte]
                        VSK["Punkte"] += Wert
                        VSK["Angriff"] += Wert
                        VSK["Verteidigung"] += Wert
                        Spieler_Zug = True
                        Ablage[Spieler].remove(Trank_Karte)
                    #Dolly Trank
                    elif Trank_Karte.Name == "Dolly Trank":
                        Ablage[Spieler].append(Andere_Karte)
                        Spieler_Zug = True
                        Ablage[Spieler].remove(Trank_Karte)
                else:
                    print("Du kannst diesen Trank nur auf Lebenwesen anwenden.")
        #Schleifen-Start/Kombi oder nicht        
        else:
            Counter_Add = 0
            for Karte in Alle_Karten:
                Counter_Add += 1
                #Kombi
                if Gesuchte_Kombi_1 in Karte.Kombi or Gesuchte_Kombi_2 in Karte.Kombi:
                    Neue_Karte = Karte
                    #LR
                    if Karte_1 in Alle_Lebensraum or Karte_2 in Alle_Lebensraum:
                        if Karte_1 in Alle_Lebensraum:
                            LR_Karte = Karte_1
                            Andere_Karte = Karte_2
                        else:
                            LR_Karte = Karte_2
                            Andere_Karte = Karte_1
                        #LR + LR
                        if Andere_Karte in Alle_Lebensraum:
                            #min. eine Feld
                            if Ort_1 == Feld_Spieler or Ort_2 == Feld_Spieler:
                                Neue_LW = []
                                if Ort_1 == Feld_Spieler:
                                    LW_1 = Feld_Spieler[Karte_1]
                                    for LW in LW_1:
                                        Neue_LW.append(LW)
                                    del Feld_Spieler[Karte_1]
                                else:
                                    Ablage_Spieler.remove(Karte_1)
                                if Ort_2 == Feld_Spieler:
                                    LW_2 = Feld_Spieler[Karte_2]
                                    for LW in LW_2:
                                        Neue_LW.append(LW)
                                    del Feld_Spieler[Karte_2]
                                else:
                                    Ablage_Spieler.remove(Karte_2)
                                Feld_Spieler.update({Neue_Karte:[]})
                                if not Neue_LW == []:
                                    for LW in Neue_LW:
                                        Feld_Spieler[Neue_Karte].append(LW)
                                Spieler_Zug = True
                                break
                            #beide Ablage
                            elif Ort_1 == Ablage_Spieler and Ort_2 == Ablage_Spieler:
                                Ablage_Spieler.remove(Karte_1)
                                Ablage_Spieler.remove(Karte_2)
                                Ablage_Spieler.append(Neue_Karte)
                                Spieler_Zug = True
                                break
                        #LR + E
                        elif Andere_Karte in Alle_Elemente:
                            #LR in Feld
                            if LR_Karte in Feld_Spieler:
                                Feld_Spieler.update({Neue_Karte:[]})
                                for LW in Feld_Spieler[LR_Karte]:
                                    Feld_Spieler[Neue_Karte].append(LW)
                                del Feld_Spieler[LR_Karte]
                                Ablage_Spieler.remove(Andere_Karte)
                                Spieler_Zug = True
                                break
                            #LR in Ablage
                            elif LR_Karte in Ablage_Spieler:
                                Ablage_Spieler.remove(Karte_1)
                                Ablage_Spieler.remove(Karte_2)
                                Ablage_Spieler.append(Neue_Karte)
                                Spieler_Zug = True
                                break
                    #LW
                    elif Karte_1 in Alle_Lebewesen or Karte_2 in Alle_Lebewesen:
                        if Karte_1 in Alle_Lebewesen:
                            LW_Karte = Karte_1
                            Andere_Karte = Karte_2
                        else:
                            LW_Karte = Karte_2
                            Andere_Karte = Karte_1
                        #LW + LW
                        if Andere_Karte in Alle_Lebewesen:
                            #beide Ablage oder beide selber LR
                            if Ort_1 == Ort_2:
                                Ort_1.remove(Karte_1)
                                Ort_2.remove(Karte_2)
                                Ort_1.append(Neue_Karte)
                                Spieler_Zug = True
                                break
                            #unterschiedliche LRs
                            else:
                                #Falsch
                                if LR_1 == False or LR_2 == False:
                                    print("Du kannst nur innerhalb des Feldes oder der Ablage kombinieren.")
                                    break
                                #Ort/geeigneter LR
                                Fertig = False
                                Lebensräume = []
                                for LR in Neue_Karte.Lebensraum:
                                    Lebensräume.append(LR)
                                if Neue_Karte in EDS:
                                    if EDS[Neue_Karte] == True:
                                        VSK = Verbesserung_Spieler[Neue_Karte]
                                        for LR in VSK["Lebensräume"]:
                                            Lebensräume.append(LR)
                                for LR in Lebensräume:
                                    if LR == LR_1.Art or LR == "Alle":
                                        Ort_1.append(Neue_Karte)
                                        Ort_1.remove(Karte_1)
                                        Ort_2.remove(Karte_2)
                                        Fertig = True
                                        Spieler_Zug = True
                                        LR_Neu = LR_1
                                        break
                                    elif LR == LR_2.Art:
                                        Ort_2.append(Neue_Karte)
                                        Ort_1.remove(Karte_1)
                                        Ort_2.remove(Karte_2)
                                        Fertig = True
                                        Spieler_Zug = True
                                        LR_Neu = LR_2
                                        break
                                if Spieler_Zug == True:
                                    break
                                if Fertig == False:
                                    print("Keiner der beiden Lebensräume ist geeignet für das neue Lebewesen.")
                                    break
                        #LW + E
                        elif Andere_Karte in Alle_Elemente:
                            #in Ablage
                            if LW_Karte in Ablage_Spieler:
                                Ablage_Spieler.remove(LW_Karte)
                                Ablage_Spieler.remove(Andere_Karte)
                                Ablage_Spieler.append(Neue_Karte)
                                Spieler_Zug = True
                                break
                            #LW auf Feld/in LR
                            else:
                                Lebensräume = []
                                for LR in Neue_Karte.Lebensraum:
                                    Lebensräume.append(LR)
                                if Neue_Karte in EDS:
                                    if EDS[Neue_Karte] == True:
                                        VSK = Verbesserung_Spieler[Neue_Karte]
                                        for LR in VSK["Lebensräume"]:
                                            Lebensräume.append(LR)
                                if LW_Karte == Karte_1:
                                    for LR in Lebensräume:
                                        if LR == LR_1.Art or LR == "Alle":
                                            Ort_1.append(Neue_Karte)
                                            Ort_1.remove(Karte_1)
                                            Ablage_Spieler.remove(Karte_2)
                                            Spieler_Zug = True
                                            LR_Neu = LR_1
                                            break
                                    if Spieler_Zug == False:
                                        print("Der Lebensraum ist nicht geeignet für das neue Lebewesen.")
                                        break
                                    break
                                elif LW_Karte == Karte_2:
                                    for LR in Lebensräume:
                                        if LR == LR_2.Art or LR == "Alle":
                                            Ort_2.append(Neue_Karte)
                                            Ort_2.remove(Karte_2)
                                            Ablage_Spieler.remove(Karte_2)
                                            Spieler_Zug = True
                                            LR_Neu = LR_2
                                            break
                                    if Spieler_Zug == False:
                                        print("Der Lebensraum ist nicht geeignet für das neue Lebewesen.")
                                        break
                                    break
                    #E + E
                    elif Karte_1 in Alle_Elemente and Karte_2 in Alle_Elemente:
                        Ablage[Spieler].append(Neue_Karte)
                        Ablage[Spieler].remove(Karte_1)
                        Ablage[Spieler].remove(Karte_2)
                        Spieler_Zug = True
                        break
                #Keine Kombi möglich
                elif Counter_Add == len(Alle_Karten):
                    print("Diese Karten lassen sich nicht kombinieren.")
            #Verbesserungen
            if Spieler_Zug == True:
                #Weitergabe Verbesserungen
                if Neue_Karte in Alle_Lebensraum:
                    Counter = 0
                    if Karte_1 in Alle_Lebensraum and Karte_1 in Verbesserung_Spieler:
                        Counter += Verbesserung_Spieler[Karte_1]
                        del Verbesserung_Spieler[Karte_1]
                    if Karte_2 in Alle_Lebensraum and Karte_2 in Verbesserung_Spieler:
                        Counter += Verbesserung_Spieler[Karte_2]
                        del Verbesserung_Spieler[Karte_1]
                    if not Counter == 0:
                        if not Neue_Karte in Verbesserung_Spieler:
                            Counter_Dict[Spieler].update({Neue_Karte:False})
                            Einmal_Dict[Spieler].update({Neue_Karte:False})
                            Verbesserung_Spieler.update({Neue_Karte:0})
                        Verbesserung_Spieler[Neue_Karte] += Counter
                elif Neue_Karte in Alle_Lebewesen:
                    Counter_P = 0
                    Counter_A = 0
                    Counter_V = 0
                    if Karte_1 in Alle_Lebewesen and Karte_1 in Verbesserung_Spieler:
                        VSK = Verbesserung_Spieler[Karte_1]
                        Counter_P += VSK["Punkte"]
                        Counter_A += VSK["Angriff"]
                        Counter_V += VSK["Verteidigung"]
                        del Verbesserung_Spieler[Karte_1]
                    if Karte_2 in Alle_Lebewesen and Karte_2 in Verbesserung_Spieler:
                        VSK = Verbesserung_Spieler[Karte_2]
                        Counter_P += VSK["Punkte"]
                        Counter_A += VSK["Angriff"]
                        Counter_V += VSK["Verteidigung"]
                        del Verbesserung_Spieler[Karte_2]
                    if not (Counter_P == 0 and Counter_A == 0 and Counter_V == 0):
                        if not Neue_Karte in Verbesserung_Spieler:
                            Counter_Dict[Spieler].update({Neue_Karte:False})
                            Einmal_Dict[Spieler].update({Neue_Karte:False})
                            Verbesserung_Spieler.update({Neue_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                        VSK = Verbesserung_Spieler[Neue_Karte]
                        VSK["Punkte"] += Counter_P
                        VSK["Angriff"] += Counter_A
                        VSK["Verteidigung"] += Counter_V
    #Extra: Aktion mit anderem Spieler oder Joker
    elif (not Karte_1 == False) or (not Karte_2 == False):
        global Aus
        if not Karte_1 == False:
            E_Karte = Karte_1
            Andere_Name = Name_Karte_2
        else:
            E_Karte = Karte_2
            Andere_Name = Name_Karte_1
        Gegner = None
        for SP in Alle_Spieler:
            if SP == Andere_Name:
                Gegner = SP
        if Gegner == None:
            #Joker
            if E_Karte == Joker:
                WASK = WAS[Joker]
                if WASK[0] > 0:
                    Neue_Karte = None
                    if Andere_Name == "Lebewesen" or Andere_Name == "lebewesen":
                        Neue_Karte = random.choice(Start_Lebewesen)
                    elif Andere_Name == "Lebensraum" or Andere_Name == "lebensraum":
                        Neue_Karte = random.choice(Start_Lebensraum)
                    elif Andere_Name == "Element" or Andere_Name == "element":
                        Neue_Karte = random.choice(Start_Elemente)
                    if Neue_Karte == None:
                        print("Wähle zwischen Element, Lebewesen und Lebensraum.")
                    else:
                        Ablage[Spieler].append(Neue_Karte)
                        print("Neue Karte:\n")
                        if not Neue_Karte in Start_Elemente:
                            if Modus == "1":
                                print(repr(Neue_Karte))
                            elif Modus == "2":
                                print(str(Neue_Karte))
                        else:
                            print(Neue_Karte)
                        Spieler_Zug = True
                        Aus = False
                        WASK[0] -= 1
                else:
                    print("Kann nur einmal pro Runde angewandt werden, Karte muss auf dem Feld platziert sein.")
            else:
                print("Eine oder beide Karten existieren nicht.")
        else:
            #Aktion mit anderem Spieler
            VG = Verbesserung[Gegner]
            EDG = Einmal_Dict[Gegner]
            for Karte in EDG:
                EDG[Karte] = True
            #Gifte und Gefrorener Trank
            if "Gift" in E_Karte.Name or E_Karte.Name == "Gefrorener Trank":
                Werte_Gifte = [Elementares_Gift, Pampiges_Gift, Trügerisches_Gift, Blutiges_Gift]
                Aussetzen_Gifte = [Magisches_Gift, Lähmendes_Gift, Gefrorener_Trank, Eisiges_Gift]
                Zerstörungs_Gifte = [Reines_Gift, Gift_des_Vergessens]
                VG = Verbesserung[Gegner]
                #Werte Gifte
                if E_Karte in Werte_Gifte:
                    if E_Karte == Werte_Gifte[0]:
                        Wert = 3
                    elif E_Karte == Werte_Gifte[1]:
                        Wert = 5
                    elif E_Karte == Werte_Gifte[2]:
                        Wert = 7
                    elif E_Karte == Werte_Gifte[3]:
                        Wert = 10
                    Gegner_LW = []
                    for LW in Ablage[Gegner]:
                        if LW in Alle_Lebewesen:
                            Gegner_LW.append(LW)
                    Feld_Gegner = Feld[Gegner]
                    for LR in Feld_Gegner:
                        for LW in Feld_Gegner[LR]:
                            Gegner_LW.append(LW)
                    LW = random.choice(Gegner_LW)
                    print("Spieler: " + Gegner)
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
                        print(repr(Z_Karte))
                    elif Modus == "2":
                        print(str(Z_Karte))
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
                    VGK["Punkte"] -= Wert
                    VGK["Angriff"] -= Wert
                    VGK["Verteidigung"] -= Wert
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
                        print(repr(Z_Karte))
                    elif Modus == "2":
                        print(str(Z_Karte))
                    LW.Punkte -= VGK["Punkte"]
                    LW.Angriff -= VGK["Angriff"]
                    LW.Verteidigung -= VGK["Verteidigung"]
                    for LR in VGK["Lebensräume"]:
                        LWLR = LW.Lebensraum
                        LWLR.remove(LR)
                    Spieler_Zug = True
                    Ablage[Spieler].remove(E_Karte)
                    Aus = False
                #Aussetzen Gifte
                elif E_Karte in Aussetzen_Gifte:
                    if E_Karte == Aussetzen_Gifte[0]:
                        Wert = 1
                    elif E_Karte == Aussetzen_Gifte[1] or E_Karte == Aussetzen_Gifte[2]:
                        Wert = 3
                    elif E_Karte == Aussetzen_Gifte[3]:
                        Wert = 5
                    Frost_Dict[Gegner] += Wert
                    if Wert == 1:
                        Druck = "einen Zug"
                    else:
                        Druck = str(Wert) + " Züge"
                    print("\n" + Gegner + " setzt " + Druck + " aus.\n")
                    Spieler_Zug = True
                    Ablage[Spieler].remove(E_Karte)
                    Aus = False
                #Zerstörungs Gifte
                elif E_Karte in Zerstörungs_Gifte:
                    Gegner_LW = []
                    for LW in Ablage[Gegner]:
                        if (LW in Alle_Lebewesen) and (LW not in Gegner_LW):
                            Gegner_LW.append(LW)
                    Feld_Gegner = Feld[Gegner]
                    for LR in Feld_Gegner:
                        for LW in Feld_Gegner[LR]:
                            if LW not in Gegner_LW:
                                Gegner_LW.append(LW)
                    if Gegner_LW == []:
                        print("Dieser Spieler besitzt keine Lebewesen.")
                    else:
                        LW_Dict = {}
                        for LW in Gegner_LW:
                            LW_Dict.update({LW:LW.Punkte})
                            if LW in Verbesserung[Gegner] and EDG[LW] == True:
                                VGK = VG[LW]
                                LW_Dict[LW] += VGK["Punkte"]
                                EDG[LW] = False
                        Werte_Liste = []
                        for LW in LW_Dict:
                            Werte_Liste.append(LW_Dict[LW])
                        Werte_Liste.sort()
                        if E_Karte == Zerstörungs_Gifte[0]:
                            for Karte in LW_Dict:
                                if Werte_Liste[0] == LW_Dict[Karte]:
                                    Z_Karte = Karte
                                    break
                        elif E_Karte == Zerstörungs_Gifte[1]:
                            for Karte in LW_Dict:
                                if Werte_Liste[-1] == LW_Dict[Karte]:
                                    Z_Karte = Karte
                                    break
                        Test = False
                        for Karte in Ablage[Gegner]:
                            if Karte == Z_Karte:
                                Ablage[Gegner].remove(Z_Karte)
                                Test = True
                                break
                        if Test == False:
                            for LR in Feld[Gegner]:
                                for LW in Feld_Gegner[LR]:
                                    if LW == Z_Karte:
                                        Feld_Gegner[LR].remove(Z_Karte)
                                        Test = True
                                        break
                                if Test == True:
                                    break
                        Counter = 0
                        for LW in Gegner_LW:
                            if LW == Z_Karte:
                                Counter += 1
                        print("Spieler: " + Gegner)
                        print("Ausgewähltes Lebewesen:\n")
                        if Z_Karte in Verbesserung[Gegner] and Counter == 1:
                            #Verbesserungen enfernen
                            CDG = Counter_Dict[Gegner]
                            del CDG[Z_Karte]
                            del EDG[Z_Karte]
                            del VG[Z_Karte]                            
                            #Verbesserungen für print
                            VGK = VG[Z_Karte]
                            Z_Karte.Punkte += VGK["Punkte"]
                            Z_Karte.Angriff += VGK["Angriff"]
                            Z_Karte.Verteidigung += VGK["Verteidigung"]
                            for LR in VGK["Lebensräume"]:
                                LWLR = Z_Karte.Lebensraum
                                LWLR.append(LR)
                        if Modus == "1":
                            print(repr(Z_Karte))
                        elif Modus == "2":
                            print(str(Z_Karte))
                        if Z_Karte in Verbesserung[Gegner] and Counter == 1:
                            VGK = VG[Z_Karte]
                            Z_Karte.Punkte -= VGK["Punkte"]
                            Z_Karte.Angriff -= VGK["Angriff"]
                            Z_Karte.Verteidigung -= VGK["Verteidigung"]
                            for LR in VGK["Lebensräume"]:
                                LWLR = Z_Karte.Lebensraum
                                LWLR.remove(LR)
                        print("\nWurde entfernt.")
                        Spieler_Zug = True
                        Ablage[Spieler].remove(E_Karte)
                        Aus = False
            #Diebische Elster
            elif E_Karte == Diebische_Elster:
                WASK = WAS[Diebische_Elster]
                if WASK[0] > 0:
                    Gegner_LW = []
                    for LW in Ablage[Gegner]:
                        if (LW in Alle_Lebewesen) and (LW not in Gegner_LW):
                            Gegner_LW.append(LW)
                    Feld_Gegner = Feld[Gegner]
                    for LR in Feld_Gegner:
                        for LW in Feld_Gegner[LR]:
                            if LW not in Gegner_LW:
                                Gegner_LW.append(LW)
                    if Gegner_LW == []:
                        print("Dieser Spieler besitzt keine Lebewesen.")
                    else:
                        LW_Dict = {}
                        for LW in Gegner_LW:
                            LW_Dict.update({LW:LW.Punkte})
                            if LW in Verbesserung[Gegner] and EDG[LW] == True:
                                VGK = VG[LW]
                                LW_Dict[LW] += VGK["Punkte"]
                                EDG[LW] = False
                        Werte_Liste = []
                        for LW in LW_Dict:
                            Werte_Liste.append(LW_Dict[LW])
                        Werte_Liste.sort()
                        for Karte in LW_Dict:
                            if Werte_Liste[0] == LW_Dict[Karte]:
                                Z_Karte = Karte
                                break
                        Test = False
                        for Karte in Ablage[Gegner]:
                            if Karte == Z_Karte:
                                Ablage[Gegner].remove(Z_Karte)
                                Test = True
                                break
                        if Test == False:
                            for LR in Feld[Gegner]:
                                for LW in Feld_Gegner[LR]:
                                    if LW == Z_Karte:
                                        Feld_Gegner[LR].remove(Z_Karte)
                                        Test = True
                                        break
                                if Test == True:
                                    break
                        Counter = 0
                        for LW in Gegner_LW:
                            if LW == Z_Karte:
                                Counter += 1
                        print("Spieler: " + Gegner)
                        print("Ausgewähltes Lebewesen:\n")
                        if Z_Karte in Verbesserung[Gegner] and Counter == 1:
                            VGK = VG[Z_Karte]
                            #Verbesserungen ins Dict bei Spieler
                            Verbesserung_Spieler = Verbesserung[Spieler]
                            if not Z_Karte in Verbesserung_Spieler:
                                Counter_Dict[Spieler].update({Z_Karte:False})
                                Einmal_Dict[Spieler].update({Z_Karte:False})
                                Verbesserung_Spieler.update({Z_Karte:{"Punkte":0, "Angriff":0, "Verteidigung":0, "Lebensräume":[]}})
                            VSK = Verbesserung_Spieler[Z_Karte]
                            VSK["Punkte"] += VGK["Punkte"]
                            VSK["Angriff"] += VGK["Angriff"]
                            VSK["Verteidigung"] += VGK["Verteidigung"]
                            for LR in VGK["Lebensräume"]:
                                VSK["Lebensräume"].append(LR)
                            #Verbesserungen für print
                            Z_Karte.Punkte += VGK["Punkte"]
                            Z_Karte.Angriff += VGK["Angriff"]
                            Z_Karte.Verteidigung += VGK["Verteidigung"]
                            for LR in VGK["Lebensräume"]:
                                LWLR = Z_Karte.Lebensraum
                                LWLR.append(LR)
                        if Modus == "1":
                            print(repr(Z_Karte))
                        elif Modus == "2":
                            print(str(Z_Karte))
                        if Z_Karte in Verbesserung[Gegner] and Counter == 1:
                            VGK = VG[Z_Karte]
                            Z_Karte.Punkte -= VGK["Punkte"]
                            Z_Karte.Angriff -= VGK["Angriff"]
                            Z_Karte.Verteidigung -= VGK["Verteidigung"]
                            for LR in VGK["Lebensräume"]:
                                LWLR = Z_Karte.Lebensraum
                                LWLR.remove(LR)
                        print("\nWurde " + Gegner + " geklaut und " + Spieler + " gegeben.")
                        Ablage[Spieler].append(Z_Karte)
                        WASK[0] -= 1
                        Spieler_Zug = True
                        Aus = False
                else:
                    print("Fähigkeit kann nur 3 Mal angewandt werden, Diebische Elster muss auf dem Feld platziert sein.")
            #Furchtdrache
            elif E_Karte == Furchtdrache or E_Karte == Starker_Furchtdrache:
                WASK = WAS[E_Karte]
                if WASK[0] > 0:
                    if E_Karte == Furchtdrache:
                        Wert = 1
                    elif E_Karte == Starker_Furchtdrache:
                        Wert = 3
                    Frost_Dict[Gegner] += Wert
                    if Wert == 1:
                        Druck = "einen Zug"
                    else:
                        Druck = str(Wert) + " Züge"
                    print("\n" + Gegner + " setzt " + Druck + " aus.\n")
                    Spieler_Zug = True
                    Aus = False
                    WASK[0] -= 1
                else:
                    print("Extrafunktion kann nur einmal pro Runde angewandt werden, Karte muss auf dem Feld platziert sein.")
            else:
                ("Diese Karte hat keine Extrafunktion, die auf andere Spieler angewandt werden kann.")
        
    #Karten existieren nicht
    else:
        print("Eine oder beide Karten existieren nicht.")
        
#Spielkern
#Runden
Runden_Counter = 0
while Runden_Counter < Runden:
    Runden_Counter += 1
    print("\nRunde " + str(Runden_Counter))
    if (Runden_Counter + 1) == Runden:
        print("Vorletzte Runde")
    elif Runden_Counter == Runden:
          print("Letzte Runde")
    Input_Enter = input("\n")
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
    #Spieler Zug
    #Vor jeder Reihe von Zügen/pro Runde einmal
    Züge_Counter = 0
    print("\nTippe \"Karten Name 1 + Karten Name 2\" um zwei Karten zu kombinieren. Damit kannst du auch Lebewesen in Lebensräumen auf dem Feld platzieren.")
    print("Tippe den Namen eines Lebensraums in deiner Ablage, um diesen im Feld zu platzieren.")
    print("Vor diesen Aktionen kannst du beliebig viele Lebewesen innerhalb des Feldes bewegen (ebenfalls mit \"+\").")
    print("Für Extrafunktionen, die mit anderen Karten (nicht mit Spielern) interagieren: Um  die Extrafunktion zu nutzen, tippe ein \"+\" hinter deine Eingabe. Wenn beide Karten Extrafunktionen haben, tippe zuerst die, die du nutzen willst.")
    print("Um weitere Regeln zu sehen, tippe \"Regeln\". Um den Zug zu übersprigen, drücke Enter.")
    while Züge_Counter < Züge:
        Züge_Counter += 1
        Übrig = Züge - Züge_Counter + 1
        Str_Übrig = "noch " + str(Übrig)
        if Übrig == 1:
            Str_Übrig = "letzter"
        #Spieler Züge
        for Spieler in Alle_Spieler:
            Zug(Spieler)
    #Extrazüge
    Extraprint = False
    for Spieler in Alle_Spieler:
        Extracounter = 0
        Dict = {}
        Feld_Spieler = Feld[Spieler]
        for LR in Feld[Spieler]:
            for LW in Feld_Spieler[LR]:
                if LW in Extrazüge:
                    Extracounter += Extrazüge[LW]
                    Dict.update({LW:Extrazüge[LW]})
        if not Extracounter == 0:
            if Extraprint == False:
                Extraprint = True
                print("\nExtrazüge\n")
            print(Spieler + ":")
            for Karte in Dict:
                print(Karte.Name + ": + " + str(Extrazüge[Karte]))
        while Extracounter > 0:
            Übrig = Extracounter
            Str_Übrig = "noch " + str(Übrig)
            if Übrig == 1:
                Str_Übrig = "letzter"
            Extracounter -= 1
            Zug(Spieler)
        #Werteverbesserungskarten pro Runde
        WAS = Werteverbesserung_Anzahl[Spieler]
        for WV_Karte in WAS:
            if (not WV_Karte == Parasit) and (not WV_Karte == Friedensengel) and (not WV_Karte == Diebische_Elster) and (not WV_Karte == Urwolf):
                WASK = WAS[WV_Karte]
                WASK[0] = WASK[1]
            
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
