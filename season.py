from teams2223 import *
from matches2223 import *
import pandas as pd
import numpy as np

class Season:
    def __init__(self):
        self.teams = [arsenal,astonvilla,bournemouth,brentford,brighton,chelsea,palace,everton,fulham,leeds,leicester,liverpool,mancity,manutd,newcastle,forest,southampton,tottenham,westham,wolves]
        self.matches = [arsenalastonvilla,arsenalbournemouth,arsenalbrentford,arsenalbrighton,arsenalchelsea,arsenaleverton,arsenalforest,arsenalfulham,arsenalleeds,arsenalleicester,arsenalliverpool,arsenalmancity,arsenalmanutd,arsenalnewcastle,arsenalpalace,arsenalsouthampton,arsenaltottenham,arsenalwestham,arsenalwolves,astonvillaarsenal,astonvillabournemouth,astonvillabrentford,astonvillabrighton,astonvillachelsea,astonvillaeverton,astonvillaforest,astonvillafulham,astonvillaleeds,astonvillaleicester,astonvillaliverpool,astonvillamancity,astonvillamanutd,astonvillanewcastle,astonvillapalace,astonvillasouthampton,astonvillatottenham,astonvillawestham,astonvillawolves,bournemoutharsenal,bournemouthastonvilla,bournemouthbrentford,bournemouthbrighton,bournemouthchelsea,bournemoutheverton,bournemouthforest,bournemouthfulham,bournemouthleeds,bournemouthleicester,bournemouthliverpool,bournemouthmancity,bournemouthmanutd,bournemouthnewcastle,bournemouthpalace,bournemouthsouthampton,bournemouthtottenham,bournemouthwestham,bournemouthwolves,brentfordarsenal,brentfordastonvilla,brentfordbournemouth,brentfordbrighton,brentfordchelsea,brentfordeverton,brentfordforest,brentfordfulham,brentfordleeds,brentfordleicester,brentfordliverpool,brentfordmancity,brentfordmanutd,brentfordnewcastle,brentfordpalace,brentfordsouthampton,brentfordtottenham,brentfordwestham,brentfordwolves,brightonarsenal,brightonastonvilla,brightonbournemouth,brightonbrentford,brightonchelsea,brightoneverton,brightonforest,brightonfulham,brightonleeds,brightonleicester,brightonliverpool,brightonmancity,brightonmanutd,brightonnewcastle,brightonpalace,brightonsouthampton,brightontottenham,brightonwestham,brightonwolves,chelseaarsenal,chelseaastonvilla,chelseabournemouth,chelseabrentford,chelseabrighton,chelseaeverton,chelseaforest,chelseafulham,chelsealeeds,chelsealeicester,chelsealiverpool,chelseamancity,chelseamanutd,chelseanewcastle,chelseapalace,chelseasouthampton,chelseatottenham,chelseawestham,chelseawolves,evertonarsenal,evertonastonvilla,evertonbournemouth,evertonbrentford,evertonbrighton,evertonchelsea,evertonforest,evertonfulham,evertonleeds,evertonleicester,evertonliverpool,evertonmancity,evertonmanutd,evertonnewcastle,evertonpalace,evertonsouthampton,evertontottenham,evertonwestham,evertonwolves,forestarsenal,forestastonvilla,forestbournemouth,forestbrentford,forestbrighton,forestchelsea,foresteverton,forestfulham,forestleeds,forestleicester,forestliverpool,forestmancity,forestmanutd,forestnewcastle,forestpalace,forestsouthampton,foresttottenham,forestwestham,forestwolves,fulhamarsenal,fulhamastonvilla,fulhambournemouth,fulhambrentford,fulhambrighton,fulhamchelsea,fulhameverton,fulhamforest,fulhamleeds,fulhamleicester,fulhamliverpool,fulhammancity,fulhammanutd,fulhamnewcastle,fulhampalace,fulhamsouthampton,fulhamtottenham,fulhamwestham,fulhamwolves,leedsarsenal,leedsastonvilla,leedsbournemouth,leedsbrentford,leedsbrighton,leedschelsea,leedseverton,leedsforest,leedsfulham,leedsleicester,leedsliverpool,leedsmancity,leedsmanutd,leedsnewcastle,leedspalace,leedssouthampton,leedstottenham,leedswestham,leedswolves,leicesterarsenal,leicesterastonvilla,leicesterbournemouth,leicesterbrentford,leicesterbrighton,leicesterchelsea,leicestereverton,leicesterforest,leicesterfulham,leicesterleeds,leicesterliverpool,leicestermancity,leicestermanutd,leicesternewcastle,leicesterpalace,leicestersouthampton,leicestertottenham,leicesterwestham,leicesterwolves,liverpoolarsenal,liverpoolastonvilla,liverpoolbournemouth,liverpoolbrentford,liverpoolbrighton,liverpoolchelsea,liverpooleverton,liverpoolforest,liverpoolfulham,liverpoolleeds,liverpoolleicester,liverpoolmancity,liverpoolmanutd,liverpoolnewcastle,liverpoolpalace,liverpoolsouthampton,liverpooltottenham,liverpoolwestham,liverpoolwolves,mancityarsenal,mancityastonvilla,mancitybournemouth,mancitybrentford,mancitybrighton,mancitychelsea,mancityeverton,mancityforest,mancityfulham,mancityleeds,mancityleicester,mancityliverpool,mancitymanutd,mancitynewcastle,mancitypalace,mancitysouthampton,mancitytottenham,mancitywestham,mancitywolves,manutdarsenal,manutdastonvilla,manutdbournemouth,manutdbrentford,manutdbrighton,manutdchelsea,manutdeverton,manutdforest,manutdfulham,manutdleeds,manutdleicester,manutdliverpool,manutdmancity,manutdnewcastle,manutdpalace,manutdsouthampton,manutdtottenham,manutdwestham,manutdwolves,newcastlearsenal,newcastleastonvilla,newcastlebournemouth,newcastlebrentford,newcastlebrighton,newcastlechelsea,newcastleeverton,newcastleforest,newcastlefulham,newcastleleeds,newcastleleicester,newcastleliverpool,newcastlemancity,newcastlemanutd,newcastlepalace,newcastlesouthampton,newcastletottenham,newcastlewestham,newcastlewolves,palacearsenal,palaceastonvilla,palacebournemouth,palacebrentford,palacebrighton,palacechelsea,palaceeverton,palaceforest,palacefulham,palaceleeds,palaceleicester,palaceliverpool,palacemancity,palacemanutd,palacenewcastle,palacesouthampton,palacetottenham,palacewestham,palacewolves,southamptonarsenal,southamptonastonvilla,southamptonbournemouth,southamptonbrentford,southamptonbrighton,southamptonchelsea,southamptoneverton,southamptonforest,southamptonfulham,southamptonleeds,southamptonleicester,southamptonliverpool,southamptonmancity,southamptonmanutd,southamptonnewcastle,southamptonpalace,southamptontottenham,southamptonwestham,southamptonwolves,tottenhamarsenal,tottenhamastonvilla,tottenhambournemouth,tottenhambrentford,tottenhambrighton,tottenhamchelsea,tottenhameverton,tottenhamforest,tottenhamfulham,tottenhamleeds,tottenhamleicester,tottenhamliverpool,tottenhammancity,tottenhammanutd,tottenhamnewcastle,tottenhampalace,tottenhamsouthampton,tottenhamwestham,tottenhamwolves,westhamarsenal,westhamastonvilla,westhambournemouth,westhambrentford,westhambrighton,westhamchelsea,westhameverton,westhamforest,westhamfulham,westhamleeds,westhamleicester,westhamliverpool,westhammancity,westhammanutd,westhamnewcastle,westhampalace,westhamsouthampton,westhamtottenham,westhamwolves,wolvesarsenal,wolvesastonvilla,wolvesbournemouth,wolvesbrentford,wolvesbrighton,wolveschelsea,wolveseverton,wolvesforest,wolvesfulham,wolvesleeds,wolvesleicester,wolvesliverpool,wolvesmancity,wolvesmanutd,wolvesnewcastle,wolvespalace,wolvessouthampton,wolvestottenham,wolveswestham]

    def getpredictions(self):
        holdtable=[["Team", "Goals For", "Goals Against", "Points"]]
        for m in self.matches:
            if m.toplay:
                m.predictmatch(self)
        for t in self.teams:
            holdtable.append([t.name, t.goalsfor + t.predgf, t.goalsag + t.predga, t.points + t.predpts])
        table = pd.DataFrame(holdtable)
        table.to_csv('predictions.csv', index=False, header=False)

    def getratings(self):
        holdratings = [["Team", "Attack", "Defence"]]
        for t in self.teams:
            holdratings.append([t.name, t.attack, t.defence])
        ratings = pd.DataFrame(holdratings)
        ratings.to_csv('teamratings.csv', index=False, header=False)

    def goalsavg(self):
        return sum(t.attack for t in self.teams) / 20

    def finattavg(self):
        return sum(t.finatt for t in self.teams) / 20

    def findefavg(self):
        return sum(t.findef for t in self.teams) / 20

    def npgavg(self):
        return sum(t.npxgattack for t in self.teams) / 20

    def refreshratings(self):
        for t in self.teams:
            t.attack = t.npxgattack + (t.finatt + self.findefavg()) + t.penfor/38 * t.penconv
            t.defence = t.npxgdefence + (t.findef + self.finattavg()) + t.penag / 38 * t.penconv
            t.penfor = t.penfbase + t.npxgattack * 0.0751299
            t.penag = 1.68601137 + t.npxgdefence * 0.0732303

    def resetsimulation(self):
        for t in self.teams:
            t.simga = 0
            t.simgf = 0
            t.simpts = 0

    def montecarlosims(self):
        column_values1 = ["Team", "Goals For", "Goals Against", "Goal Difference", "Points"]
        column_values2 = ["Team", "Goals For", "Goals Against", "Goal Difference", "Points", "Position"]
        runs = 10000
        allsims = []
        for i in range(runs):
            holdtable = []
            self.resetsimulation()
            for m in self.matches:
                if m.toplay:
                    m.simulatematch(self)
            for t in self.teams:
                holdtable.append([t.name, t.goalsfor + t.simgf, t.goalsag + t.simga, t.goalsfor + t.simgf - t.goalsag - t.simga, t.points + t.simpts])
            table = pd.DataFrame(data=np.array(holdtable), columns=column_values1)
            table['Points'] = pd.to_numeric(table['Points'])
            table['Goal Difference'] = pd.to_numeric(table['Goal Difference'])
            table['Goals For'] = pd.to_numeric(table['Goals For'])
            table["Position"] = table[["Points", "Goal Difference", "Goals For"]].apply(tuple, axis=1).rank(ascending=False, method='first')
            table_np = table.to_numpy(copy=True)
            allsims.append(table_np)
        output = pd.DataFrame(np.array(allsims).reshape(20*runs,6), columns=column_values2)
        output.to_csv("simulations.csv", index=False)

    def rebasepens(self):
        spreadpens = 110
        currentpensfor = sum(t.penfor for t in self.teams)
        currentpensag = sum(t.penag for t in self.teams)
        for t in self.teams:
            t.penfor = t.penfor * spreadpens / currentpensfor
            t.penag = t.penag * spreadpens / currentpensag





