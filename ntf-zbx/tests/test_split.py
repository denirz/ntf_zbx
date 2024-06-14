import re

import pytest


def split_(stringin):
    return [x.strip('"') for x in re.findall("(?:\".*?\"|\\S)+", stringin)]


testdata = [
    ('ls -l s-lad asda as- assadasd "asdsa asdasd" asdddd ', 8),
    ('"ls" -l s-lad "asda as- assadasd" "asdsa asdasd" asdddd ', 6),
    ('ls -l', 2),
    ('osx asd 332', 3),
    ('"osx asd" 332', 2),
    ('"osx asd 332', 3),
    ('"osx asd 332', 3),
    ('ls -la "/Users/denirz/Documents/Travels/Uzbekistan 05 24"', 3)
]


@pytest.mark.parametrize(("string", "count"), testdata)
def test_split(string, count):
    spliited = split_(string)
    print(spliited)
    assert len(spliited) == count
