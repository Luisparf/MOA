############################################# INPUT BY FILE ###############################################


def fileinput():
    """

    Apenas para uma versão futura...

    """
    f = open('1.in', 'r')
    lines = f.readlines()

    del lines[0:5]
    lines.pop()

    for i in range(1, len(lines)):
        line = lines[i].replace('\r', '').replace('.', '').split()
        lines[i] = line

    f.close()
    return lines


############################################ RUN.CODES INPUT ##############################################

def runcodesinput():
    lines = []
    while (line := str(input())) != "EOF":
        line = line.replace('\r', '').replace('.', '').split()
        lines.append(line.copy())

    del lines[0:5]

    lines = formatnode(lines)
    return lines


############################################################################################################

def formatnode(lines):
    dict = {}

    for i in range(1, len(lines)):
        # dict["node"] = lines[i][0]  # sei lá se usaremos...
        dict["x"] = lines[i][1]
        dict["y"] = lines[i][2]

        lines[i] = dict.copy()
        # print('\n'.join("{}: {}".format(k, v) for k, v in lines[i].items()))

        '''
        x1 = int(lines[1]['x'])
        y1 = int(lines[1]['y'])

        x2 = int(lines[i]['x'])
        y2 = int(lines[i]['y'])

        a = [x1, y1]
        b = [x2, y2]
        # print("Euclidian distance between node {}{} and node {}{} is {}\n".format(1, a, i, b, distance.euclidean(a, b)))
        # print("Euclidian distance between node {}{} and node {}{} is {}\n".format(1, a, i, b, dist(a, b)))
        '''
    return lines
