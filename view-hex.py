#!/usr/bin/env python3
import sys


current_line = ""


def parse_hex_line(line):
    global current_line
    if len(current_line) == 0:
        return
    bytecount = int(line[0:2], 16)
    address = int(line[2:6], 16)
    rec_type = int(line[6:8], 16)

    rec_output = str(hex(address)) + '\t(' + str(bytecount) + ')\t'
    if rec_type == 0:
        rec_output += '(data)'
        rec_output += '\t\t' + line[8:(8 + 2 * bytecount)]
    elif rec_type == 1:
        rec_output += '(end of file)'
    elif rec_type == 2:
        rec_output += '(extended segment address)'
    elif rec_type == 3:
        rec_output += '(start segment address)'
    elif rec_type == 4:
        rec_output += '(extended linear address)'
    elif rec_type == 5:
        rec_output += '(start linear address)'
    print(rec_output)


def main():
    global current_line
    if len(sys.argv) != 2:
        print("Usage: view-hex.py <hex-file>")
        sys.exit(1)
    #   (1) Open the Hex File
    hex_file_path = sys.argv[1]
    print("Parsing " + hex_file_path)
    hex_file = open(hex_file_path, "r")

    #   (2) Analyze the hex file line by line
    current_line = ""
    try:
        byte = "1"  # initial placeholder
        while byte != "":
            byte = hex_file.read(1)
            if byte == ":":
                #   (1) Parse the current line!
                parse_hex_line(current_line)
                #   (2) Reset the current line to build the next one!
                current_line = ""
            else:
                current_line += byte
        parse_hex_line(current_line)
    finally:
        hex_file.close()


if __name__ == "__main__":
    main()
