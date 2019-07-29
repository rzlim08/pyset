""" Pyset Module"""
import csv
import argparse

class PySet:
    """Performs set operations on csvs """

    def __init__(self):
        """initialize PySet class"""
        # Todo: set delimiter
        self.delimiter = ","
        # Todo: set columns
        self.columns = {}
        # Todo: set csv paths
        self.csv_paths = []
        # Todo: set csvs
        self.csvs = []
        # Todo: set primary
        self.primary = 0

    def add_csv(self, path_to_csv, columns=None):
        self.csv_paths.append(path_to_csv)
        self.columns[path_to_csv] = columns

    def read_csv(self, path_to_csv):
        """read in csv and subset columns"""
        try:
            cols = self.columns[path_to_csv]
        except KeyError:
            cols = None
        with open(path_to_csv) as csv_file:
            reader = csv.reader(csv_file, delimiter=self.delimiter)
            if cols:
                csvset = [tuple(row[column - 1] for column in cols) for row in reader]
            else:
                csvset = [tuple(row) for row in reader]

        return csvset

    def intersection(self):
        """
        make intersection of 2 csvsets
        """
        self.csvs = self.read_csv_list()
        csv0 = self.csvs[0]
        for csv1 in self.csvs[1:]:
            csv0 = self._intersection(csv0, csv1)
        return self.dedupe(csv0)

    def union(self):
        """ create union of 2 csvsets"""
        self.csvs = self.read_csv_list()
        un = []
        for csvset in self.csvs:
            un.extend(csvset)
        return self.dedupe(un)

    def complement(self):
        self.csvs = self.read_csv_list()
        csv0 = self.csvs[0]
        for csv1 in self.csvs[1:]:
            csv0 = self._complement(csv0, csv1)
        return csv0

    def read_csv_list(self):
        return [self.read_csv(csv_path) for csv_path in self.csv_paths]

    @staticmethod
    def _complement(csv0, csv1):
        return [row for row in csv0 if row not in csv1]

    @staticmethod
    def _intersection(csv0, csv1):
        return [row for row in csv0 if row in csv1]

    @staticmethod
    def dedupe(csvset, return_dupes=False):
        """dedupe but keep order
        https://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-whilst-preserving-order"""
        seen = set()
        seen_add = seen.add
        deduped = [row for row in csvset if not (row in seen or seen_add(row))]
        if return_dupes:
            return seen
        return deduped


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="performs set operations on csvs")
    parser.add_argument("csvs", nargs="*")
    print(parser.parse_args())
