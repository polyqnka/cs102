class Movie:
    """
    Класс, представляющий фильм.
    """

    def __init__(self, movie_id: int, title: str):
        self.movie_id = movie_id  # Идентификатор фильма
        self.title = title  # Название фильма


class User:
    """
    Класс, представляющий пользователя.
    """

    def __init__(self, user_id: int, watched_movies: set[int]):
        self.user_id = user_id  # Идентификатор пользователя
        self.watched_movies = set(watched_movies)  # Множество просмотренных фильмов


class Recommender:
    """
    Класс рекомендателя, который генерирует рекомендации на основе истории просмотров других пользователей.
    """

    def __init__(self, movies: dict[int, Movie], history: list[User]):
        """
        Инициализация рекомендателя с фильмами и историей просмотров пользователей.
        :param movies: Словарь фильмов {movie_id: Movie}
        :param history: Список пользователей [User]
        """
        self.movies = movies
        self.history = history

    def recommend(self, user_history: list[int]) -> str | None:
        """
        Рекомендует фильм для пользователя на основе истории просмотров других пользователей.
        :param user_history: Список ID фильмов, просмотренных текущим пользователем
        :return: Название рекомендованного фильма или None
        """
        current_user = User(None, set(user_history))

        # Найти похожих пользователей
        similar_users = [
            user for user in self.history
            if current_user.watched_movies & user.watched_movies
        ]

        if not similar_users:
            print("Похожие пользователи не найдены.")
            return None

        # Собираем кандидатов для рекомендаций
        candidate_movies = self._collect_candidates(current_user, similar_users)

        if not candidate_movies:
            print("Нет фильмов для рекомендации.")
            return None

        # Определяем фильм с наибольшим весом
        most_common_movie_id = max(candidate_movies, key=candidate_movies.get)

        return self.movies.get(most_common_movie_id, None).title

    def _collect_candidates(self, current_user: User, similar_users: list[User]) -> dict[int, float]:
        """
        Собирает фильмы-кандидаты на рекомендацию с их весами.
        :param current_user: Текущий пользователь
        :param similar_users: Список похожих пользователей
        :return: Словарь кандидатов {movie_id: вес}
        """
        candidate_movies = {}

        for user in similar_users:
            common_movies = current_user.watched_movies & user.watched_movies
            common_percentage = len(common_movies) / len(current_user.watched_movies)

            weight = self._calculate_weight(common_percentage)

            for movie_id in user.watched_movies - current_user.watched_movies:
                candidate_movies[movie_id] = candidate_movies.get(movie_id, 0) + weight

        return candidate_movies

    @staticmethod
    def _calculate_weight(common_percentage: float) -> float:
        """
        Рассчитывает вес фильма в зависимости от процента совпадений.
        :param common_percentage: Процент совпадающих фильмов
        :return: Вес фильма
        """
        if common_percentage >= 1.0:
            return 1.0
        elif common_percentage >= 0.7:
            return 0.7
        elif common_percentage >= 0.5:
            return 0.5
        return 0.0


    @staticmethod
    def load_movies(filename: str) -> dict[int, Movie]:
        """
        Загружает фильмы из файла.
        :param filename: Путь к файлу с фильмами
        :return: Словарь фильмов {movie_id: Movie}
        """
        movies = {}
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    movie_id, title = map(str.strip, line.split(',', 1))
                    movies[int(movie_id)] = Movie(int(movie_id), title)
        except FileNotFoundError:
            print(f"Ошибка: файл {filename} не найден.")
        return movies

    @staticmethod
    def load_watch_history(file_path: str) -> list[User]:
        """
        Загружает историю просмотров пользователей из файла.
        :param file_path: Путь к файлу с историей
        :return: Список пользователей [User]
        """
        history = []
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(",")
                    user_id = int(parts[0])
                    watched_movies = {int(movie_id) for movie_id in parts[1:]}
                    history.append(User(user_id, watched_movies))
        except FileNotFoundError:
            print(f"Ошибка: файл {file_path} не найден.")
        return history


if __name__ == '__main__':
    movies = Recommender.load_movies('movies.txt')
    history = Recommender.load_watch_history('watch_history.txt')

    recommender = Recommender(movies, history)

    user_history_input = input("Введите ID просмотренных фильмов через запятую: ")
    user_history = [int(movie_id.strip()) for movie_id in user_history_input.split(",") if movie_id.strip().isdigit()]

    recommended_movie = recommender.recommend(user_history)

    if recommended_movie:
        print(f"Рекомендованный фильм: {recommended_movie}")
    else:
        print("Нет рекомендаций.")
