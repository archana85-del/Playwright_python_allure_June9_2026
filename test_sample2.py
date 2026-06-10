
import pytest



def test_sum3(precondition2):
    print("This is a sample test file.")


@pytest.mark.skip
def test_sum5():
    l1 = [1,2]
    print(l1[3])

@pytest.mark.test
def test_sum4():
    print("This is a sample test file.")

