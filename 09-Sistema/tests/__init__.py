import os
import tempfile
import contextlib


@contextlib.contextmanager
def temp_env(env_vars):
    old = {k: os.environ.get(k) for k in env_vars}
    os.environ.update({k: v for k, v in env_vars.items() if v is not None})
    try:
        yield
    finally:
        for k, v in old.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def tmp_env():
    return temp_env({})
