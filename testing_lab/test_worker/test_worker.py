from pythonProject.python_oop_course.testing_lab.test_worker.worker import Worker

import unittest


class WorkerTests(unittest.TestCase):
    valid_name = "Worker"
    valid_salary = 1000
    valid_energy = 100

    def test_init__when_valid_name_salary_energy__expected_correct_initialization(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        self.assertEqual(self.valid_name, worker.name)
        self.assertEqual(self.valid_salary, worker.salary)
        self.assertEqual(self.valid_energy, worker.energy)
        self.assertEqual(0, worker.money)

    def test_rest__when_valid__expect_energy_to_be_incremented(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        worker.rest()

        self.assertEqual(self.valid_energy + 1, worker.energy)

    def test_work__when_energy_equal_or_lower_than_zero__expect_raise_error(self):
        worker = Worker(self.valid_name, self.valid_salary, 0)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual("Not enough energy.", str(context.exception))

    def test_work__when_valid__expect_worker_money_to_be_increased_by_salary(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()
        worker.work()

        self.assertEqual(self.valid_salary * 2, worker.money)

    def test_work__when_valid__expect_worker_energy_to_be_decreased_by_1(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()
        worker.work()

        self.assertEqual(self.valid_energy - 2, worker.energy)

    def test_get_info__when_valid__expect_return_proper_values(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        expected = f'{self.valid_name} has saved 0 money.'
        result = worker.get_info()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
