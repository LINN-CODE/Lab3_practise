import Lab2.bmi as bmi

def test_normal_weight():
    result = bmi.calculate_bmi_2(1.72,70)
    assert(result == 0)

def test_under_weight():
    result = bmi.calculate_bmi_2(1.72,50)
    assert(result == -1)

def test_over_weight():
    result = bmi.calculate_bmi_2(1.72,90)
    assert(result == 1)