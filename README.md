# Deidara

A bionic reading generator.

Inputs a text file and outputs a text file with bold markdown.

# Usage

## Python

``
python3 main.py [<args>]
``

### Arguments

- `-i` input file
- `-o` output file
- `-t` target language [md, html]
- `-j` number of words to skip
- `-f` percentage of word to mark [0 .. 100]

### Example

``
python3 main.py -i my_text.txt -o output_file.md -t md -j 0 -f 50
``

## Shell

``
./bash.sh [<files>]
``

### Example

``
./bash.sh file1.txt file2.txt
``
