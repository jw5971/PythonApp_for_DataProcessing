import argparse


def convert_namespace_to_dict(args):
    """
    Convert Namespace to Dictionary.
    :param args: namespace
    :return: dictionary
    """
    dict_ionary = vars(args)
    return dict_ionary
