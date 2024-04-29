from solution import solution

def test_solution():
    assert solution('abc', 'bc') == True
    assert solution('abc', 'd') == False
