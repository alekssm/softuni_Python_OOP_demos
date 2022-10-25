from pythonProject.python_oop_course.testing_lab.List.extended_list import IntegerList


import unittest


class IntegerListTests(unittest.TestCase):
    valid_sequence = (1, 2, 3, 4, 7)
    valid_el = 9
    invalid_el = "a"

    def test_init__when_valid_sequence__expected_correct_initialization(self):
        ll = IntegerList(self.valid_sequence)
        self.assertEqual(ll.get_data(), list(map(int, self.valid_sequence)))

    def test_add__when_element_is_invalid__expected_raise_error(self):
        ll = IntegerList()
        with self.assertRaises(Exception) as context:
            ll.add(self.invalid_el)
        self.assertIsNotNone(context.exception)

    def test_add__when_element_is_valid__expected_to_add_it_to_the_list(self):
        ll = IntegerList(self.valid_sequence)
        ll.add(self.valid_el)
        self.assertEqual(ll.get_data(), [1, 2, 3, 4, 7, 9])

    def test_remove_index__when_index_is_out_of_range__expected_to_raise_error(self):
        ll = IntegerList(self.valid_sequence)
        invalid_index = len(ll.get_data())

        with self.assertRaises(Exception) as context:
            ll.remove_index(invalid_index)
        self.assertIsNotNone(context.exception)

    def test_remove_index__when_index_is_valid_and_list_is_populated__expected_to_remove_el(self):
        ll = IntegerList(self.valid_sequence)
        valid_index = len(ll.get_data()) - 1
        ll.remove_index(valid_index)
        self.assertEqual(ll.get_data(), [1, 2, 3, 4])

    def test_get__when_index_is_out_of_range__expected_to_raise_error(self):
        ll = IntegerList(self.valid_sequence)
        invalid_index = len(ll.get_data())

        with self.assertRaises(Exception) as context:
            ll.get(invalid_index)
        self.assertIsNotNone(context.exception)

    def test_get__when_index_valid_and_list_is_populated__expected_to_return_el(self):
        ll = IntegerList(self.valid_sequence)
        valid_index = len(ll.get_data()) - 1
        el = ll.get(valid_index)
        self.assertEqual(el, self.valid_sequence[-1])

