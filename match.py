from scipy.stats import skellam
from speeds import *

class Match:
    def __init__(self, hometeam, awayteam):
        self.hometeam = hometeam
        self.awayteam = awayteam
        self.npxgspeed = npxgupdatespeed
        self.finspeed = finupdatespeed
        self.toplay = True
        self.initfinattavg = 1
        self.initfindefavg = 1


    def playmatch(self, season, npgoalh, npgoala, npxgh, npxga, pengoalh=0, pengoala=0):
        goalh = npgoalh + pengoalh
        goala = npgoala + pengoala
        self.predh = self.hometeam.npxgattack * self.awayteam.npxgdefence / season.npgavg()
        self.preda = self.awayteam.npxgattack * self.hometeam.npxgdefence / season.npgavg()
        self.hometeam.npxgattack = (npxgh - self.predh) * self.npxgspeed + self.hometeam.npxgattack
        self.hometeam.npxgdefence = (npxga - self.preda) * self.npxgspeed + self.hometeam.npxgdefence
        self.awayteam.npxgattack = (npxga - self.preda) * self.npxgspeed + self.awayteam.npxgattack
        self.awayteam.npxgdefence = (npxgh - self.predh) * self.npxgspeed + self.awayteam.npxgdefence
        self.hometeam.finatt = self.hometeam.finatt + self.finspeed*(npgoalh - npxgh)
        self.awayteam.finatt = self.awayteam.finatt + self.finspeed*(npgoala - npxga)
        self.hometeam.findef = self.hometeam.findef + self.finspeed*(npgoala - npxga)
        self.awayteam.findef = self.awayteam.findef + self.finspeed*(npgoalh - npxgh)
        self.toplay = False
        self.hometeam.goalsfor += goalh
        self.hometeam.goalsag += goala
        self.awayteam.goalsfor += goala
        self.awayteam.goalsag += goalh
        if goalh > goala:
            self.hometeam.points += 3
        elif goalh == goala:
            self.hometeam.points += 1
            self.awayteam.points += 1
        else:
            self.awayteam.points += 3
        season.refreshratings()

    def predictmatch(self, season):
        self.simhomeg = self.hometeam.attack * self.awayteam.defence / season.goalsavg()
        self.simawayg = self.awayteam.attack * self.hometeam.defence / season.goalsavg()
        probaway = skellam.cdf(-1, self.simhomeg, self.simawayg)
        probdraw = skellam.pmf(0, self.simhomeg, self.simawayg)
        probhome = 1 - probaway - probdraw
        self.hometeam.simgf += self.simhomeg
        self.awayteam.simgf += self.simawayg
        self.hometeam.simga += self.simawayg
        self.awayteam.simga += self.simhomeg
        self.hometeam.simpts += 3 * probhome + probdraw
        self.awayteam.simpts += 3 * probaway + probdraw
