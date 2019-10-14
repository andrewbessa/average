import json
import argparse
from . import process_args

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Input file path with events.")
parser.add_argument("-w", "--window_size", default=1, type=int, help="Define the window size in minutes of the average. The default size value is 1 minute.")
parser.add_argument("-o", "--output_file", help="Output file path.")

process_args(parser.parse_args())