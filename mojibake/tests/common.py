import os

def get_path(relative_to: str, path: str) -> str:
    base, _ = os.path.split(relative_to)
    return os.path.join(base, path)
