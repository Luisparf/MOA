# from constructiveModule import calculateDistance

if __name__ == '__main__':

    lines = []
    dict = {}
    while (line := str(input())) != "EOF":
        line = line.replace('\r', '').split()
        lines.append(line.copy())

    del lines[0:5]

    #print(lines)

    for i in range(1, len(lines)):
        dict["node"] = lines[i][0]  # sei lá se usaremos...
        dict["x"] = lines[i][1]  # same
        dict["y"] = lines[i][2]  # same ^
        lines[i] = dict.copy()

    print(lines)
