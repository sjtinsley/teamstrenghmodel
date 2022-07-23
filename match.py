from scipy.stats import skellam, poisson
from speeds import *

class Match:
    def __init__(self, hometeam, awayteam):
        self.homeadvantage = 0.24
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
        self.predh = self.hometeam.npxgattack * self.awayteam.npxgdefence / season.npgavg() * 2 * self.homeadvantage / (2 + self.homeadvantage)
        self.preda = self.awayteam.npxgattack * self.hometeam.npxgdefence / season.npgavg() * 2 / (2 + self.homeadvantage)
        self.hometeam.npxgattack += (npxgh - self.predh) * self.npxgspeed
        self.hometeam.npxgdefence += (npxga - self.preda) * self.npxgspeed
        self.awayteam.npxgattack += (npxga - self.preda) * self.npxgspeed
        self.awayteam.npxgdefence += (npxgh - self.predh) * self.npxgspeed
        self.hometeam.finatt += self.finspeed*(npgoalh - npxgh)
        self.awayteam.finatt += self.finspeed*(npgoala - npxga)
        self.hometeam.findef += self.finspeed*(npgoala - npxga)
        self.awayteam.findef += self.finspeed*(npgoalh - npxgh)
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
        self.predhomeg = self.hometeam.attack * self.awayteam.defence / season.goalsavg()
        self.predawayg = self.awayteam.attack * self.hometeam.defence / season.goalsavg()
        probaway = skellam.cdf(-1, self.predhomeg, self.predawayg)
        probdraw = skellam.pmf(0, self.predhomeg, self.predawayg)
        probhome = 1 - probaway - probdraw
        self.hometeam.predgf += self.predhomeg
        self.awayteam.predgf += self.predawayg
        self.hometeam.predga += self.predawayg
        self.awayteam.predga += self.predhomeg
        self.hometeam.predpts += 3 * probhome + probdraw
        self.awayteam.predpts += 3 * probaway + probdraw

    def simulatematch(self, season):
        self.simhomeg = poisson.rvs(self.hometeam.attack * self.awayteam.defence / season.goalsavg())
        self.simawayg = poisson.rvs(self.awayteam.attack * self.hometeam.defence / season.goalsavg())
        self.hometeam.simgf += self.simhomeg
        self.awayteam.simga += self.simhomeg
        self.awayteam.simgf += self.simawayg
        self.hometeam.simga += self.simawayg
        if self.simhomeg > self.simawayg:
            self.hometeam.simpts += 3
        elif self.simhomeg == self.simawayg:
            self.hometeam.simpts += 1
            self.awayteam.simpts += 1
        else:
            self.awayteam.simpts += 3





