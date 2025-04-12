import pytest
from src.lab4.recomendations import Movie, User, Recommender


def test_movie_initialization():
    """Тестирует инициализацию класса Movie."""
    movie = Movie("1", "Inception")
    assert movie.movie_id == "1"
    assert movie.title == "Inception"


def test_user_initialization():
    """Тестирует инициализацию класса User."""
    user = User("123", ["1", "2", "3"])
    assert user.user_id == "123"
    assert user.watched_movies == {"1", "2", "3"}


def test_recommender_no_similar_users():
    """Тестирует случай, когда нет похожих пользователей."""
    movies = {
        1: Movie(1, "Inception"),
        2: Movie(2, "Matrix"),
        3: Movie(3, "Avatar"),
    }
    history = [
        User(1, {1}),
        User(2, {2}),
    ]
    recommender = Recommender(movies, history)



def test_recommender_recommendation():
    """Тестирует корректность рекомендаций."""
    movies = {
        1: Movie(1, "Inception"),
        2: Movie(2, "Matrix"),
        3: Movie(3, "Avatar"),
    }
    history = [
        User(1, {1, 2}),
        User(2, {2, 3}),
    ]
    recommender = Recommender(movies, history)  # Создаем объект
    recommendation = recommender.recommend([1])
    assert recommendation == "Matrix"


def test_recommender_no_movies_to_recommend():
    """Тестирует случай, когда нет фильмов для рекомендации."""
    movies = {
        "1": Movie("1", "Inception"),
        "2": Movie("2", "Matrix"),
    }
    history = [
        User("1", ["1", "2"]),
    ]
    recommender = Recommender(movies, history)
    recommendation = recommender.recommend(["1", "2"])
    assert recommendation is None


def test_load_movies(mocker):
    """Тестирует загрузку фильмов из файла."""
    mocker.patch("builtins.open", mocker.mock_open(read_data="1,Inception\n2,Matrix\n"))
    movies = Recommender.load_movies("movies.txt")  # Вызов через класс
    assert len(movies) == 2
    assert movies[1].title == "Inception"

def test_load_watch_history(mocker):
    """Тестирует загрузку истории просмотров из файла."""
    mocker.patch("builtins.open", mocker.mock_open(read_data="1,1,2\n2,2,3\n"))
    history = Recommender.load_watch_history("watch_history.txt")  # Вызов через класс
    assert len(history) == 2
    assert history[0].user_id == 1

