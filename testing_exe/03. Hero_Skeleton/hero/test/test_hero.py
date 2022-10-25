from project.hero import Hero


import unittest


class HeroTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Hero", 80, 100, 200)

    def test_init__when_valid_username_hp_damage_lvl__expected_correct_initialization(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(200, self.hero.damage)
        self.assertEqual(80, self.hero.level)

    def test_battle__when_enemy_username_is_equal_to_hero_username__expected_to_raise_exception(self):
        enemy_hero = Hero(self.hero.username, 80, 100, 80)
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_battle__when_hero_hp_is_0__expected_to_raise_exception(self):
        hero = Hero("Hero", 80, 0, 200)
        enemy_hero = Hero("Villain", 80, 100, 80)
        with self.assertRaises(ValueError) as context:
            hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle__when_enemy_hero_hp_is_0__expected_to_raise_exception(self):
        enemy_hero = Hero("Villain", 80, 0, 80)
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(context.exception))

    def test_battle__when_both_heroes_hp_is_0_or_less_after_battle__expected_to_return_draw(self):
        enemy_hero = Hero("Villain", 80, 100, 200)
        expected = "Draw"
        hero_expected_health = self.hero.health - enemy_hero.level * enemy_hero.damage
        enemy_hero_expected_health = enemy_hero.health - self.hero.level * self.hero.damage
        actual = self.hero.battle(enemy_hero)
        self.assertEqual(expected, actual)
        self.assertEqual(hero_expected_health, self.hero.health)
        self.assertEqual(enemy_hero_expected_health, enemy_hero.health)

    def test_battle__when_enemy_hero_reaches_0_or_less_after_battle__expected_to_win(self):
        enemy_hero = Hero("Villain", 1, 100, 10)
        expected = "You win"
        hero_expected_health = (self.hero.health - enemy_hero.level * enemy_hero.damage) + 5
        enemy_hero_expected_health = enemy_hero.health - self.hero.level * self.hero.damage
        hero_expected_lvl = self.hero.level + 1
        hero_expected_damage = self.hero.damage + 5

        actual = self.hero.battle(enemy_hero)
        self.assertEqual(expected, actual)
        self.assertEqual(hero_expected_health, self.hero.health)
        self.assertEqual(hero_expected_lvl, self.hero.level)
        self.assertEqual(hero_expected_damage, self.hero.damage)
        self.assertEqual(enemy_hero_expected_health, enemy_hero.health)

    def test_battle__when_hero_reaches_0_or_less_after_battle__expected_to_lose(self):
        hero = Hero("Fallen hero", 1, 100, 10)
        enemy_hero = Hero("Villain", 80, 100, 200)
        expected = "You lose"
        hero_expected_health = hero.health - enemy_hero.level * enemy_hero.damage
        enemy_hero_expected_health = (enemy_hero.health - hero.level * hero.damage) + 5
        enemy_hero_expected_lvl = enemy_hero.level + 1
        enemy_hero_expected_damage = enemy_hero.damage + 5

        actual = hero.battle(enemy_hero)
        self.assertEqual(expected, actual)
        self.assertEqual(hero_expected_health, hero.health)
        self.assertEqual(enemy_hero_expected_lvl, enemy_hero.level)
        self.assertEqual(enemy_hero_expected_damage, enemy_hero.damage)
        self.assertEqual(enemy_hero_expected_health, enemy_hero.health)

    def test_str__expected_correct_info(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected, str(self.hero))


if __name__ == "__main__":
    unittest.main()