import functools
import logging

# Настройка логгера
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_api_call(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.status_code != 200:
            logger.info(f"Вызов API: {func.__name__}")
            logger.info(f"URL: {response.request.url}")
            logger.info(f"Метод: {response.request.method}")
            logger.info(f"Тело запроса: {response.request.body}")
            logger.info(f"Статус-код ответа: {response.status_code}")

        return response

    return wrapper



def time_counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Время выполнения теста: {end_time - start_time} секунд")
        return result

    return wrapper
