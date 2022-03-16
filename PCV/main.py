from scipy.spatial import distance
from input import fileinput ,runinput

if __name__ == '__main__':

    # lines = fileinput()
    lines = runinput()
    dict = {}

    print(lines)

    for i in range(1, len(lines)):
        dict["node"] = lines[i][0]  # sei lá se usaremos...
        dict["x"] = lines[i][1]  # same
        dict["y"] = lines[i][2]  # same ^

        lines[i] = dict.copy()
        print(lines[i])

        x1 = int(lines[1]['x'])
        y1 = int(lines[1]['y'])

        x2 = int(lines[i]['x'])
        y2 = int(lines[i]['y'])

        a = (x1, y1)
        b = (x2, x2)
        print("Euclidian distance between node {}{} and node {}{} is {}\n".format(1, a, i, b, distance.euclidean(a, b)))
