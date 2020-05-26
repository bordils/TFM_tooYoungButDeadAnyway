'''
BALL HIT DISCRIMINATION.
this piece of code attempts to find out which padel player hits the ball in a game.
Our Iput is the file 'plays.csv' it contains the following fields.
The video is played at 25fps.

    CONTROL INFO:
        first control column with line number (int).
    
    TIME PLACING INFO:
        Frame (int): number of the frame we are on
        Time (float): second corresponding to the footage.
        Play (int): number of the play of the game.

    PLAY INFO:
        Winner (B/T): top or bottom, the team that ends up winning the point (binary)
        Service(TR,TL,BR,BL): who serves at the start of the play (enum[TR,TL,BR,BL])

    LENGTH INFO:
        PlayStart (int): frame at which the play this frame belongs to started
        PlayEnd (int): frame at which the play this frame belongs to ends

    PLAYER POSITION INFO:
        PlayerTR-x
        PlayerTR-y
        PlayerTL-x
        PlayerTL-y
        PlayerBL-x
        PlayerBL-y
        PlayerBR-x
        PlayerBR-y

Our First approach is, knowhing who started the game, choosing the player from the 
opposing team that completes the longest distance between shots.
Before that, we have to be able to identify when the ball gets hit.
First we are going through the video to manually identify who and when hits the ball.

'''


import math

from enum import Enum
from module1 import DirectionFind

class Direction(Enum):
    RIGHT = 1
    DIAGONAL_RU = 2
    UP = 3
    DIAGONAL_LU = 4
    LEFT = 5
    DIAGONAL_LD = 6
    DOWN = 7
    DIAGONAL_RD = 8

frames = [line.rstrip().split(',') for line in open('../data/plays.csv')]

TRdistances = []
TLdistances = []
BRdistances = []
BLdistances = []

'''
x1 = float(frames[4][8])
y1 = float(frames[4][9])
x0 = float(frames[3][8])
y0 = float(frames[3][9])

d = Direction(DirectionFind(x0,y0,x1,y1))

print("this is a test")
print(d)
print("end of the test")
'''


for i in range(2,330):
    TRx1 = float(frames[i][8])
    TRy1 = float(frames[i][9])
    TRx0 = float(frames[i - 1][8])
    TRy0 = float(frames[i - 1][9])
    TRdistance = math.sqrt( math.pow((TRx1 - TRx0),2) + math.pow((TRy1 - TRy0),2) )
    d = Direction(DirectionFind(TRx0,TRy0,TRx1,TRy1))

    print(d)

    TRdistances.append(TRdistance)

    TLx1 = float(frames[i][10])
    TLy1 = float(frames[i][11])
    TLx0 = float(frames[i - 1][10])
    TLy0 = float(frames[i - 1][11])
    TLdistance = math.sqrt( math.pow((TLx1 - TLx0),2) + math.pow((TLy1 - TLy0),2) )
    TLdistances.append(TLdistance)

    BRx1 = float(frames[i][12])
    BRy1 = float(frames[i][13])
    BRx0 = float(frames[i - 1][12])
    BRy0 = float(frames[i - 1][13])
    BRdistance = math.sqrt( math.pow((BRx1 - BRx0),2) + math.pow((BRy1 - BRy0),2) )
    BRdistances.append(BRdistance)

    BLx1 = float(frames[i][14])
    BLy1 = float(frames[i][15])
    BLx0 = float(frames[i - 1][14])
    BLy0 = float(frames[i - 1][15])
    BLdistance = math.sqrt( math.pow((BLx1 - BLx0),2) + math.pow((BLy1 - BLy0),2) )
    BLdistances.append(BLdistance)

    

distanceSumsTR = 0
distanceSumsTL = 0
distanceSumsBR = 0
distanceSumsBL = 0

for i in range(len(TRdistances)):
    distanceSumsTR += TRdistances[i]

print('Top Right total Distance: ')
print(distanceSumsTR)


for distance in TLdistances:
    distanceSumsTL += distance

print('Top Left total distance: ') 
print(distanceSumsTL)

for distance in BRdistances:
    distanceSumsBR += distance

print('Bottom Right total distance: ')
print(distanceSumsBR)

for distance in BLdistances:
    distanceSumsBL += distance

print('Bottom Left total distance: ')
print(distanceSumsBL)




#####################################################################################
'''

i = 0
with open('../data/plays.csv') as file:
    if(i < 328):
        for frame in file:
            strippedLine = frame.rstrip().split(',')
            ++i
            print(strippedLine)


'''