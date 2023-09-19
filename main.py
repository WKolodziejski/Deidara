import getopt
import os
import sys
from math import ceil
from typing import Callable
from stringreader import StringReader


def print_word(write: Callable[[str], None], word: str, char: chr):
    write(word)

    if char:
        write(char)


def bionize(read: Callable[[int], chr], write: Callable[[str], None], skipnum: int, fixnum: float, symbol: (str, str)):
    word: str = ''
    skipcount = 0
    reading = True
    lastchar = None

    while reading:
        char: chr = read(1)

        if not char:
            reading = False

        if reading and char.isalpha():
            word += char

        else:
            size = len(word)

            if size == 0:
                if char:
                    write(char)
                    lastchar = char
                continue

            if fixnum == 0:
                print_word(write, word, char)
                lastchar = char
                word = ''
                continue

            if skipcount == skipnum and skipnum > 0:
                print_word(write, word, char)
                lastchar = char
                word = ''
                skipcount = 0
                continue

            half = int(ceil(size / (1 / fixnum)))
            bionic = symbol[0]

            for i in range(0, half):
                bionic += word[i]

            bionic += symbol[1]

            for i in range(half, size):
                bionic += word[i]

            print_word(write, bionic, char)
            lastchar = char
            word = ''
            skipcount += 1

    if lastchar != '\n':
        write(os.linesep)


def main(argv):
    opts, args = getopt.getopt(argv, "h f: j: i: o: t:", ["help", "fix=", "skip=", "input=", "output=", "target="])

    inputfilename = None
    outputfilename = None
    skipnum = 0
    fixnum = 50
    argscount = 0
    target = ('**', '**')
    read: Callable[[], chr]
    write: Callable[[str], None]
    inputfile = None
    outputfile = None

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('usage: [-f <fixnum>] [-j <skipnum>] [-i <inputfile>] [-o <outputfile>] [-t <target>]')
            sys.exit()

        elif opt in ('-i', '--input'):
            inputfilename = str(arg)
            argscount += 2

        elif opt in ('-o', '--output'):
            outputfilename = str(arg)
            argscount += 2

        elif opt in ('-f', '--fix'):
            fixnum = int(arg)
            argscount += 2

            if fixnum < 0 or fixnum > 100:
                print('-f should be between 0 and 100')
                sys.exit(1)

        elif opt in ('-j', '--skip'):
            skipnum = int(arg)
            argscount += 2

            if skipnum < 0:
                print('-j should be greater than or equal to 0')
                sys.exit(1)

        elif opt in ('-t', '--target'):
            argscount += 2

            if arg == 'html':
                target = ('<b>', '</b>')

            elif arg in ('md', 'markdown'):
                target = ('**', '**')

            else:
                print('-t should be md or html')
                sys.exit(1)

    if len(argv) != argscount:
        print(f'unknown arguments')
        sys.exit(1)

    try:
        argstr = ''.join(argv[argscount:])

        if inputfilename:
            inputfile = open(inputfilename, 'r')
            read = inputfile.read

        elif argstr:
            reader = StringReader(argstr)
            read = reader.read

        else:
            read = sys.stdin.read

        if outputfilename:
            outputfile = open(outputfilename, 'w')
            write = outputfile.write

        else:
            write = sys.stdout.write

        bionize(read, write, skipnum, fixnum / 100, target)

    except KeyboardInterrupt:
        sys.exit()

    except Exception as e:
        print(e)

    finally:
        if inputfile:
            inputfile.close()

        if outputfile:
            outputfile.close()


if __name__ == "__main__":
    main(sys.argv[1:])
