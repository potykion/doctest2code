import pytest

from doctest2code.utils import doctest_to_code


@pytest.mark.parametrize("doctest, code", [
    (
            ">>> sum_ = 0\n>>> for num in range(5):\n...   sum_ += num\n>>> sum_\n10",
            "sum_ = 0\nfor num in range(5):\n  sum_ += num\nassert sum_ == 10"
    ),
    (
            "as\nas\nas",
            "as\nas\nas"
    ),
    (
            ">>> def op(*, oppa=None):\n...   return oppa\n...\n>>> op(oppa=\"oppa\")\n'oppa'",
            "def op(*, oppa=None):\n  return oppa\n\nassert op(oppa=\"oppa\") == 'oppa'"
    )

])
def test_doctest_to_code(doctest, code):
    assert doctest_to_code(doctest) == code
