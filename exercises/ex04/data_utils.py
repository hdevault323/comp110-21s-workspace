"""Utility functions for wrangling data."""

__author__ = "730236759"

from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    rows: list[dict[str, str]] = []
    for row in csv_reader:
        rows.append(row)
    return rows
    file_handle.close()


def column_values(data_rows: list[dict[str, str]], column_name: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    value_of_columns: list[str] = []
    for row in data_rows:
        value_of_columns.append(str(row[column_name]))
    return value_of_columns


def columnar(data_rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms table from a list of rows to a dictionary of columns."""
    dict_cols: dict[str, list[str]] = {}
    col_names = data_rows[0].keys() 
    for i in col_names:
        list_str: list[str] = column_values(data_rows, i)
        dict_cols[i] = list_str 
    return dict_cols


def head(data_cols: dict[str, list[str]], N: int) -> dict[str, list[str]]: 
    """Produces a column based table with N number of rows."""
    new_table: dict[str, list[str]] = {}
    iterations = int(N)
    for column in data_cols:
        first_N_values: list[str] = []
        i = 0
        if iterations > len(data_cols[column]):
            iterations = len(data_cols[column])
        while i < iterations:
            first_N_values.append(data_cols[column][i])
            i += 1
            new_table[column] = first_N_values
    return new_table
 
def select(data_cols: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    return_dict: dict[str, list[str]] = {}
    for item in column_names:
        return_list: list[str] = data_cols[item]
        return_dict[item] = return_list
    return return_dict


def count(values: list[str]) -> dict[str, int]:
    """Produces a dictionary where each key is a unique value in the list."""
    store: dict[str, int] = {}
    for item in values:
        if item in store:
            store[item] += 1
        else:
            store[item] = 1
    return store