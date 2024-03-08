#!/usr/bin/env python3
# Author: Shyamal S. Chandra

from tqdm import tqdm
from mplayer import Player, CmdPrefix
import sys
import time
import datetime

FoodNum = int(sys.argv[1])
FoodFilename = str(sys.argv[2])
PrayerFileName = str(sys.argv[3])
BreathingFileName = str(sys.argv[4])
player = Player()
player.loadfile(BreathingFileName)
time.sleep(player.length)
player.loadfile(PrayerFileName)
time.sleep(player.length)
for i in tqdm(range(FoodNum), desc = 'Chew-Track-I'):
    player.loadfile(FoodFilename)
    time.sleep(player.length)
player.loadfile(PrayerFileName)
time.sleep(player.length)
