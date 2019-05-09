def Nächster(Spieler):
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(622, 0, 800, 89))
    global Runden_Counter
    global Züge_Counter
    global Züge
    global Runden
    global Spieler
    global Extrazüge_Dict
    global Ex_Zü
    global Werteverbesserung_Anzahl
    Neuer_Spieler = None
    ##Nach dem Zug mit altem Spieler##
    ##Züge aufgebraucht##
    if Alter_Spieler == Alle_Spieler[-1]:
        #Überschrift
        Übrig = Züge - Züge_Counter
        Züge_String = "noch " + str(Übrig) + " Züge"
        if Übrig == 1:
            Züge_String = "letzter Zug"
        #Letzter Spieler mit letzem Zug -> Runde vorbei
        if Züge_Counter == Züge:
            #Extrazüge berechnen
            if Ex_Zü == True:
                Ex_Zü = False
                for Spieler_ in Alle_Spieler:
                    Extracounter = 0
                    Extrazüge_Dict.update({Spieler_:[[], 0]})
                    for Lr in Feld[Spieler_]:
                        for Lw in Feld[Spieler_][Lr]:
                            if Lw in Karten.Extrazüge:
                                Extrazüge_Dict[Spieler_][1] += Karten.Extrazüge[Lw]
                                Extrazüge_Dict[Spieler_][0].append(Lw)
            #Extrazüge ausführen
            for Spieler__ in Alle_Spieler:
                if Spieler__ in Extrazüge_Dict:
                    if Extrazüge_Dict[Spieler__][1] == 0:
                        Extrazüge_Dict.pop(Spieler__)
            if not Extrazüge_Dict == {}:
                Spieler_1 = Extrazüge_Dict[0]
                String = "Extrazüge\n"
                for Lw in Extrazüge_Dict[Spieler_1][0]:
                    String += Karte.Name + ": + " + str(Karten.Extrazüge[Lw]) + "\n"
                String += "Insgesamt: + " + str(Extrazüge_Dict[Spieler_1][1])
                Info_Text(String)
                ###############Extrazüge ausführen fehlt#####################################
            #Runde fertig wenn Extrazüge aufgebraucht
            if Extrazüge_Dict == {}:
                Ex_Zü = True
    #Überschrift
    Übrig = Runden - Runden_Counter
    Runden_String = "noch " + str(Übrig) + " Runden"
    if Übrig == 1:
        Runden_String = "letzte Runde"
    Text = SMaxG(Runden_String, None, 30)
    screen.blit(Text, (620 + (415 / 2 - Text.get_width() / 2), 10))
    Übrig = Züge - Züge_Counter
    Züge_String = "noch " + str(Übrig) + " Züge"
    if Übrig == 1:
        Züge_String = "letzter Zug"
    Text = SMaxG(Züge_String, None, 30)
    screen.blit(Text, (620 + (415 / 2 - Text.get_width() / 2), 60))
    if Spieler[-1] == "s" or Spieler[-1] == "S" or Spieler[-1] == "X" or Spieler[-1] == "x":
        Text = SMaxG(Spieler + "\' Zug", 300, 50)
    else:
        Text = SMaxG(Spieler + "s Zug", 300, 50)
    screen.blit(Text, (1025 + (415 / 2 - Text.get_width() / 2), 50 - Text.get_height() / 2))
    global Spieler_Zug
    Spieler_Zug = False
    for Bttn in Aktions_Buttons:
        if Bttn.Switch == False:
            Bttn.Change()
    Clear()