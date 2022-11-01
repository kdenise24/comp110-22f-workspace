"""Dictionary related utility functions."""

__author__ = "730566062"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(origin_table: dict[str, list[str]], numberof_rows: int) -> dict[str, list[str]]:
    """Produces a new dict with the first `numberof_row` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in origin_table:
        i: int = 0
        if len(origin_table[column]) <= numberof_rows:
            return origin_table
        else: 
            while i < numberof_rows:
                n_list: list[str] = []
                n_list.append((origin_table[column])[i])
                i += 1
            result[column] = n_list
    return result


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a new dict table with only a specific subset of columns."""
    result: dict[str, list[str]] = {}
    for item in names:
        result[item] = column_table[item]
    return result


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in first:
        result[column] = first[column]
    for column in second:
        if column in result:
            result[column] = result[column] + second[column]
        else:
            result[column] = second[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str] = {}
    for item in values:
        if item in result:
            result[item] = result[item] + 1
        else:
            result[item] = 1
    return result