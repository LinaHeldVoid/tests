import unittest

from test_data import patriot_filter, id_filter, stat_review


class TestPack(unittest.TestCase):

    def test_1(self):
        len_data = patriot_filter()
        result = len(len_data)
        expected = 6
        self.assertEqual(result, expected)

    def test_2(self):
        result = id_filter()
        expected = [213, 15, 54, 119, 98, 35]
        self.assertEqual(result, expected)

    def test_3(self):
        report = stat_review()
        data = report.values()
        expected = ['57.14 %', '42.86 %']
        i = 0
        for result in data:
            self.assertEqual(result, expected[i])
            i += 1
