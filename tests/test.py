from mypackage import myModule

def test_top_n():
    """ 
    Test that top_n works
    """

    assert myModule.top_n([8,5,4,3], 3) == [8,5,4], 'incorrect'
    assert myModule.top_n([12,43,21,20], 3) == [43,21,20], 'incorrect'
    assert myModule.top_n([0,2,5,7], 3) == [7,5,2], 'incorrect'