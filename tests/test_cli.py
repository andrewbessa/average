import argparse
import json
from pathlib import Path
from . import average


def test_process_args_interface():
    args = argparse.Namespace()
    data_folder = Path("testfile/")
    file_input = data_folder/"events01.json"
    file_output = data_folder/"output.json"
    file_result_expected = data_folder/"result06.txt"
    result_expected = []
    result = []
    
    args.window_size = 1
    args.input_file = file_input
    args.output_file = file_output
    average.process_args(args)

    with open(file_result_expected) as file:
        for event in file:
            result_expected.append(event)
    
    with open(file_output) as file:
        for event in file:
            result.append(event)

    assert result_expected == result


    

    