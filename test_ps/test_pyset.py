import unittest
from pyset.pyset import PySet
from test_ps.data.get_data import get_simple_csv, get_simple_csv2, get_simple_csv3


class TestPySet(unittest.TestCase):
    def setUp(self):
        self.pytest = PySet()

    def test_read_csv(self):
        data_path = get_simple_csv()
        csv = self.pytest.read_csv(data_path)
        self.assertIsNotNone(csv)

    def test_csv_intersection(self):
        data_path1 = get_simple_csv()
        data_path2 = get_simple_csv2()
        self.pytest.add_csv(data_path1)
        self.pytest.add_csv(data_path2)
        intersect = self.pytest.intersection()
        self.assertEqual(intersect, [("J", "K", "L")])

    def test_csv_intersection_no_results(self):
        data_path1 = get_simple_csv()
        data_path3 = get_simple_csv3()
        self.pytest.add_csv(data_path1)
        self.pytest.add_csv(data_path3)
        intersect = self.pytest.intersection()
        self.assertEqual(len(intersect), 0)
