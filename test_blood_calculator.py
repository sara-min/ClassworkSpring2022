import pytest


@pytest.mark.parametrize("input_HDL, expected", [
    [70, "Normal"],
    [45, "Borderline Low"],
    [20, "Low"]
])  # a decorator
def test_check_HDL(input_HDL, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input_HDL)
    assert answer == expected
    # answer = check_HDL(55)
    # assert answer == "Borderline Low"
    # answer = check_HDL(30)
    # assert answer == "Low"

@pytest.mark.parametrize("input_tupa, input_tupb, inputc, expected", [
    [(1,1), (2,2), 4, 4],
])  # a decorator
def test_function(input_tupa, input_tupb, inputc, expected):
    from blood_calculator import function
    answer = function(input_tupa, input_tupb, inputc)
    assert answer == expected


# def test_check_HDL_borderline():
#     from blood_calculator import check_HDL
#     answer = check_HDL(55)
#     assert answer == "Borderline Low"

# def test_check_HDL_low():
#     from blood_calculator import check_HDL
#     answer = check_HDL(30)
#     assert answer == "Low"
