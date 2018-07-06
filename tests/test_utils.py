import pytest

from doctest2code.utils import doctest_to_code


@pytest.fixture()
def doctest():
    return """>>> sum_ = 0
>>> for num in range(5):
...   sum_ += num
>>> sum_
10"""


@pytest.fixture()
def code():
    return """sum_ = 0
for num in range(5):
  sum_ += num
assert sum_ == 10"""


def test_doctest_to_code(doctest, code):
    assert doctest_to_code(doctest) == code
