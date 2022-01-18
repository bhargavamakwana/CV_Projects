import argparse

def argument_parser():
    """
    Utility function to parse the arguments
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("--path", type=str, required=True)

    args = parser.parse_args()

    return args
