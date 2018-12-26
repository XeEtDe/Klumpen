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