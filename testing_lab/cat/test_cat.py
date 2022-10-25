from pythonProject.python_oop_course.testing_lab.cat.cat import Cat

import unittest


class CatTests(unittest.TestCase):
    valid_name = "Cat"

    def test_eat__when_valid__expect_size_increased(self):
        cat = Cat(self.valid_name)

        cat.eat()
        self.assertEqual(1, cat.size)

    def test_eat__when_valid__expect_fed_is_True(self):
        cat = Cat(self.valid_name)

        cat.eat()
        self.assertEqual(True, cat.fed)

    def test_eat__when_already_fed__expect_raise_error(self):
        cat = Cat(self.valid_name)

        cat.eat()
        with self.assertRaises(Exception) as context:
            cat.eat()
        self.assertEqual("Already fed.", str(context.exception))

    def test_sleep__when_not_fed__expects_raise_error(self):
        cat = Cat(self.valid_name)

        with self.assertRaises(Exception) as context:
            cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(context.exception))

    def test_sleep__when_sleep__expect_set_sleepy_to_false(self):
        cat = Cat(self.valid_name)
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    unittest.main()
