
from datetime import datetime
from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования работы функций.

    filename - имя файла для записи логов.Если не указан, логи выводятся в консоль.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # формирование строки для догирования
            args_str = ", ".join([repr(arg) for arg in args])
            kwargs_str = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])

            if args_str and kwargs_str:
                all_args = f"{args_str}, {kwargs_str}"
            elif args_str:
                all_args = args_str
            elif kwargs_str:
                all_args = kwargs_str
            else:
                all_args = ""

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                result = func(*args, **kwargs)

                # сообщение об успехе
                log_message = f"[{timestamp}] {func.__name__}({all_args}) -> {repr(result)} (ok)"

                # выбор места логирования в консоль или в файл
                if filename is None:
                    print(log_message)
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message + "\n")

                return result

            except Exception as e:
                # сообщение об ошибке
                error_message = f"[{timestamp}] {func.__name__}({all_args}) -> ERROR: {type(e).__name__}: {e}"

                # выбор места логирования в консоль или в файл
                if filename is None:
                    print(error_message)
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")

                raise

        return wrapper

    return decorator