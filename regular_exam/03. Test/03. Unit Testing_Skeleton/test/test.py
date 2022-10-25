from project.team import Team


from unittest import TestCase


class TeamTests(TestCase):
    def test_when__invalid_name__expected_raise_error(self):
        with self.assertRaises(ValueError) as context:
            team = Team("123p=31")
        self.assertEqual('Team Name can contain only letters!', str(context.exception))

    def test_when__valid_name__expected_correct_initialization(self):
        team = Team("United")
        expected = "United"
        actual = team.name
        self.assertEqual(expected, actual)
        self.assertEqual({}, team.members)

    def test_str_method(self):
        team = Team("United")
        expected = "Team name: United"
        actual = str(team)
        self.assertEqual(expected, actual)

    def test_gt_method_if_false(self):
        team = Team("United")
        team_2 = Team("Chelsea")
        self.assertFalse(team > team_2)

    def test_gt_method_if_true(self):
        team = Team("United")
        team.members["Tom"] = 23
        team_2 = Team("Chelsea")
        self.assertTrue(team > team_2)

    def test_add_method(self):
        team = Team("United")
        team_2 = Team("Chelsea")
        new_team = team + team_2
        expected = "UnitedChelsea"
        actual = new_team.name
        self.assertEqual(expected, actual)

    def test_len(self):
        team = Team("United")
        self.assertEqual(0, len(team)