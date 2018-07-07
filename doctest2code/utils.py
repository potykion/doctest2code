import re
from typing import Iterable


def doctest_to_code(doctest: str) -> str:
    doctest_lines = doctest.splitlines()
    code_lines = _to_code_lines(doctest_lines)
    code = '\n'.join(code_lines)
    return code


def _to_code_lines(lines: Iterable[str]) -> Iterable[str]:
    code_lines = []
    previous_line_is_doctest = False

    for line in lines:
        if line.startswith('>>>') or line.startswith('...'):
            code_lines.append(_strip_doctest_line(line))
            previous_line_is_doctest = True
        elif previous_line_is_doctest:
            code_lines[-1] = f'assert {code_lines[-1]} == {line}'
            previous_line_is_doctest = False
        else:
            code_lines.append(line)
            previous_line_is_doctest = False

    return code_lines


def _strip_doctest_line(line: str) -> str:
    """
    >>> _strip_doctest_line(">>> def op(a)")
    'def op(a)'
    >>> _strip_doctest_line("... return a")
    'return a'
    >>> _strip_doctest_line("... ")
    ''
    >>> _strip_doctest_line("...    ")
    ''
    >>> _strip_doctest_line("...")
    ''
    """
    stripped = re.sub("(>>>|\.\.\.)\s?", "", line)

    if re.match("\s*$", stripped):
        stripped = ""

    return stripped
