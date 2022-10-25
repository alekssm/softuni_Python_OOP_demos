from project.vehicle import Vehicle


import unittest


class VehicleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 200)

    def test_init__whe_valid_fuel_horse_power_expected_correct_initialization(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive__when_not_enough_fuel__expected_to_raise_exception(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption

        with self.assertRaises(Exception) as context:
            self.vehicle.drive(max_distance + 1)

        self.assertEqual("Not enough fuel", str(context.exception))

    def test_drive__when_enough_fuel__expected_to_lower_the_fuel_amount(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption

        self.vehicle.drive(max_distance)

        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel__when_more_fuel_than_capacity__expected_to_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(10)

        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_refuel__when_less_fuel_than_capacity__expected_to_raise_exception(self):
        traveled_distance = 10
        self.vehicle.drive(traveled_distance)
        fuel_used = traveled_distance * self.vehicle.fuel_consumption
        fuel_recharged = fuel_used / 2
        expected = self.vehicle.fuel + fuel_recharged
        self.vehicle.refuel(fuel_recharged)

        self.assertEqual(expected, self.vehicle.fuel)

    def test_str__expected_correct_info(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(expected, str(self.vehicle))


if __name__ == "__main__":
    unittest.main()