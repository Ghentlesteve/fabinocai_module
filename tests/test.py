from mypackage import myModule

def test_top_n_function():
    """Test the top_n function from myModule."""

    assert myModule.top_n([1, 3, 2, 5, 4], 3) == [5, 4, 3], "Test Case 1 Failed"
    assert myModule.top_n([10, 20, 30, 40, 50], 2) == [50, 40], "Test Case 2 Failed"
    assert myModule.top_n([5, 1, 3, 7, 9], 4) == [9, 7, 5, 3], "Test Case 3 Failed"
    