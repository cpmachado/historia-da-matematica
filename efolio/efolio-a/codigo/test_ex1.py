import unittest
from ex1 import pentagonal, pentagonal_dk, pentagonal_extensive_sum


class Ex1TestCase(unittest.TestCase):
    def test_pentagonal_dk(self):
        kv = [(1, 1), (2, 4), (3, 7), (4, 10), (5, 13)]

        for k, v in kv:
            actual = pentagonal_dk(k)
            self.assertEqual(actual, v, f"Expected d({k}) = {v} and not {actual}")

    def test_pentagonal(self):
        kv = [(1, 1), (2, 5), (3, 12), (4, 22), (5, 35)]

        for k, v in kv:
            actual = pentagonal(k)
            self.assertEqual(actual, v, f"Expected p({k}) = {v} and not {actual}")

    def test_pentagonal_extensive_sum(self):
        kv = [
            (1, "1"),
            (2, "1 + 4"),
            (3, "1 + 4 + 7"),
            (4, "1 + 4 + 7 + 10"),
            (5, "1 + 4 + 7 + 10 + 13"),
        ]

        for k, v in kv:
            actual = pentagonal_extensive_sum(k)
            self.assertEqual(actual, v, f"Expected p({k}) = {v} and not {actual}")


if __name__ == "__main__":
    unittest.main()
