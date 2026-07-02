import unittest
from image_utils import calculate_threshold

class TestThresholdCalculation(unittest.TestCase):
    def test_threshold_calculation(self):
        image = np.array([100, 150, 200])
        threshold = calculate_threshold(image)
        self.assertGreater(threshold, 0)