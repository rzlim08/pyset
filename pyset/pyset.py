""" Pyset Module"""
import csv


class PySet:
    """Performs set operations on csvs """
    def __init__(self):
        """initialize PySet class"""
        # Todo: set delimiter
        self.delimiter = ","
        # Todo: set columns
        self.columns = []

    def read_csv(self, path_to_csv):
        """read in csv and subset columns"""
        with open(path_to_csv) as csv_file:
            reader = csv.reader(csv_file, delimiter=self.delimiter)
            if self.columns:
                csvset = [row[column] for row in reader for column in self.columns]
            else:
                csvset = reader

        return csvset
