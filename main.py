import unittest


def is_bulky(width_cm: float, height_cm: float, length_cm: float) -> bool:

    if width_cm <= 0 or height_cm <= 0 or length_cm <= 0:
        raise ValueError(f"Dimensions cannot be zero or less")

    if width_cm * height_cm * length_cm >= 1000000.0:
        return True

    return False


def is_heavy(weight_kg: float) -> bool:

    if weight_kg <= 0:
        raise ValueError(f"Weight cannot be zero or less -> {weight_kg}")

    if weight_kg >= 20.0:
        return True

    return False


def sort(width_cm: float, height_cm: float, length_cm: float, weight_kg: float) -> str:

    if is_bulky(width_cm, height_cm, length_cm) and is_heavy(weight_kg):
        return "REJECTED"

    if is_bulky(width_cm, height_cm, length_cm) or is_heavy(weight_kg):
        return "SPECIAL"

    return "STANDARD"


class TestSortingFunctions(unittest.TestCase):
    def test_is_bulky(self):
        self.assertTrue(is_bulky(100, 100, 100))
        self.assertFalse(is_bulky(10, 10, 10))
        with self.assertRaises(ValueError):
            is_bulky(100, 100, 0)

    def test_is_heavy(self):
        self.assertTrue(is_heavy(20))
        self.assertFalse(is_heavy(10))
        with self.assertRaises(ValueError):
            is_heavy(0)

    def test_sort(self):
        self.assertEqual(sort(99, 99, 99, 19.99), "STANDARD")
        self.assertEqual(sort(99, 99, 99, 20), "SPECIAL")
        self.assertEqual(sort(100, 100, 100, 19.99), "SPECIAL")
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        with self.assertRaises(ValueError):
            sort(100, 100, 100, 0)
        with self.assertRaises(ValueError):
            sort(100, 100, 0, 20)


if __name__ == '__main__':
    unittest.main()
