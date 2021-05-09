import unittest
from pyset.pyset import PySet
from test_ps.data.get_data import get_double_csv1, get_double_csv2


class TestPySet(unittest.TestCase):
    def setUp(self):
        self.pytest = PySet()

    def test_read_duplicates(self):
        data_path = get_double_csv1()
        data_path2 = get_double_csv2()
        self.pytest.add_csv(data_path, [1])
        self.pytest.add_csv(data_path2, [1])
        self.pytest.set_full_output(True)
        intersect = self.pytest.intersection()
        self.assertEqual(len(intersect), 5)
        self.assertEqual(intersect, [('key1', 'value1'), ('key1', 'value2'), ('key2', 'value3'), ('key3', 'value4'),
                                     ('key1', 'value6')])

