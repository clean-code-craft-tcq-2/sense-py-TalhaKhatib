import unittest
import statistics
from math import nan, isnan


class StatsTest(unittest.TestCase):
    def test_report_min_max_avg(self):
        computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
        epsilon = 0.001
        self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
        self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
        self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

    def test_avg_is_nan_for_empty_input(self):
        computedStats = statistics.calculateStats([])
        # All fields of computedStats (average, max, min) must be
        # nan (not-a-number), as defined in the math package
        # Design the assert here.
        # Use nan and isnan in https://docs.python.org/3/library/math.html
        # nan is not equal to itself hence we will do assertFalse
        self.assertFalse(isnan(computedStats["avg"] == nan))
        self.assertFalse(isnan(computedStats["max"] == nan))
        self.assertFalse(isnan(computedStats["min"] == nan))

    def test_raise_alerts_when_max_above_threshold(self):
        # To check the max value and raise alerts
        # Values are returned in dictionary from StatsAlerter function to have proper reference to max values
        emailAlert = statistics.EmailAlert()  # Functions to raise alert, by default are set to True
        ledAlert = statistics.LEDAlert()  # Functions to raise alert, by default are set to True
        maxThreshold = 10.5
        statsAlerter = statistics.StatsAlerter([22.6, 12.5, 3.7], maxThreshold, [emailAlert, ledAlert])
        self.assertTrue(statsAlerter[22.6]["emailAlert"])
        self.assertTrue(statsAlerter[22.6]["ledAlert"])
        self.assertTrue(statsAlerter[12.5]["emailAlert"])
        self.assertTrue(statsAlerter[12.5]["ledAlert"])
        self.assertFalse(statsAlerter[3.7]["emailAlert"])
        self.assertFalse(statsAlerter[3.7]["ledAlert"])


if __name__ == "__main__":
    unittest.main()
