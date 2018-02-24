def printLevelArray():
    layer = [["  0,"] * 32] * 32
    for row in range(32):
        for col in range(32):
            print(layer[row][col], end = "")
        print()
            
printLevelArray()