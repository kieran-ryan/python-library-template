"""FizzBuzz unit tests."""

import unittest

from pysamplelib.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """Test `fizzbuzz` function with default keyword mapping."""

    def test_fizz(self):
        """`Fizz` returned."""
        for i in [3, 6, 9, 18]:
            print("testing", i)
            self.assertEqual(fizzbuzz(i), "Fizz")

    def test_buzz(self):
        """`Buzz` returned."""
        for i in [5, 10, 20, 25]:
            print("testing", i)
            self.assertEqual(fizzbuzz(i), "Buzz")

    def test_fizz_buzz(self):
        """`FizzBuzz` returned."""
        for i in [15, 30, 45, 60]:
            print("testing", i)
            self.assertEqual(fizzbuzz(i), "FizzBuzz")

    def test_unmapped_keys(self):
        """Digits returned for unmapped keys."""
        for i in [2, 7, 11, 14]:
            print("testing", i)
            self.assertTrue(fizzbuzz(i).isdigit())

    def test_floats(self):
        """Keywords or floats returned with floats as an argument."""
        self.assertEqual(fizzbuzz(3.0), "Fizz")
        self.assertEqual(fizzbuzz(3.5), "3.5")
        self.assertEqual(fizzbuzz(5.0), "Buzz")
        self.assertEqual(fizzbuzz(15.0), "FizzBuzz")


class TestFizzBuzzCustom(unittest.TestCase):
    """Test `fizzbuzz` function with custom keyword mapping."""

    _CUSTOM_KEYWORDS = {
        4: "Biff",
        9: "Fuzz",
    }

    def test_biff(self):
        """`Biff` returned."""
        for i in [4, 8, 12, 16]:
            print("testing", i)
            self.assertEqual(fizzbuzz(i, self._CUSTOM_KEYWORDS), "Biff")

    def test_fuzz(self):
        """`Fuzz` returned."""
        for i in [9, 18, 27, 45]:
            print("testing", i)
            self.assertEqual(fizzbuzz(i, self._CUSTOM_KEYWORDS), "Fuzz")

    def test_biff_fuzz(self):
        """`BiffFuzz` returned."""
        for i in [36, 72, 108, 144]:
            print("testing", i)
            self.assertEqual(fizzbuzz(i, self._CUSTOM_KEYWORDS), "BiffFuzz")

    def test_unmapped_keys(self):
        """Digits returned for unmapped keys."""
        for i in [2, 7, 11, 14]:
            print("testing", i)
            self.assertTrue(fizzbuzz(i, self._CUSTOM_KEYWORDS).isdigit())

    def test_floats(self):
        """Keywords or floats returned with floats as an argument."""
        self.assertEqual(fizzbuzz(4.0, self._CUSTOM_KEYWORDS), "Biff")
        self.assertEqual(fizzbuzz(3.5, self._CUSTOM_KEYWORDS), "3.5")
        self.assertEqual(fizzbuzz(9.0, self._CUSTOM_KEYWORDS), "Fuzz")
        self.assertEqual(fizzbuzz(36.0, self._CUSTOM_KEYWORDS), "BiffFuzz")
