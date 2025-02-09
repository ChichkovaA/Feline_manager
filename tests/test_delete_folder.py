import pytest
import os
import shutil
from commands.add_cat import add_cat
from commands.delete_folder import delete_folder


@pytest.fixture(autouse=True)
def setup_test_space():
    os.makedirs('test_ground')
    os.chdir('test_ground')

    yield
    os.chdir('..')
    shutil.rmtree('test_ground')


def test_delete_folder():
    add_cat('test_cat')

    assert (os.path.exists('cats'))
    assert (os.path.exists('cats/test_cat'))

    delete_folder('test_cat')

    assert (os.path.exists('cats'))
    assert (not os.path.exists('cats/test_cat'))
