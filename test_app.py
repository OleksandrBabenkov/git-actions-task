from myapp.app import add, subtract, generate_random_value, jakobi_method


def test_add():

    assert add(2, 3) == 5

def test_subtract():

    assert subtract(2, 3) == -1

def test_random_value():

    assert generate_random_value() == True

# def test_jakubi_method():

#     assert jakobi_method(A=[[1, 2], [3, 4]], b=[5, 6]) == [1, 2]
