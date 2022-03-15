from scipy.spatial import distance
from input import fileinput ,runinput

if __name__ == '__main__':

    # a = (1, 2)
    # b = (4, 5)
    # print(distance.euclidean(a, b))

    # lines = fileinput()
    lines = runinput()
    dict = {}

    print(lines)

    for i in range(1, len(lines)):
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
