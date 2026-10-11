import unittest
import numpy as np
from BoxCounting import BoxCountingE, GetNb


class BoxCountingTests(unittest.TestCase):
    def test_sparse_unsorted_spectrum_keeps_empty_boxes(self):
        counts, left_edges = BoxCountingE([10, 0, 1, 9], 5)
        self.assertEqual(counts, [2, 0, 0, 0, 2])
        self.assertEqual(left_edges, [0, 2, 4, 6, 8])
        self.assertEqual(sum(counts), 4)

    def test_internal_edges_and_maximum(self):
        counts, _ = BoxCountingE([0, 2, 4, 6, 8, 10], 5)
        self.assertEqual(counts, [1, 1, 1, 1, 2])

    def test_constant_spectrum(self):
        counts, left_edges = BoxCountingE([3, 3], 4)
        self.assertEqual(len(counts), 4)
        self.assertEqual(len(left_edges), 4)
        self.assertEqual(sum(counts), 2)

    def test_occupied_boxes_and_powers(self):
        self.assertEqual(GetNb([0, 2, 0, 3], q=0), 2)
        self.assertEqual(GetNb([0, 2, 0, 3], q=2), 13)
        self.assertEqual(GetNb([0, 2, 0, 4], q=-1), 0.75)
        self.assertEqual(GetNb([], q=0), 0)

    def test_invalid_spectra(self):
        for values in ([], [[1, 2]], [1, np.nan], [1, np.inf], [1+2j]):
            with self.subTest(values=values), self.assertRaises(ValueError):
                BoxCountingE(values, 2)
        for bins in (0, -1, 1.5, True):
            with self.subTest(bins=bins), self.assertRaises(ValueError):
                BoxCountingE([1, 2], bins)

    def test_invalid_counts(self):
        for values in ([1, -1], [np.nan], [[1, 2]]):
            with self.subTest(values=values), self.assertRaises(ValueError):
                GetNb(values)


if __name__ == "__main__":
    unittest.main()

