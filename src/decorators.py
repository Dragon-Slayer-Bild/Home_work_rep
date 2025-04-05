import time


def log(filename=None):
    """Декоратор, который логирует выполнение функции"""

    def my_decorator(function):
        def wrapper(*args, **kwargs):
            try:  # текст при выполнении функции
                result = function(*args, **kwargs)
                message = f"[{function.__name__}] result: {result} - OK [{time.asctime()}]\n"
            except Exception as e:  # текст при ошибке в выполнении функции
                message = f"[{function.__name__}] error: {e}. Inputs: {args}, {kwargs} [{time.asctime()}]\n"
                result = None
            finally:
                if filename is None:  # вывод в консоль при отсутствии названия файла
                    print(message, end="")
                else:  # сохранение в файл при наличии названия файла
                    with open(filename, "a") as file:
                        file.write(message)
            return result

        return wrapper

    return my_decorator
