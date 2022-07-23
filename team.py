class Team:
    def __init__(self, name, npxgattack, npxgdefence, finatt=1, findef=1, penfbase=1.68, penconv=87.5/110):
        self.name = name
        self.npxgattack = npxgattack
        self.npxgdefence = npxgdefence
        self.finatt = (finatt - 1) * npxgattack
        self.findef = (findef - 1) * npxgdefence
        self.penfbase = penfbase
        self.penfor = penfbase + npxgattack * 0.0751299
        self.penag = 1.68601137 + npxgdefence * 0.0732303
        self.penconv = penconv
        self.goalsfor = 0
        self.goalsag = 0
        self.points = 0
        self.attack = self.npxgattack + (self.finatt) + self.penfor/38 * self.penconv
        self.defence = self.npxgdefence + (self.findef) + self.penag/38 * self.penconv
        self.simgf = 0
        self.simga = 0
        self.simpts = 0
        self.predgf = 0
        self.predga = 0
        self.predpts = 0
        self.schedadjnpxgf = 0
        self.schedadjnpxga = 0
        self.matches_played = 0
