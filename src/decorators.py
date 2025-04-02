import time


def log(filename=None):
    """Декоратор, который логирует выполнение функции"""
    def my_decorator(function):
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                message = f'[{function.__name__}] result: {result} - OK [{time.asctime()}]\n'
            except Exception as e:
                message = f'[{function.__name__}] error: {e}. Inputs: {args}, {kwargs} [{time.asctime()}]\n'
                result = None
            finally:
                if filename is None:
                    print(message, end='')  # Важно: end='' чтобы не было лишнего переноса строки
                else:
                    with open(filename, 'a') as file: # 'a' для добавления в файл
                        file.write(message)
            return result
        return wrapper
    return my_decorator
