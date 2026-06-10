
import pytest


@pytest.fixture(scope="session")
def precondition():
    print("launching amazon")
    yield
    print("closing amazon")


# @pytest.fixture(autouse=True)
# def precondition1():
#     print("amazon1")


@pytest.fixture(scope="function")
def precondition2():
    print("amazon2")
    yield
    print("amazon2 closing")


def test_m1(precondition2):
    # precondition()
    print("test_m1")



def test_m2(precondition2):
    # precondition()
    print("test_m2")




def test_m3(precondition2):
    # precondition()
    print("test_m3")