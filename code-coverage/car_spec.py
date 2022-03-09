import unittest
from unittest.mock import patch
from Car import Car

class TestCars(unittest.TestCase):

    def setUp(self):
        self.car_1 = Car('Honda')

    def test_car_creation(self):
        self.assertIsNone(self.car_1.defect)
        self.assertEqual(self.car_1.brand, 'Honda')

    def test_wear_and_tear(self):
        with patch('Car.randrange') as fake_randrange:
            fake_randrange.return_value = 0
            self.assertEqual(self.car_1.wear_and_tear(), 0)
            fake_randrange.assert_called_once_with(0,1)

    def test_damage_taken(self):
        with patch('Car.randrange') as fake_randrange:
            fake_randrange.return_value = 1
            with patch("Car.choice") as fake_choice:
                fake_choice.return_value = 'panel gaps'
                self.car_1.take_damage()
                self.assertEqual(self.car_1.defect, 'panel gaps')
                fake_randrange.assert_called()

    def test_damage_none(self):
        with patch('Car.randrange') as fake_randrange:
            fake_randrange.return_value = 0
            self.car_1.take_damage()
            self.assertIsNone(self.car_1.defect)

if __name__ == "__main__":
    unittest.main()
