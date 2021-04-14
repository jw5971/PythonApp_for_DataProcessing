import logging
import pandas as pd
import os


def read(description, path, file_type='excel', separator=',', skip_rows=0, use_cols=None, sheet_name=0):
    """
    Read file, along with validating provided path.
    :param description: str; File description
    :param path: str; Fully qualified file name to read
    :param file_type: str, default='Excel'; Read type with possible values of 'csv' or 'excel'
    :param separator: str, default=','; Values separator
    :param skip_rows: int, default=0; Number of rows to skip
    :param use_cols: int, default=None; A list of columns to read (all others are discarded)
    :param sheet_name: int or str; default=0; A sheet name or index to read
    :return: pd.DataFrame; Resulted dataframe
    """
    df_target = None
    if validate_path(path):
        if file_type.lower() == 'csv':
            # Read csv based file.
            df_target = pd.read_csv(path, sep=separator, skiprows=skip_rows, usecols=use_cols)
        elif file_type.lower() == 'excel':
            # Read Excel based file.
            if len((pd.ExcelFile(path)).sheet_names) > 1:
                df_target = pd.read_excel(path, skiprows=skip_rows, sheet_name=sheet_name)
            else:
                df_target = pd.read_excel(path, skiprows=skip_rows)

    logging.info(f'{description} records <{len(df_target.index)}> were read from <{path}>')
    return df_target


def validate_path(path, file_mode=True):
    """
    Validate provided path.
    :param path: Fully qualified file path
    :param file_mode: bool; default=True; Validate file or directory
    :return: bool; Resulted validation; either true or raise an exception
    """
    if (file_mode and os.path.isfile(path)) or (not file_mode and os.path.isdir(path)):
        return True

    logging.error(f'Provided file path is invalid: <{path}>')
    raise FileNotFoundError(f'Provided file path is invalid: <{path}>')


def write(df, description, path, file_type, index, separator=',', mode='overwrite'):
    """
    Write file, along with validating provided path.
    :param df: pd.DataFrame; Provided dataframe
    :param description: str; File description
    :param path: str; Fully qualified file name to read
    :param file_type: str, default='Excel'; Read type with possible values of 'csv' or 'excel'
    :param index: bool; Index to write
    :param separator: str, default=','; Values separator
    :param skip_rows: int, default=0; Number of rows to skip
    :param use_cols: int, default=None; A list of columns to read (all others are discarded)
    :param sheet_name: int or str; default=0; A sheet name or index to read
    :return: null
    """
    # TODO: Enhance the code to construct new file name, based on the mode parameter.
    path_part, file_port = os.path.split(path)
    if validate_path(path_part, False):
        if file_type.lower() == 'csv':
            # Write CSV based file.
            df.to_csv(path, index=index, sep=separator)
        elif file_type.lower() == 'excel':
            # Write Excel based file.
            with pd.ExcelWriter(path, engine='xlsxwriter') as excel_handler:
                df.to_excel(excel_handler, index=index)
        logging.info(f'{description} records <{len(df.index)}> were written to <{path}>')

