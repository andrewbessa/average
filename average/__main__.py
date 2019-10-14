import sys
import json
import argparse

from . import translation_delivered_parser, TranslationDelivered, AverageCalc

def process_args(args):
    
    average_calc = AverageCalc(args.window_size)
    for item in translation_delivered_parser(args.input_file):
        average_calc.add_tranlation_delivered(item)
    
    for item in average_calc.cal_avg_delivered_time():
        print(json.dumps({"date": item[0], "average_delivery_time": item[1]}))

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Input file path with events.")
parser.add_argument("-w", "--window_size", default=1, type=int, help="Define the average window size. The default size is 1.")

process_args(parser.parse_args())

