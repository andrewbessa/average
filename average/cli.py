import json
from . import translation_delivered_parser, TranslationDelivered, AverageCalc

def process_args(args):
    average_calc = AverageCalc(args.window_size)
    output_file = None
    for event in translation_delivered_parser(args.input_file):
        average_calc.add_tranlation_delivered(event)

    if args.output_file is not None:
        output_file = open(args.output_file,'a')
    
    for event in average_calc.cal_avg_delivered_time():
        line = json.dumps({"date": event[0], "average_delivery_time": event[1]})
        print(line, file=output_file)

    if output_file is not None:
        output_file.close()