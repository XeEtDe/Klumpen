#Kombi
#def Add(Karten_Liste, Extra = False):
    #Überprüfung und Zuweisung von Variablen
    #if beide Listenelemente Karten:
        #if Ort nicht definiert:
            #Meldung
            #break
        #elif Extra == True:
            #Extrafunktionen
        #elif Lw und LR:
            #LW bewegen
        #elif Trank in Name:
            #Tränke
        #else:
            #for Karte in Alle_Karten:
                #if Gesuchte_Kombi in Karte.Kombi:
                    #if eine Karte == LR:
                        #LR + LR
                        #LR + E
                    #elif eine Karte == LW:
                        #LW + LW
                        #LW + E
                    #else:
                        #E + E
                #elif Counter == len:
                    #Keine Kombi möglich
            #if Spieler_Zug == True: (erfolgreicher Zug)
                #übertragene Verbesserungen
    #elif ein Listenelement Karte: ###ab hier überarbeiten###
        #if Gegener == None:
            #Extraaktion ohne Gegner mit anderer Extrainfo
        #else:
            #Extraaktion mit Gegner
    #else:
        #Eine oder beide Karten existieren nicht
def Add(Karten_Liste, Extra = False):
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
    #Karten und Namen
    Name_Karte_1 = Karten_Liste[0]
    Name_Karte_2 = Karten_Liste[1]
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
        if Ort_1 == False or Ort_2 == False:
            print("Fehler Add(); Ort_1 oder Ort_2 nicht definiert")
        #Extrafunktionen
        elif Extra == True:
            E_Karte = Karte_1
            Andere_Karte = Karte_2
            Ort = Ort_1
            Anderer_Ort = Ort_2
            Anderer_LR = LR_2
            if E_Karte in WAS:
                WASK = WAS[E_Karte]
            #Parasit
            if E_Karte == Karten.Parasit:
                if Andere_Karte in Karten.Alle_Lebewesen:
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
                        Info_Text("Fähigkeit kann nur einmal angewandt werden, Parasit muss auf dem Feld platziert sein.")
                else:
                    Info_Text("Kann nur die Werte von Lebewesen aufnehmen.")
            #Werteverbesserungskarte
            elif E_Karte in Karten.Werteverbesserung_Übersicht:
                if Andere_Karte in Karten.Alle_Lebewesen:
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
                        Info_Text("Fähigkeit kann nur einmal angewandt werden, Karte muss auf dem Feld platziert sein.")
                else:
                    Info_Text("Kann nur die Werte von Lebewesen verbessern.")
            #Mehr Lebensräume
            elif E_Karte in Karten.ExtraLRs:
                if Andere_Karte in Karten.Alle_Lebewesen:
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
                            Info_Text("Dieses Lebewesen kann bereits in allen Lebensräumen leben.")
                        else:
                            #Zufall
                            Spieler_Zug = True
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
                        Info_Text("Platziere Lebewesen auf dem Feld, um ihre Extrafunktion zu nutzen.")
                else:
                    Info_Text("Kann nur auf Lebewesen angewandt werden.")
            #Friedensengel
            elif E_Karte == Karten.Friedensengel:
                if Andere_Karte in Karten.Alle_Lebensraum:
                    if WASK[0] > 0:
                        if "Klein" in Andere_Karte.Name:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Karten.Magisches_Kleines_Wonderland
                            else:
                                Neue_Karte = Karten.Kleines_Wonderland
                        elif "Groß" in Andere_Karte.Name:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Karten.Magisches_Großes_Wonderland
                            else:
                                Neue_Karte = Karten.Großes_Wonderland
                        else:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Karten.Magisches_Wonderland
                            else:
                                Neue_Karte = Karten.Wonderland
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
                        Info_Text("Muss auf dem Feld platziert sein und kann nur 3 Mal angewandt werden.")
                else:
                    Info_Text("Extrafunktion kann nur auf Lebensräume angewandt werden.")
            #Zauberer
            elif E_Karte == Karten.Zauberer:
                if Andere_Karte in Karten.Alle_Elemente:
                    if not Ort == Ablage[Spieler]:
                        for Trank in Karten.Tränke_Kombi:
                            if Andere_Karte in Karten.Tränke_Kombi[Trank]:
                                Neue_Karte = Trank
                                break
                        Ablage_Spieler.append(Neue_Karte)
                        Ablage_Spieler.remove(Andere_Karte)
                        Spieler_Zug = True
                    else:
                        Info_Text("Platziere den Zauberer im Feld um seine Funktion zu nutzen.")
                else:
                    Info_Text("Zauberer kann nur Elemente in Tränke verwandeln.")
            #Dunkler Magier
            elif E_Karte == Karten.Dunkler_Magier:
                if Andere_Karte in Karten.Alle_Elemente:
                    if not Ort == Ablage[Spieler]:
                        for Gift in Karten.Gifte_Kombi:
                            if Andere_Karte in Karten.Gifte_Kombi[Gift]:
                                Neue_Karte = Gift
                                break
                        Ablage_Spieler.append(Neue_Karte)
                        Ablage_Spieler.remove(Andere_Karte)
                        Spieler_Zug = True
                    else:
                        Info_Text("Platziere den Dunklen Magier im Feld um seine Funktion zu nutzen.")
                else:
                    Info_Text("Dunkler Magier kann nur Elemente in Gifte verwandeln.")
            #Urwolf
            elif E_Karte == Karten.Urwolf:
                if Andere_Karte in Karten.Alle_Lebewesen:
                    if WASK[0] > 0:
                        Weiter = True
                        if Andere_Karte.Punkte > Karten.Werwolf.Punkte:
                            Info_Text("Die Karte ist bereits besser als eine Werwolf-Karte.")
                            Weiter = False
                        if not Anderer_Ort == Ablage[Spieler]:
                            if not Anderer_LR.Art == "Wald":
                                Info_Text("Der Lebensraum ist für einen Werwolf nicht geeignet. Wähle ein Lebewesen in einem Wald oder in der Ablage.")
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
                        Info_Text("Kann nur einmal im Spiel angewandt werden, Karte muss auf dem Feld platziert sein.")
                else:
                    Info_Text("Kann nur auf Lebewesen angewandt werden.")
            else:
                Info_Text("Keine der Karten hat eine Extrafunktion.")
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
                Info_Text("Platziere den Lebensraum erst auf dem Feld.")
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
                    Info_Text("Dieser Lebensraum ist bereits voll")
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
                    Info_Text("Dieser Lebensraum ist für das Lebewesen nicht geeignet")
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
                if Andere_Karte in Karten.Alle_Lebensraum:
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
                                Neue_Karte = Karten.Magisches_Kleines_Wonderland
                            else:
                                Neue_Karte = Karten.Kleines_Wonderland
                        elif "Groß" in Andere_Karte.Name:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Karten.Magisches_Großes_Wonderland
                            else:
                                Neue_Karte = Karten.Großes_Wonderland
                        else:
                            if "Magisch" in Andere_Karte.Name:
                                Neue_Karte = Karten.Magisches_Wonderland
                            else:
                                Neue_Karte = Karten.Wonderland
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
                    Info_Text("Du kannst diesen Trank nur auf Lebensräume anwenden.")
            #Lebewesen-Tränke     
            elif "Lebewesen" in Trank_Karte.Beschreibung:
                if Andere_Karte in Karten.Alle_Lebewesen:
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
                    Info_Text("Du kannst diesen Trank nur auf Lebenwesen anwenden.")
        #Schleifen-Start/Kombi oder nicht        
        else:
            Counter_Add = 0
            for Karte in Alle_Karten:
                Counter_Add += 1
                #Kombi
                if Gesuchte_Kombi_1 in Karte.Kombi or Gesuchte_Kombi_2 in Karte.Kombi:
                    Neue_Karte = Karte
                    #LR
                    if Karte_1 in Karten.Alle_Lebensraum or Karte_2 in Karten.Alle_Lebensraum:
                        if Karte_1 in Karten.Alle_Lebensraum:
                            LR_Karte = Karte_1
                            Andere_Karte = Karte_2
                        else:
                            LR_Karte = Karte_2
                            Andere_Karte = Karte_1
                        #LR + LR
                        if Andere_Karte in Karten.Alle_Lebensraum:
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
                        elif Andere_Karte in Karten.Alle_Elemente:
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
                    elif Karte_1 in Karten.Alle_Lebewesen or Karte_2 in Karten.Alle_Lebewesen:
                        if Karte_1 in Karten.Alle_Lebewesen:
                            LW_Karte = Karte_1
                            Andere_Karte = Karte_2
                        else:
                            LW_Karte = Karte_2
                            Andere_Karte = Karte_1
                        #LW + LW
                        if Andere_Karte in Karten.Alle_Lebewesen:
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
                                    Info_Text("Du kannst nur innerhalb des Feldes oder der Ablage kombinieren.")
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
                                    Info_Text("Keiner der beiden Lebensräume ist geeignet für das neue Lebewesen.")
                                    break
                        #LW + E
                        elif Andere_Karte in Karten.Alle_Elemente:
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
                                        Info_Text("Der Lebensraum ist nicht geeignet für das neue Lebewesen.")
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
                                        Info_Text("Der Lebensraum ist nicht geeignet für das neue Lebewesen.")
                                        break
                                    break
                    #E + E
                    elif Karte_1 in Karten.Alle_Elemente and Karte_2 in Karten.Alle_Elemente:
                        Ablage[Spieler].append(Neue_Karte)
                        Ablage[Spieler].remove(Karte_1)
                        Ablage[Spieler].remove(Karte_2)
                        Spieler_Zug = True
                        break
                #Keine Kombi möglich
                elif Counter_Add == len(Alle_Karten):
                    Info_Text("Diese Karten lassen sich nicht kombinieren.")
            #Verbesserungen
            if Spieler_Zug == True:
                #Weitergabe Verbesserungen
                if Neue_Karte in Karten.Alle_Lebensraum:
                    Counter = 0
                    if Karte_1 in Karten.Alle_Lebensraum and Karte_1 in Verbesserung_Spieler:
                        Counter += Verbesserung_Spieler[Karte_1]
                        del Verbesserung_Spieler[Karte_1]
                    if Karte_2 in Karten.Alle_Lebensraum and Karte_2 in Verbesserung_Spieler:
                        Counter += Verbesserung_Spieler[Karte_2]
                        del Verbesserung_Spieler[Karte_1]
                    if not Counter == 0:
                        if not Neue_Karte in Verbesserung_Spieler:
                            Counter_Dict[Spieler].update({Neue_Karte:False})
                            Einmal_Dict[Spieler].update({Neue_Karte:False})
                            Verbesserung_Spieler.update({Neue_Karte:0})
                        Verbesserung_Spieler[Neue_Karte] += Counter
                elif Neue_Karte in Karten.Alle_Lebewesen:
                    Counter_P = 0
                    Counter_A = 0
                    Counter_V = 0
                    if Karte_1 in Karten.Alle_Lebewesen and Karte_1 in Verbesserung_Spieler:
                        VSK = Verbesserung_Spieler[Karte_1]
                        Counter_P += VSK["Punkte"]
                        Counter_A += VSK["Angriff"]
                        Counter_V += VSK["Verteidigung"]
                        del Verbesserung_Spieler[Karte_1]
                    if Karte_2 in Karten.Alle_Lebewesen and Karte_2 in Verbesserung_Spieler:
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
            #############Joker######################
            if E_Karte == Karten.Joker:
                WASK = WAS[Joker]
                if WASK[0] > 0:
                    Neue_Karte = None
                    #######Auswahl als Buttons
                    if Andere_Name == "Lebewesen" or Andere_Name == "lebewesen":
                        Neue_Karte = random.choice(Start_Lebewesen)
                    elif Andere_Name == "Lebensraum" or Andere_Name == "lebensraum":
                        Neue_Karte = random.choice(Start_Lebensraum)
                    elif Andere_Name == "Element" or Andere_Name == "element":
                        Neue_Karte = random.choice(Start_Elemente)
                    if Neue_Karte == None:
                        Info_Text("Wähle zwischen Element, Lebewesen und Lebensraum.")
                    else:
                        Ablage[Spieler].append(Neue_Karte)
                        Info_Text("Neue Karte:")
                        #####################
                        if not Neue_Karte in Karten.Start_Elemente:
                            if Modus == "1":
                                print(repr(Neue_Karte))
                            elif Modus == "2":
                                print(str(Neue_Karte))
                        else:
                            print(Neue_Karte)
                        Spieler_Zug = True
                        WASK[0] -= 1
                else:
                    Info_Text("Kann nur einmal pro Runde angewandt werden, Karte muss auf dem Feld platziert sein.")
            else:
                Info_Text("Eine oder beide Karten existieren nicht.")
        else:
            ########################Aktion mit anderem Spieler##############################
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
        Info_Text("Eine oder beide Karten existieren nicht.")