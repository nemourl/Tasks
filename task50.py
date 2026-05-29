import re


def breakdown_csv(line):
    pattern = r'"((?:[^"]|"")*)"|([^,]+)'

    res = []

    for quoted, simple in re.findall(pattern, line):
        if quoted:
            res.append(quoted.replace('""', '"'))
        else:
            res.append(simple)

    return res

text = 'hello,"complex, with ""quotes""",world'

print(breakdown_csv(text))