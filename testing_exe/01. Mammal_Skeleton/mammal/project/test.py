from project.mammal import Mammal


import unittest


class MammalTests(unittest.TestCase):

    def test_init__when_valid_name_type_sound__expected_correct_initialization(self):
        cat = Mammal("Cat", "cat", "Meow")

        self.assertEqual("Cat", cat.name)
        self.assertEqual("cat", cat.type)
        self.assertEqual("Meow", cat.sound)
        self.assertEqual("animals", cat.__Mammal__kindom)

    def test_make_sound__when_correct_initialization__expected_correct_sound(self):
        cat = Mammal("Cat", "cat", "Meow")
        self.assertEqual(f"Cat makes Meow", cat.make_sound())

    # testing already done in init test...
    def test_get_kingdom__when_correct_initialization_expected_correct_kingdom(self):
        cat = Mammal("Cat", "cat", "Meow")
        self.assertEqual("animals", cat.get_kingdom())

    def test_info__when_correct_initialization_expected_correct_info(self):
        cat = Mammal("Cat", "cat", "Meow")
        self.assertEqual(f"Cat is of type cat", cat.info())


if __name__ == "__main__":
    unittest.main()
