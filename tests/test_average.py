from pathlib import Path
from ast import literal_eval
from . import average

def compare_average_result(average_calc, file_input, file_result):
    result_expected = []
    result = []
    data_folder = Path("testfile/")

    with open(data_folder/file_result) as result_file:
        for item in result_file:
            result_expected.append(literal_eval(item))

    for item in average.translation_delivered_parser(data_folder/file_input):
        average_calc.add_tranlation_delivered(item)
        print(item)

    for item in average_calc.cal_avg_delivered_time():
        result.append(item)

    assert result_expected == result

def test_case_window_size_negative():
    average_calc = average.AverageCalc(-1)
    compare_average_result(average_calc, "events02.json", "result02.txt")

def test_case_window_size_0():
    average_calc = average.AverageCalc(0)
    compare_average_result(average_calc, "events02.json", "result02.txt")

def test_case_window_size_one():
    average_calc = average.AverageCalc(1)
    compare_average_result(average_calc, "events02.json", "result03.txt")

def test_case_file_one_event():
    average_calc = average.AverageCalc(10)
    compare_average_result(average_calc, "events01.json", "result01.txt")    

def test_case_file_three_events_window_10():
    average_calc = average.AverageCalc(10)
    compare_average_result(average_calc, "events02.json", "result04.txt")    

def test_case_file_three_events_window_20():
    average_calc = average.AverageCalc(20)
    compare_average_result(average_calc, "events02.json", "result04.txt")    
