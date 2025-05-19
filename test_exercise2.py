import exercise2 as test2

def test_find_min_max():
    input_arr = [1, 2, 3, 4, 5, 6, 9]
    result = test2.find_min_max(input_arr)
    assert(result[0] == 1)
    assert(result[1] == 9)

def test_calc_average():
    input_arr = [1, 2, 3, 4, 5, 6]
    result = test2.calc_average(input_arr)
    assert(result == 3.5)

def test_calc_median_temperature():
    input_arr = [1, 2, 3, 4, 5, 6]
    result = test2.calc_median_temperature(input_arr)
    assert(result == 3.5)