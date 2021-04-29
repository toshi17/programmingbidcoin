from point import Point
from field_element import FieldElement

class ECCTest(TestCase):

    def test_on_curve(self):
        prime = 223
        a = FieldElement(0, 223)
        b = FieldElement(7, 223)
        valid_points = ((192, 105), (17, 56), (1, 193))
        invalid_points = ((200, 119), (42, 99))
        for x_raw, y_raw in valid_points:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            Point(x, y, a, b)
        for x_raw, y_raw in invalid_points:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            with self.assetRaises(valueError):
                Point(x, y, a, b)
