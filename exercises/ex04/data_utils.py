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
    values_of_columns: list[str] = []
    for row in data_rows
        value_of_columns.append(str(row["subject_age]))
    return values_of_columns


    return rows


# TODO: Define the other functions here.

