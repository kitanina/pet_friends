import functools
import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_api_call(func):
    """
    Декоратор для логирования запросов к API.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Предполагается, что функция возвращает объект ответа запроса,
        # например, объект Response из библиотеки requests.
        response = func(*args, **kwargs)

        # Логирование информации о запросе и ответе
        logger.info(f"Вызов API: {func.__name__}")
        logger.info(f"URL: {response.request.url}")
        logger.info(f"Метод: {response.request.method}")
        logger.info(f"Тело запроса: {response.request.body}")
        logger.info(f"Статус-код ответа: {response.status_code}")

        return response

    return wrapper
