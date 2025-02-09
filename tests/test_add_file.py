import pytest
import os
import shutil
from commands.add_cat import add_cat
from commands.add_file import add_file


@pytest.fixture(autouse=True)
def setup_test_space():
    os.makedirs('test_ground')
    os.chdir('test_ground')
    os.makedirs('test_folder_to_add/')
    with open('test_file_1.txt', 'w') as f:
        f.write('1')
    with open(os.path.join('test_folder_to_add', 'test_file_2.txt'), 'w') as f:
        f.write('2')

    yield
    os.chdir('..')
    shutil.rmtree('test_ground')


def test_add_file():
    add_cat('test_add_cat')

    assert (os.path.exists('cats'))
    assert (os.path.exists('cats/test_add_cat'))

    add_file('test_file_1.txt', 'test_add_cat')
    add_file('test_folder_to_add', 'test_add_cat')

    assert (os.path.exists('cats/test_add_cat/test_file_1.txt'))
    assert (os.path.exists('cats/test_add_cat/test_folder_to_add'))
    assert (os.path.exists('cats/test_add_cat/test_folder_to_add/test_file_2.txt'))
