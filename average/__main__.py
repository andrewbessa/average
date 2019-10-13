import sys
import json

from . import translation_delivered_parser, TranslationDelivered, AverageCalc

def help():
    print("--window_size : Define the average window size. Mandatory argument")
    print("--input_file  : Input file path. Mandatory argument")

def process_args(argv):
    result = {}
    
    if "--window_size" in argv and "--input_file" in argv:
        result["window_size"] = argv[argv.index("--window_size") + 1]  
        result["input_file"] = argv[argv.index("--input_file") + 1]
    else:
        help()
    
    return result

def main():
    args = process_args(sys.argv)
    
    if len(args) > 0:
        average_calc = AverageCalc(args["window_size"])
        for item in translation_delivered_parser(args["input_file"]):
            average_calc.add_tranlation_delivered(item)
        
        for item in average_calc.cal_avg_delivered_time():
            print(json.dumps({"date": item[0], "average_delivery_time": item[1]}))

main()