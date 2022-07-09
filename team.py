class Team:
    def __init__(self, name, npxgattack, npxgdefence, finatt=1, findef=1, penfor=5.5, penag=5.5, penconv=0.76):
        self.name = name
        self.npxgattack = npxgattack
        self.npxgdefence = npxgdefence
        self.finatt = finatt
        self.findef = findef
        self.penfor = penfor
        self.penag = penag
        self.penconv = penconv
        self.goalsfor = 0
        self.goalsag = 0
        self.points = 0
        self.attack = self.npxgattack * (self.finatt) + self.penfor/38 * self.penconv
        self.defence = self.npxgdefence * (self.findef) + self.penag/38 * self.penconv
        self.simgf = 0
        self.simga = 0
        self.simpts = 0