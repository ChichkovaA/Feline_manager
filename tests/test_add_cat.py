import pytest
import os
import shutil
from commands.add_cat import add_cat


@pytest.fixture(autouse=True)
def setup_test_space():
    os.makedirs('test_ground')
    os.chdir('test_ground')
    yield
    os.chdir('..')
    shutil.rmtree('test_ground')


def test_add_cat():
    add_cat('test_add_cat')

    assert (os.path.exists('cats'))
    assert (os.path.exists('cats/test_add_cat'))
