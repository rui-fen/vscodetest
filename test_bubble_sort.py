import unittest

from bubble_sort import bubble_sort


class BubbleSortTests(unittest.TestCase):
    def test_sorts_unsorted_numbers(self):
        self.assertEqual(bubble_sort([5, 3, 8, 4, 2]), [2, 3, 4, 5, 8])

    def test_handles_empty_and_single_item_lists(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([42]), [42])

    def test_keeps_already_sorted_list_in_order(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_sorts_reverse_duplicates_and_negative_numbers(self):
        self.assertEqual(bubble_sort([3, -1, 3, 0, -5]), [-5, -1, 0, 3, 3])
        self.assertEqual(bubble_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_does_not_modify_the_input_list(self):
        numbers = [3, 1, 2]

        result = bubble_sort(numbers)

        self.assertEqual(numbers, [3, 1, 2])
        self.assertEqual(result, [1, 2, 3])
        self.assertIsNot(result, numbers)


if __name__ == "__main__":
    unittest.main()
