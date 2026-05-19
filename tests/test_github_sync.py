import os
import importlib.util
import sys


def load_github_sync_module():
    repo_root = os.path.dirname(os.path.dirname(__file__))
    module_path = os.path.join(repo_root, ".scripts", "github_sync.py")
    spec = importlib.util.spec_from_file_location("github_sync", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_build_session_reads_token():
    os.environ.pop("GITHUB_TOKEN", None)
    gs = load_github_sync_module()
    s = gs.build_session()
    assert s is not None
