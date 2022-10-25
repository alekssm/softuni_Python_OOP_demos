from pythonProject.python_oop_course.testing_lab.List.extended_list import IntegerList


import unittest


class IntegerListTests(unittest.TestCase):

    def test_init__when_valid_sequence__expected_correct_initialization(self):
        ll = IntegerList((1, 2, 3, 4, 7))
        self.assertEqual(list((1, 2, 3, 4, 7)), ll.get_data())

    def test_add__when_element_is_invalid__expected_raise_error(self):
        ll = IntegerList()
        with self.assertRaises(Exception) as context:
            ll.add("str")
        self.assertIsNotNone(context.exception)

    def test_add__when_element_is_valid__expected_to_add_it_to_the_list(self):
        ll = IntegerList(1, 2, 3, 4, 7)
        ll.add(9)
        self.assertEqual([1, 2, 3, 4, 7, 9], ll.get_data())

    def test_remove_index__when_index_is_out_of_range__expected_to_raise_error(self):
        ll = IntegerList(1, 2, 3, 4, 7)
        invalid_index = len(ll.get_data())

        with self.assertRaises(Exception) as context:
            ll.remove_index(invalid_index)
        self.assertIsNotNone(context.exception)

    def test_remove_index__when_index_is_valid_and_list_is_populated__expected_to_remove_el(self):
        ll = IntegerList(1, 2, 3, 4, 7)
        valid_index = len(ll.get_data()) - 1
        ll.remove_index(valid_index)
        self.assertEqual([1, 2, 3, 4], ll.get_data())

    def test_get__when_index_is_out_of_range__expected_to_raise_error(self):
        ll = IntegerList(1, 2, 3, 4, 7)
        invalid_index = len(ll.get_data())

        with self.assertRaises(Exception) as context:
            ll.get(invalid_index)
        self.assertIsNotNone(context.exception)

    def test_get__when_index_valid_and_list_is_populated__expected_to_return_el(self):
        ll = IntegerList(1, 2, 3, 4, 7)
        valid_index = len(ll.get_data()) - 1
        el = ll.get(valid_index)
        self.assertEqual(list((1, 2, 3, 4, 7))[valid_index], el)

    def test_insert__when_el_is_not_valid_index_is_valid__expected_raise_error(self):
        ll = IntegerList(1, 2, 3, 4, 7)
        valid_index = len(ll.get_data()) - 1
        with self.assertRaises(Exception) as context:
            ll.insert(valid_index, "str")
        self.assertIsNotNone(context.exception)

    def test_insert__when_el_is_valid_index_is_not_valid__expected_raise_error(self):
        ll = IntegerList(1, 2, 3, 4, 7)
        invalid_index = len(ll.get_data())
        with self.assertRaises(Exception) as context:
            ll.insert(invalid_index, 9)
        self.assertIsNotNone(context.exception)

    def test_insert__when_el_is_valid_and_index_is_valid__expected_to_insert_el(self):
        ll = IntegerList(1, 2, 3, 4, 7)
        valid_index = len(ll.get_data()) - 1
        ll.insert(valid_index, 9)
        self.assertEqual(ll.get_data(), [1, 2, 3, 4, 9, 7])

    def test_get_biggest__expected_to_get_the_biggest_el(self):
        ll = IntegerList(1, 2, 3, 4, 7)
        self.assertEqual(7, ll.get_biggest())

    def test_get_index__expected_to_return_the_index_of_el_if_in_list(self):
        ll = IntegerList(1, 2, 3, 4, 7)
        self.assertEqual(4, ll.get_index(7))


if __name__ == "__main__":
    unittest.main()