        else:
            ########################Aktion mit anderem Spieler##############################
            #Gifte und Gefrorener Trank
            if "Gift" in E_Karte.Name or E_Karte.Name == "Gefrorener Trank":
                #Zerstörungs Gifte
                elif E_Karte in Zerstörungs_Gifte:
                    Gegner_LW = []
                    for Lw in Ablage[Gegner]:
                        if (Lw in Alle_Lebewesen) and (Lw not in Gegner_LW):
                            Gegner_LW.append(Lw)
                    Feld_Gegner = Feld[Gegner]
                    for Lr in Feld_Gegner:
                        for Lw in Feld_Gegner[Lr]:
                            if Lw not in Gegner_LW:
                                Gegner_LW.append(Lw)
                    if Gegner_LW == []:
                        print("Dieser Spieler besitzt keine Lebewesen.")
                    else:
                        LW_Dict = {}
                        for Lw in Gegner_LW:
                            LW_Dict.update({Lw:Lw.Punkte})
                            if Lw in Verbesserung[Gegner] and Ein_D_Ge[Lw] == True:
                                VGK = Verbesserung_Gegner[Lw]
                                LW_Dict[Lw] += VGK["Punkte"]
                                Ein_D_Ge[Lw] = False
                        Werte_Liste = []
                        for Lw in LW_Dict:
                            Werte_Liste.append(LW_Dict[Lw])
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
                            for Lr in Feld[Gegner]:
                                for Lw in Feld_Gegner[Lr]:
                                    if Lw == Z_Karte:
                                        Feld_Gegner[Lr].remove(Z_Karte)
                                        Test = True
                                        break
                                if Test == True:
                                    break
                        Counter = 0
                        for Lw in Gegner_LW:
                            if Lw == Z_Karte:
                                Counter += 1
                        print("Spieler: " + Gegner)
                        print("Ausgewähltes Lebewesen:\n")
                        if Z_Karte in Verbesserung[Gegner] and Counter == 1:
                            #Verbesserungen enfernen
                            CDG = Counter_Dict[Gegner]
                            del CDG[Z_Karte]
                            del Ein_D_Ge[Z_Karte]
                            del Verbesserung_Gegner[Z_Karte]                            
                            #Verbesserungen für print
                            VGK = Verbesserung_Gegner[Z_Karte]
                            Z_Karte.Punkte += VGK["Punkte"]
                            Z_Karte.Angriff += VGK["Angriff"]
                            Z_Karte.Verteidigung += VGK["Verteidigung"]
                            for Lr in VGK["Lebensräume"]:
                                LWLR = Z_Karte.Lebensraum
                                LWLR.append(Lr)
                        if Modus == "1":
                            print(repr(Z_Karte))
                        elif Modus == "2":
                            print(str(Z_Karte))
                        if Z_Karte in Verbesserung[Gegner] and Counter == 1:
                            VGK = Verbesserung_Gegner[Z_Karte]
                            Z_Karte.Punkte -= VGK["Punkte"]
                            Z_Karte.Angriff -= VGK["Angriff"]
                            Z_Karte.Verteidigung -= VGK["Verteidigung"]
                            for Lr in VGK["Lebensräume"]:
                                LWLR = Z_Karte.Lebensraum
                                LWLR.remove(Lr)
                        print("\nWurde entfernt.")
                        Spieler_Zug = True
                        Ablage[Spieler].remove(E_Karte)
                        Aus = False
            #Diebische Elster
            elif E_Karte == Diebische_Elster:
                WASK = WAS[Diebische_Elster]
                if WASK[0] > 0:
                    Gegner_LW = []
                    for Lw in Ablage[Gegner]:
                        if (Lw in Alle_Lebewesen) and (Lw not in Gegner_LW):
                            Gegner_LW.append(Lw)
                    Feld_Gegner = Feld[Gegner]
                    for Lr in Feld_Gegner:
                        for Lw in Feld_Gegner[Lr]:
                            if Lw not in Gegner_LW:
                                Gegner_LW.append(Lw)
                    if Gegner_LW == []:
                        print("Dieser Spieler besitzt keine Lebewesen.")
                    else:
                        LW_Dict = {}
                        for Lw in Gegner_LW:
                            LW_Dict.update({Lw:Lw.Punkte})
                            if Lw in Verbesserung[Gegner] and Ein_D_Ge[Lw] == True:
                                VGK = Verbesserung_Gegner[Lw]
                                LW_Dict[Lw] += VGK["Punkte"]
                                Ein_D_Ge[Lw] = False
                        Werte_Liste = []
                        for Lw in LW_Dict:
                            Werte_Liste.append(LW_Dict[Lw])
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
                            for Lr in Feld[Gegner]:
                                for Lw in Feld_Gegner[Lr]:
                                    if Lw == Z_Karte:
                                        Feld_Gegner[Lr].remove(Z_Karte)
                                        Test = True
                                        break
                                if Test == True:
                                    break
                        Counter = 0
                        for Lw in Gegner_LW:
                            if Lw == Z_Karte:
                                Counter += 1
                        print("Spieler: " + Gegner)
                        print("Ausgewähltes Lebewesen:\n")
                        if Z_Karte in Verbesserung[Gegner] and Counter == 1:
                            VGK = Verbesserung_Gegner[Z_Karte]
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
                            for Lr in VGK["Lebensräume"]:
                                VSK["Lebensräume"].append(Lr)
                            #Verbesserungen für print
                            Z_Karte.Punkte += VGK["Punkte"]
                            Z_Karte.Angriff += VGK["Angriff"]
                            Z_Karte.Verteidigung += VGK["Verteidigung"]
                            for Lr in VGK["Lebensräume"]:
                                LWLR = Z_Karte.Lebensraum
                                LWLR.append(Lr)
                        if Modus == "1":
                            print(repr(Z_Karte))
                        elif Modus == "2":
                            print(str(Z_Karte))
                        if Z_Karte in Verbesserung[Gegner] and Counter == 1:
                            VGK = Verbesserung_Gegner[Z_Karte]
                            Z_Karte.Punkte -= VGK["Punkte"]
                            Z_Karte.Angriff -= VGK["Angriff"]
                            Z_Karte.Verteidigung -= VGK["Verteidigung"]
                            for Lr in VGK["Lebensräume"]:
                                LWLR = Z_Karte.Lebensraum
                                LWLR.remove(Lr)
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