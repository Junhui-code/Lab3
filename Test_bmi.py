from Lab2 import BMI

def test_bmi_normal_weight():
    assert (BMI.calculate_bmi(70, 1.75) == 0)
def test_bmi_over_weight():
    assert (BMI.calculate_bmi(100, 1.8) == 1)
def test_bmi_under_weight():
    assert (BMI.calculate_bmi(30, 1.8) == -1)