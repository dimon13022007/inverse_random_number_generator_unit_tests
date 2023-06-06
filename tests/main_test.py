
import unittest
import numpy as np
import matplotlib.pyplot as plt

from main import (
    inverse_congruential_generator,
    plot_random_points,
    calculate_mean,
    calculate_variance,
    generate_normal_distribution,
    plot_pie_chart
)

class TestYourCode(unittest.TestCase):
    def test_inverse_congruential_generator(self):
        seed = 1
        a = 1664525
        c = 1013904223
        m = pow(2, 32)
        n = 1000


        random_numbers = inverse_congruential_generator(seed, a, c, m, n)


        self.assertEqual(len(random_numbers), n)

    def test_calculate_mean(self):
        data = [1, 2, 3, 4, 5]
        expected_mean = np.mean(data)


        calculated_mean = calculate_mean(data)


        self.assertEqual(calculated_mean, expected_mean)

    def test_calculate_variance(self):
        data = [1, 2, 3, 4, 5]
        expected_variance = np.var(data)


        calculated_variance = calculate_variance(data)


        self.assertEqual(calculated_variance, expected_variance)

    def test_generate_normal_distribution(self):
        mean = 0
        std_deviation = 1
        size = 1000


        normal_distribution = generate_normal_distribution(mean, std_deviation, size)


        self.assertEqual(len(normal_distribution), size)

    def test_plot_pie_chart(self):
        labels = ['A', 'B', 'C', 'D']
        sizes = [20, 30, 10, 40]


        plot_pie_chart(labels, sizes)



if __name__ == '__main__':
    unittest.main()