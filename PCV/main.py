if __name__ == '__main__':

    lines = []
    while (line := str(input())) != "EOF":
        line = line.replace('\r', '')
        lines.append(line)

    del lines[0:5]
    print(lines)
