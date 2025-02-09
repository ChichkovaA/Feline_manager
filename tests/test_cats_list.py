import pytest
import os
import shutil
from commands.add_cat import add_cat
from commands.cats_list import cats_list


@pytest.fixture(autouse=True)
def setup_test_space():
    os.makedirs('test_ground')
    os.chdir('test_ground')

    yield
    os.chdir('..')
    shutil.rmtree('test_ground')


def test_cats_list():
    add_cat('test_cat_1')
    add_cat('test_cat_2')

    cats = cats_list()

    assert (len(cats) == 2)
    assert ('Test_cat_1' in cats)
    assert ('Test_cat_2' in cats)
