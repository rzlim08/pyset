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
        # Todo: set csv paths
        self.csv_paths = []
        # Todo: set csvs
        self.csvs = []

    def add_csv(self, path_to_csv):
        self.csv_paths.append(path_to_csv)

    def read_csv(self, path_to_csv):
        """read in csv and subset columns"""
        with open(path_to_csv) as csv_file:
            reader = csv.reader(csv_file, delimiter=self.delimiter)
            if self.columns:
                csvset = [row[column] for row in reader for column in self.columns]
            else:
                csvset = [tuple(row) for row in reader]

        return csvset

    def intersection(self):
        """
        make intersection of 2 csvsets
        """
        self.csvs = [self.read_csv(csv_path) for csv_path in self.csv_paths]
        csv0 = self.csvs[0]
        for csv1 in self.csvs[1:]:
            csv0 = self._intersection(csv0, csv1)
        return csv0

    def _intersection(self, csv0, csv1):
        return [row for row in csv0 if row in csv1]

    def dedupe(self, csvset):
        """dedupe but keep order
        https://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-whilst-preserving-order"""
        seen = set()
        seen
