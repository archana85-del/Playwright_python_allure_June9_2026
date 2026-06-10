
import pytest


@pytest.mark.test
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.negetiveTestcase
def test_sum():
    print("This is a sample test file.")

@pytest.mark.smoke
def test_sum2():
    print("This is a sample test file.")


@pytest.mark.smoke
@pytest.mark.skip
def test_sum2_1():
    print("This is a sample test file.")

@pytest.mark.negetiveTestcase
def test_sum2_2():
    print("This is a sample test file.")


# sum()