import datetime
import os

BASE_PATH = os.getcwd()
FILE_NAME = 'logger.log'
DIR_LOGS = 'logs'
default_path = os.path.join(BASE_PATH, DIR_LOGS, FILE_NAME)


def logger(path=DIR_LOGS):
    def _logger(some_function):
        if not os.path.exists(path):
            os.mkdir(path)
        if path != default_path:
            log_path = os.path.join(BASE_PATH, path, FILE_NAME)
        else:
            log_path = default_path
        def write_log(*args, **kwargs):
            with open(log_path, 'a+', encoding='utf8') as f:
                f.write(f'Вызвана функция {some_function} в {datetime.datetime.now()} с аргументами {args} | {kwargs}\n')
                result = some_function(*args, **kwargs)
                f.write(f'Вернули результат {result}\n')
                return result


        return write_log
    return _logger


if __name__ == "__main__":
    logger()
