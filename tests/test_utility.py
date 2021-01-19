# -*- coding: utf-8 -*-

import os

import pytest

from files import file_read
from directories import directory_create, directory_delete
from democritus_utility import (
    request_or_read,
    is_sorted,
    first_unsorted_value,
    last_unsorted_value,
    unsorted_values,
    sorted_values,
    unique_items,
    atomic_write,
    prettify,
)

TEST_DIRECTORY_PATH = './test_files'
NON_EXISTENT_FILE_PATH = './foo'
TEST_FILE_NAME = 'a'
EXISTING_FILE_PATH = os.path.join(TEST_DIRECTORY_PATH, TEST_FILE_NAME)


def test_atomic_write_docs_1():
    directory_create(TEST_DIRECTORY_PATH)
    FILE_CONTENTS = 'foo'

    with atomic_write(EXISTING_FILE_PATH) as f:
        f.write(FILE_CONTENTS)
    assert file_read(EXISTING_FILE_PATH) == FILE_CONTENTS

    with atomic_write(EXISTING_FILE_PATH) as f:
        f.write(FILE_CONTENTS)
    assert file_read(EXISTING_FILE_PATH) == FILE_CONTENTS

    # if we try to write to an existing file with `overwrite=False`, we will get an error
    with pytest.raises(FileExistsError):
        with atomic_write(EXISTING_FILE_PATH, overwrite=False) as f:
            f.write(FILE_CONTENTS)

    directory_delete(TEST_DIRECTORY_PATH)


def test_unique_items_1():
    result = unique_items([1, 2, 3], [2, 3, 4])
    assert result == {'a': {1}, 'b': {4}}

    # TODO: as of September 2020, this is failing... not sure if we should add a work around or not
    # result = unique_items([{'a': 1}, {'b': 2}], [{'a': 1}, {'c': 2}])
    # assert result == {'a': [{'b': 1}], 'b': [{'c': 1}]}


def test_unsorted_values_1():
    l = [1, 2, 4, 3]
    results = list(unsorted_values(l))
    assert results == [4, 3]

    l = [1, 3, 2, 4]
    results = list(unsorted_values(l, descending=True))
    assert results == [1, 4]

    l = [1, 2, 1, 3]
    results = list(unsorted_values(l))
    assert results == [2, 1]


def test_sorted_values_1():
    l = [1, 2, 4, 3]
    results = list(sorted_values(l))
    assert results == [1, 2]

    l = [1, 3, 2, 4]
    results = list(sorted_values(l, descending=True))
    assert results == [3, 2]

    l = [1, 2, 1, 3]
    results = list(sorted_values(l))
    assert results == [1, 3]


def test_last_unsorted_value_1():
    l = [1, 2, 3, 4]
    assert last_unsorted_value(l) == None
    assert last_unsorted_value(l, descending=True) == 4

    l = [4, 3, 2, 1]
    assert last_unsorted_value(l) == 1
    assert last_unsorted_value(l, descending=True) == None

    l = 'abc'
    assert last_unsorted_value(l) == None
    assert last_unsorted_value(l, descending=True) == 'c'

    l = 'cdf'
    assert last_unsorted_value(l) == None
    assert last_unsorted_value(l, descending=True) == 'f'

    l = 'cba'
    assert last_unsorted_value(l) == 'a'
    assert last_unsorted_value(l, descending=True) == None


def test_first_unsorted_value_1():
    l = [1, 2, 3, 4]
    assert first_unsorted_value(l) == None
    assert first_unsorted_value(l, descending=True) == 1

    l = [4, 3, 2, 1]
    assert first_unsorted_value(l) == 4
    assert first_unsorted_value(l, descending=True) == None

    l = 'abc'
    assert first_unsorted_value(l) == None
    assert first_unsorted_value(l, descending=True) == 'a'

    l = 'cdf'
    assert first_unsorted_value(l) == None
    assert first_unsorted_value(l, descending=True) == 'c'

    l = 'cba'
    assert first_unsorted_value(l) == 'c'
    assert first_unsorted_value(l, descending=True) == None


@pytest.mark.network
def test_request_or_read_1():
    s = os.path.abspath(os.path.join(os.path.dirname(__file__), './utility.py'))
    result = request_or_read(s)
    assert 'def request_or_read(path):' in result

    s = 'https://hightower.space/projects'
    result = request_or_read(s)
    assert 'Floyd Hightower' in result


def test_is_sorted_1():
    l = [1, 2, 3, 4]
    assert is_sorted(l)

    l = [4, 3, 2, 1]
    assert not is_sorted(l)
    assert is_sorted(l, descending=True)

    l = 'abc'
    assert is_sorted(l)

    l = 'cdf'
    assert is_sorted(l)

    l = 'cba'
    assert not is_sorted(l)


def test_prettify_1():
    d = {'nums': [i for i in range(0, 10)], 'ids': 'a' * 64}
    result = prettify(d)
    assert (
        result
        == '''{'ids': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
 'nums': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}'''
    )
