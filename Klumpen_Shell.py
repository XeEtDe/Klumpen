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
            
#Auswertung
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
