# 0 log
# 1 warn
# 2 error
def log_decorator(log_level: int, log_msg: str):
    def wrapper(func):
        if log_level == 0:
            print("[LOG]: ", log_msg)
        elif log_level == 1:
            print("[WARN]: ", log_msg)
        elif log_level == 2:
            print("[ERROR]: ", log_msg)
        return func
    return wrapper

@log_decorator(1, "lol")
def a():
    print("hello")

a()
