import argparse
import numpy as np
from src.preprocessing import read_file, sort_and_rank, write_data
from resources import DATA_PATH


def configure_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument('-i', '--input_file_path',
                        type=str,
                        default=DATA_PATH.parent / 'in.txt',
                        help='Path to input txt tile. ')

    parser.add_argument('-o', '--output_file_path',
                        type=str,
                        default=DATA_PATH.parent / 'out.txt',
                        help='Path to output txt tile. ')


def count_rank_sum(ranks: np.ndarray):
    """
    Function takes an array of ranks and returns sums of first and last N / 3 ranks.
    :param ranks: np.ndarray of ranks
    :return: Tuple[float, float]
    """
    p = round(ranks.shape[0] / 3)
    first_p_ranks_sum = np.sum(ranks[:p])
    last_p_ranks_sum = np.sum(ranks[ranks.shape[0] - p:])

    rank_sum_difference = round(first_p_ranks_sum - last_p_ranks_sum)
    standard_error = round((ranks.shape[0] + 0.5) * ((p / 6) ** 0.5))
    conjugacy_value = round(rank_sum_difference / (p * (ranks.shape[0] - p)), 2)
    return [rank_sum_difference, standard_error, conjugacy_value]


def main(input_file_path: str, output_file_path: str):
    """
    Function takes filepath to the input file and writes difference between r1 and r2, standard error and conjugacy
    value to the output file in the same directory.
    :param input_file_path: str
    :param output_file_path: str
    :return: None
    """

    input_data = read_file(input_file_path)
    ranks = sort_and_rank(input_data)
    output_data = count_rank_sum(ranks)
    write_data(output_data, output_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    configure_arguments(parser)
    args = parser.parse_args()
    main(args.input_file_path, args.output_file_path)
