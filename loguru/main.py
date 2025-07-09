from loguru import logger
# установка pip install loguru
# Настройка логгера (вывод в файл и консоль)
logger.add("app.log", rotation="10 MB", level="INFO")  # Запись в файл с ротацией

# Примеры сообщений разного уровня
logger.debug("Это сообщение отладки (не будет записано)")
logger.info("Запуск приложения")
logger.warning("Предупреждение: низкий уровень памяти")
logger.error("Произошла ошибка!")
logger.critical("Критическая ошибка! Приложение остановлено")

# Логирование исключений
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Деление на ноль!")

# Пример функции с логированием
def process_data(data):
    logger.info(f"Обработка данных: {data}")
    return data * 2

result = process_data(42)
logger.success(f"Результат: {result}")