from ET0735_Lab2 import all_in_one

def test_min_max():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    min_max = (11, 90)

    result = all_in_one.find_min_max(input_arr)

    assert (result == min_max)

def test_calc_average():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_average = 40.57142857142857

    result = all_in_one.calc_average(input_arr)

    assert (result == test_average)

def test_cal_median():
    assert (all_in_one.cal_median_temperature([43, 456, 23, 46, 35]) == 43)