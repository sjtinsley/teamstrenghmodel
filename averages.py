from teams2223 import *
import numpy as np

teams = [arsenal, astonvilla, bournemouth, brentford, brighton, chelsea, palace, everton, fulham, leeds, leicester,
             liverpool, mancity, manutd, newcastle, forest, southampton, tottenham, westham, wolves]

goalsavg = sum(t.attack for t in teams) / 20
finattavg = sum(t.finatt for t in teams) / 20
findefavg = sum(t.findef for t in teams) / 20
npgavg = sum(t.npxgattack for t in teams) / 20
