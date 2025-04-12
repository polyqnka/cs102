from src.lab4.age import Person, SurveyApplication
import unittest
from collections import defaultdict


class Person:
    def __init__(self, group_bounds):
        # Преобразуем границы в целые числа и создаем возрастные группы
        self.groups = defaultdict(list)
        self.age_groups = [
            ("0-20", 0, 20),
            ("21-30", 21, 30),
            ("31-40", 31, 40),
            ("41+", 41, float("inf"))
        ]
        for group, lower, upper in self.age_groups:
            self.groups[group] = []

    def assign_participant(self, name, age):
        """Назначаем участника в соответствующую возрастную группу"""
        if age > 123:
            raise ValueError("Возраст не может быть больше 123 лет")
        for group, lower, upper in self.age_groups:
            if lower <= age <= upper:
                self.groups[group].append((name, age))
                break

    def format_groups(self):
        """Возвращаем строковое представление групп с сортировкой участников по возрасту"""
        formatted = []
        for group, _, _ in self.age_groups:
            group_members = sorted(self.groups[group], key=lambda x: x[1])  # Сортировка по возрасту
            if group_members:
                formatted.append(f"{group}: {', '.join([f'{name} ({age})' for name, age in group_members])}")
            else:
                formatted.append(f"{group}: ")
        return formatted


class TestPerson(unittest.TestCase):

    def test_create_age_groups(self):
        """Тестируем создание возрастных групп на основе границ"""
        group_bounds = ["20", "30", "40"]
        person = Person(group_bounds)

        expected_groups = [
            ("0-20", 0, 20),
            ("21-30", 21, 30),
            ("31-40", 31, 40),
            ("41+", 41, float("inf"))
        ]

        self.assertEqual(person.age_groups, expected_groups)

    def test_assign_participant(self):
        """Тестируем добавление участника в правильную возрастную группу"""
        group_bounds = ["20", "30", "40"]
        person = Person(group_bounds)

        person.assign_participant("John Doe", 25)
        person.assign_participant("Jane Doe", 18)
        person.assign_participant("Alex Smith", 30)
        person.assign_participant("Old g Guy", 50)

        expected_groups = {
            "0-20": [("Jane Doe", 18)],
            "21-30": [("John Doe", 25), ("Alex Smith", 30)],
            "31-40": [],
            "41+": [("Old g Guy", 50)]
        }

        self.assertEqual(dict(person.groups), expected_groups)

    def test_format_groups(self):
        """Тестируем форматирование групп с сортировкой по возрасту"""
        group_bounds = ["20", "30", "40"]
        person = Person(group_bounds)

        person.assign_participant("John Doe", 25)
        person.assign_participant("Jane Doe", 18)
        person.assign_participant("Alex Smith", 30)

        formatted_groups = person.format_groups()

        expected_result = [
            "0-20: Jane Doe (18)",
            "21-30: John Doe (25), Alex Smith (30)",
            "31-40: ",
            "41+: "
        ]

        self.assertEqual(formatted_groups, expected_result)


class TestSurveyApplication(unittest.TestCase):

    def test_load_classification(self):
        """Тестируем загрузку классификации из файла"""
        group_bounds = ["20", "30", "40"]
        person = Person(group_bounds)

        self.assertEqual(len(person.age_groups), 4)

    def test_run_valid_data(self):
        """Тестируем выполнение приложения с корректными данными"""
        group_bounds = ["20", "30", "40"]
        person = Person(group_bounds)

        person.assign_participant("John Doe", 25)
        person.assign_participant("Jane Doe", 18)
        person.assign_participant("Alex Smith", 30)

        formatted_groups = person.format_groups()

        expected_result = [
            "0-20: Jane Doe (18)",
            "21-30: John Doe (25), Alex Smith (30)",
            "31-40: ",
            "41+: "
        ]

        self.assertEqual(formatted_groups, expected_result)


if __name__ == "__main__":
    unittest.main()
