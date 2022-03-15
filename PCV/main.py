from scipy.spatial import distance

if __name__ == '__main__':

    # a = (1, 2)
    # b = (4, 5)
    # print(distance.euclidean(a, b))

    lines = []
    dict = {}

    ############################################# INPUT BY FILE ###############################################

    f = open('1.in', 'r')
    lines = f.readlines()

    del lines[0:5]

    for i in range(1, len(lines)):
        line = lines[i].replace('\r', '').replace('.', '').split()
        lines[i] = line

    ############################################ RUN.CODES INPUT ##############################################

    '''
    while (line := str(input())) != "EOF":
      line = line.replace('\r', '').replace('.', '').split()
      lines.append(line.copy())

    del lines2[0:5]

    print(lines)
    '''
    ############################################################################################################

    # print(lines)

    for i in range(1, len(lines)-1):
        dict["node"] = lines[i][0]  # sei lá se usaremos...
        dict["x"] = lines[i][1]  # same
        dict["y"] = lines[i][2]  # same ^
        print("\nDicionario: {}".format(dict))

        lines[i] = dict.copy()
        print("Linha:{}".format(lines[i]))

        x1 = int(lines[1]['x'])
        print("\nx = {}".format(x1))
        y1 = int(lines[1]['y'])
        print("y = {}".format(y1))

        x2 = int(lines[i]['x'])
        print("\nx = {}".format(x2))
        y2 = int(lines[i]['y'])
        print("y = {}".format(y2))

        a = (x1, y1)
        b = (x2, x2)
        print("\nEuclidian distance between {} and {} is {}\n".format(a, b, distance.euclidean(a, b)))


    

    f.close()
