from collections import defaultdict


class Person:
    def __init__(self, group_bounds):
        """
        Класс для управления распределением участников по возрастным группам.

        :param group_bounds: Список возрастных границ для формирования групп.
        """
        self.age_groups = self._create_age_groups(group_bounds)
        self.groups = defaultdict(list)

    def _create_age_groups(self, group_bounds):
        """
        Формирует список возрастных групп из заданных границ.

        :param group_bounds: Список возрастных границ.
        :return: Список возрастных групп с названиями и диапазонами.
        """
        print("Полученные данные:", group_bounds)

        # Фильтрация некорректных данных и преобразование в числа
        valid_bounds = [int(x) for x in group_bounds if str(x).isdigit()]

        # Добавляем верхнюю границу для последней группы
        valid_bounds.append(float("inf"))

        age_groups = []
        for i, upper in enumerate(valid_bounds):
            lower = 0 if i == 0 else valid_bounds[i - 1] + 1
            group_name = f"{lower}-{upper}" if upper != float("inf") else f"{lower}+"
            age_groups.append((group_name, lower, upper))

        return age_groups

    def assign_participant(self, name, age):
        """
        Распределяет участника в соответствующую возрастную группу.

        :param name: Имя участника.
        :param age: Возраст участника.
        """
        if age > 123:
            print(f"Ошибка: участник {name} с возрастом {age} не может быть добавлен, так как возраст больше 123.")
            return  # Прерываем выполнение, если возраст больше 123

        for group_name, lower, upper in self.age_groups:
            if lower <= age <= upper:
                self.groups[group_name].append((name, age))
                break

    def format_groups(self):
        """
        Форматирует данные групп для вывода.
        """
        result = []
        for group_name, participants in sorted(self.groups.items()):  # Сортировка по названиям групп
            if participants:
                sorted_participants = sorted(participants, key=lambda x: (-x[1], x[0]))
                participants_str = ", ".join(f"{fio} ({age})" for fio, age in sorted_participants)
                result.append(f"{group_name}: {participants_str}")
            else:
                result.append(f"{group_name}: ")
        return result


class SurveyApplication:
    def __init__(self, classification_file, persons_file):
        """
        Приложение для обработки анкет участников.

        :param classification_file: Файл с возрастными группами.
        :param persons_file: Файл с данными участников.
        """
        self.persons_file = persons_file
        self.person = self._load_classification(classification_file)

    def _load_classification(self, classification_file):
        """
        Загружает возрастные группы из файла.

        :param classification_file: Путь к файлу с группами.
        :return: Экземпляр класса Person.
        """
        try:
            with open(classification_file, "r") as file:
                group_bounds = file.read().split()
                return Person(group_bounds)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {classification_file} не найден.")

    def run(self):
        """
        Основной метод для запуска приложения.
        """
        try:
            with open(self.persons_file, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        name, age = line.rsplit(",", 1) # только по последней запятой
                        self.person.assign_participant(name.strip(), int(age.strip()))
                    except ValueError:
                        print(f"Пропущена некорректная строка: {line}")
        except FileNotFoundError:
            print(f"Ошибка: файл {self.persons_file} не найден.")
            return

        print("\nРазбивка по возрастным группам:")
        for group in self.person.format_groups():
            print(group)


if __name__ == "__main__":
    classification_file = "classification.txt"
    persons_file = "persons.txt"

    app = SurveyApplication(classification_file, persons_file)
    app.run()
