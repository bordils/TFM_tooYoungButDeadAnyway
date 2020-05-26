
def DirectionFind(x0,y0,x1,y1):
    deltaX = x1 - x0
    deltaY = y1 - y0
    deltaXY = abs(deltaX/deltaY)

    if(deltaXY < 0.5 or deltaXY > 2.0):
                if(deltaXY < 0.5):
                    if(deltaY > 0):
                        return 1
                    else:
                        return 5
                if(deltaXY > 2.0):
                    if(deltaX > 0):
                        return 3
                    else:
                        return 7
    else:
        if(deltaX > 0 and deltaY > 0):
            return 2
        if(deltaX < 0 and deltaY > 0):
            return 4
        if(deltaX < 0 and deltaY < 0):
            return 6
        if(deltaX > 0 and deltaY < 0):
            return 8