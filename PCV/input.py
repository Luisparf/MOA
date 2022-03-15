############################################# INPUT BY FILE ###############################################

def fileinput():
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


def runinput():

    lines = []
    while (line := str(input())) != "EOF":
        line = line.replace('\r', '').replace('.', '').split()
        lines.append(line.copy())

    del lines[0:5]

    return lines

############################################################################################################
