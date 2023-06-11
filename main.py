from gcodeWriter import gcodeWriter
from gcodeGenerator import gcodeGenerator
import argparse

"""
TODO validation of file (if it exists, if its JPG file).
TODO validation if save file is creatable.
TODO expand argument list on: 
        - output dimensions
"""
def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, required=True, help='JPG file which you want to convert to gcode.')
    parser.add_argument("-s", "--save", type=str, default='./', help='directory to save gcode file. Default is current directory.')
    return parser.parse_args()

if __name__ == '__main__':
    args = init_parser()
    writer = gcodeWriter(args.save)
    generator = gcodeGenerator(args.file)
