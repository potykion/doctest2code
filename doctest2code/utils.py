def doctest_to_code(doctest: str) -> str:
    code_lines = []

    lines = doctest.splitlines()
    for line in lines:
        if line.startswith('>>> ') or line.startswith('... '):
            line = line[4:]
            code_lines.append(line)
        elif code_lines:
            code_lines[-1] = f'assert {code_lines[-1]} == {line}'
        else:
            code_lines.append(line)

    code = '\n'.join(code_lines)
    return code
