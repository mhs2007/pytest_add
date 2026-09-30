from add import calulate_add

def test_positive_no():
    assert calulate_add(40,80) == 120

def test_zero():
    assert calulate_add(15,0) == 15

def test_negative_no():
    assert calulate_add(-5,1) == -4
    


    