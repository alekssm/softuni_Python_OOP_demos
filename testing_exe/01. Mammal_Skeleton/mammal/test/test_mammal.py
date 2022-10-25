from project.mammal import Mammal


import unittest


class MammalTests(unittest.TestCase):
    def setUp(self):
        name = "Tom"
        mammal_type = "cat"
        sound = "Meow"
        self.cat = Mammal(name, mammal_type, sound)

    def test_init__when_valid_name_type_sound__expected_correct_initialization(self):
        self.assertEqual("Tom", self.cat.name)
        self.assertEqual("cat", self.cat.type)
        self.assertEqual("Meow", self.cat.sound)

    def test_init__when_valid__expected__correct_private_attribute(self):
        privet_attribute = self.cat._Mammal__kingdom
        privet_result = "animals"
        self.assertEqual(privet_attribute, privet_result)

    def test_make_sound__when_correct_initialization__expected_correct_sound(self):
        expected = f"{self.cat.name} makes {self.cat.sound}"
        actual = self.cat.make_sound()
        self.assertEqual(expected, actual)

    def test_get_kingdom__when_correct_initialization_expected_correct_kingdom(self):
        self.assertEqual("animals", self.cat.get_kingdom())

    def test_info__when_correct_initialization_expected_correct_info(self):
        expected = f"{self.cat.name} is of type {self.cat.type}"
        actual = self.cat.info()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
