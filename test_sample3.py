
import pytest

@pytest.mark.test2
@pytest.mark.parametrize("a,b",[(2,4),(3,4),(4,4)])
def test_addition(a,b):
    c= a+b
    print(c)
    
