from math import log
import matplotlib.pyplot as plt


class Functions:
    data = [-0.03, 0.73, -0.59, -1.59, 0.38, 1.49, 0.14, -0.62, -1.59, 1.45,
            0.34, -1.38, -1.14, 0.80, 0.73, 0.38, 1.31, 0.52, -1.55, -0.90]

    sorted_data = sorted(data)

    count_set = {}
    n = 0
    expected_value = 0
    dispersion = 0

    def print_init_series(self):
        print("Исходный ряд:")
        print(*self.data)

    def print_sorted_series(self):
        print("Вариационный ряд:")
        print(*self.sorted_data)

    def find_extremal_values(self):
        print(f"Первая порядковая статистика: {self.sorted_data[0]}")
        print(f"Последняя порядковая статистика: {self.sorted_data[-1]}")
        print(f"Размах: {self.sorted_data[-1] - self.sorted_data[0]}")

    def find_expected_value(self):
        for x in self.sorted_data:
            if self.count_set and x == list(self.count_set.keys())[-1]:
                self.count_set[x] += 1
            else:
                self.count_set[x] = 1

        for i in range(len(self.count_set)):
            self.expected_value += list(self.count_set.keys())[i] * list(self.count_set.values())[i] / len(self.data)

        print("Математическое ожидание:", self.expected_value)

    def find_dispersion(self):
        for i in range(len(self.count_set)):
            self.dispersion += (list(self.count_set.keys())[i] - self.expected_value) ** 2 * \
                               list(self.count_set.values())[i]
        print("Дисперсия:", self.dispersion)

    def find_standard_deviation(self):
        print("СКО:", self.dispersion ** 0.5)

    def find_emp_function(self):
        print("Эмпирическая функция:")
        self.n = len(self.data)
        x = list(self.count_set.keys())
        y = 0
        print(f'{round(y, 2)}, при x <= {x[0]}')
        for i in range(len(self.count_set) - 1):
            y += self.count_set[x[i]] / len(self.data) if i < len(self.count_set) else 0
            print(f'{round(y, 2)}, при {x[i]} < x <= {x[i + 1]}')
            plt.plot([x[i], x[i + 1]], [y, y], c='blue')
        y += self.count_set[x[-1]] / len(self.data)
        print(f'{round(y, 2)}, при {x[-1]} < x')
        plt.title("График эмпирической функции распределения")
        plt.show()

    def poligon_and_gistorgram(self):
        h = round((self.sorted_data[-1] - self.sorted_data[0]) / (1 + round(log(self.n, 2))), 2)
        curr_x = round(self.sorted_data[0] - h / 2, 2)
        next_x = round(curr_x + h, 2)
        grouped_data = {curr_x: 0}

        for x in self.sorted_data:
            if x < next_x:
                grouped_data[curr_x] += 1 / self.n
            else:
                grouped_data[next_x] = 1 / self.n
                curr_x = next_x
                next_x = round(next_x + h, 2)

        plt.subplot(3, 1, 1)
        plt.title("Полигон частот")
        plt.plot(list(grouped_data.keys()), list(grouped_data.values()), c='blue')

        plt.subplot(3, 1, 3)
        plt.title("Гистограмма частот")
        plt.bar(list(map(lambda x: x + h / 2, grouped_data.keys())), list(grouped_data.values()), width=h)
        xticks = list(grouped_data.keys()) + [round(list(grouped_data.keys())[-1] + h, 2)]
        plt.xticks(xticks, xticks)
        plt.show()
