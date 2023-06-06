import matplotlib.pyplot as plt
import numpy as np


def inverse_congruential_generator(seed, a, c, m, n):
    random_numbers = []
    x = seed
    for _ in range(n):
        inv_a = pow(a, -1, m)  # Вычисление обратного числа a по модулю m
        x = (inv_a * x + c) % m
        random_numbers.append(x)
    return random_numbers


def plot_random_points(x_coords, y_coords):
    plt.scatter(x_coords, y_coords, s=5)
    plt.title("Случайные точки")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def plot_histogram(data):
    plt.hist(data, bins='auto', edgecolor='black')
    plt.title("Гистограмма распределения")
    plt.xlabel("Значение")
    plt.ylabel("Частота")
    plt.show()


def plot_line_chart(x, y):
    plt.plot(x, y)
    plt.title("Линейный график")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def generate_random_numbers(seed, a, c, m, n):
    random_numbers = inverse_congruential_generator(seed, a, c, m, n)
    return random_numbers


def calculate_mean(data):
    mean = np.mean(data)
    return mean


def calculate_variance(data):
    variance = np.var(data)
    return variance


def calculate_standard_deviation(data):
    std_deviation = np.std(data)
    return std_deviation


def generate_normal_distribution(mean, std_deviation, size):
    normal_distribution = np.random.normal(mean, std_deviation, size)
    return normal_distribution


def plot_normal_distribution(data):
    plt.hist(data, bins='auto', density=True, alpha=0.7)
    plt.title("Нормальное распределение")
    plt.xlabel("Значение")
    plt.ylabel("Плотность")
    plt.show()


def calculate_median(data):
    median = np.median(data)
    return median


def calculate_min_max(data):
    min_value = np.min(data)
    max_value = np.max(data)
    return min_value, max_value


def plot_boxplot(data):
    plt.boxplot(data)
    plt.title("Boxplot")
    plt.xlabel("Данные")
    plt.ylabel("Значение")
    plt.show()


def plot_scatter_regression(x, y):
    plt.scatter(x, y, s=5)
    coeffs = np.polyfit(x, y, 1)
    regression_line = np.polyval(coeffs, x)
    plt.plot(x, regression_line, color='red')
    plt.title("Scatter plot с линией регрессии")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

def plot_pie_chart(labels, sizes):

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title("Круговая диаграмма")
    plt.show()


def main():
    # Параметры генератора
    seed = 1
    a = 1664525
    c = 1013904223
    m = pow(2, 32)


    n = int(input("Введите количество случайных точек: "))
    x_seed = int(input("Введите начальное значение для x: "))
    y_seed = int(input("Введите начальное значение для y: "))

    # Генерация псевдослучайных чисел
    random_numbers = generate_random_numbers(seed, a, c, m, 2 * n)

    # Разделение полученной последовательности на координаты x и y
    x_coords = random_numbers[:n]
    y_coords = random_numbers[n:2 * n]

    # Построение графика случайных точек
    plot_random_points(x_coords, y_coords)

    # Расчет и вывод среднего значения и дисперсии
    mean = calculate_mean(random_numbers)
    variance = calculate_variance(random_numbers)
    print("Среднее значение:", mean)
    print("Дисперсия:", variance)

    # Генерация случайных чисел с нормальным распределением
    normal_distribution = generate_normal_distribution(mean, np.sqrt(variance), n)

    # Построение графика нормального распределения
    plot_normal_distribution(normal_distribution)

    labels = ['A', 'B', 'C', 'D']
    sizes = [20, 30, 10, 40]

    plot_pie_chart(labels, sizes)





if __name__ == "__main__":
    main()