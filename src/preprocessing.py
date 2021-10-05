import numpy as np
from scipy.stats import rankdata
from typing import List, Union


def read_file(filepath: str):
    """
    Function takes input txt file as input and return 2d array of shape n_samples x 2.
    :param filepath: str
    :return: 2d array of shape n_samples x 2.
    """
    try:
        data = np.loadtxt(filepath)
        assert len(data.shape) == 2 and data.shape[1] == 2, \
            'Please, make sure your input file consists of exactly 2 columns. '
        assert data.shape[0] >= 9, 'Method requires the length of data samples to be more or equal than 9.'
        return data

    except IOError:
        print('Please, make sure your pass to the txt file is correct.')


def write_data(data: List[Union[int, float]], filepath: str):
    """
    Function takes list of 3 numbers and writes data to the txt file.
    :param data: List[Union[int, float]]
    :param filepath: str path to the output file
    :return:
    """
    np.savetxt(filepath, [f'{data[0]} {data[1]} {data[2]}'], fmt="%s")


def sort_and_rank(data: np.ndarray):
    """
    Function takes 2d array of floats as input and return ranks of 2nd dimension of array in sorted order
    of the 1st dimension of an array.
    :param data: np.ndarray[np.float32]
    :return: np.ndarray[np.float32]
    """
    assert (isinstance(data[0][0], float) and isinstance(data[1][0], float)) or (
                isinstance(data[0][0], int) and isinstance(data[1][0], int)), \
        'Input file should consists of integer or float values. '

    sorted_data = data[data[:, 0].argsort()]
    smart_ranks = rankdata(sorted_data[:, 1])
    return smart_ranks
