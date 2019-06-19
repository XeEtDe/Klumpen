class Spieler():
    def __init__(self, Name):
        self.Name = Name

    def Druck(self):
        print(self.Name)

First = Spieler("A")

Dict = {"A":1, "B":2, "C":3}
for Num, (Pos, Karte) in enumerate(Dict.items()):
    print(Num)
    print(Pos)
    print(Karte)