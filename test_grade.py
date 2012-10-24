from datetime import datetime
from grade import calculate
from unittest import TestCase

class TestGrade(TestCase):
    def test_100_get_A(self):
        score = 100
        grade = calculate(score)
        self.assertEqual('A', grade)

    def test_80_get_A(self):
        score = 80
        grade = calculate(score)
        self.assertEqual('A', grade)

    def test_79_get_B(self):
        score = 79 
        grade = calculate(score)
        self.assertEqual('B', grade)

    def test_0_get_F(self):
        score = 0 
        grade = calculate(score)
        self.assertEqual('F', grade)

    def test_calculate_uses_less_than_100_ms(self):
        x = datetime.now()
        score = 0 
        grade = calculate(score)
        self.assertEqual('F', grade)
        y = datetime.now()
        time_used = y - x
        self.assertTrue(time_used.microseconds < 100000)

