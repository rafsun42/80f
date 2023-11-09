import sys

COL = 80


def main(argv:list[str])->None:
    infilename = argv[1]
    infile = open(infilename, 'r')
    outfile = sys.stdout

    while True:
        linein = infile.readline()
        if not linein:
            break

        lineout = breakline(linein)
        outfile.write(lineout)

    infile.close()


def breakline(line:str)->str:
    """
    Breaks the line into multiple short lines
    each less than COL in length
    """
    # str to char array
    linearr = [c for c in line]
    linelen = len(linearr)

    # line already too short
    if linelen <= COL:
        return ''.join(linearr)
    
    # breaks the line
    start = 0
    prefix = whitespace_prefix(linearr)
    while True:
        # after breaking the line adds whitespace padding
        # from the original line
        breakidx = get_last_spaceidx(linearr, start, COL-len(prefix))
        linearr[breakidx] = '\n' + prefix
        start = breakidx + 1

        if breakidx == linelen - 1:
            break

    return ''.join(linearr)


def get_last_spaceidx(linearr:list[str], start:int, max:int)->int:
    """
    Returns the last index of space within the range-
        [start, start + max)
    """
    # last index of space within that range
    # starts with this random guess
    last_spaceidx = start + max

    # last possible index of linearr
    last_idx = len(linearr) - 1

    # this assumes that last_idx is '\n'
    if last_spaceidx > last_idx:
        return last_idx

    # guess is correct
    if linearr[last_spaceidx] == ' ':
        return last_spaceidx
    
    # if guess is incorrect,
    # walks back until finds a space
    while linearr[last_spaceidx] != ' ':
        last_spaceidx = last_spaceidx - 1

        # TODO: what if last_spaceidx becomes < start
        # while walking back

    return last_spaceidx


def whitespace_prefix(linearr:list[str])->str:
    """
    Returns the whitespace prefix of linearr.
    """
    prefixarr = []
    i = 0

    while True:
        if linearr[i] not in [' ', '\t']:
            break

        prefixarr.append(linearr[i])
        i = i + 1
    
    return ''.join(prefixarr)

main(sys.argv)

