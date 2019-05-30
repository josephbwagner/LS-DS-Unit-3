from . import structurizer
import os


def test_apply_cookiecutter(tmpdir):
    dir = structurizer.Directory(tmpdir)
    dir.apply_cookiecutter()
    print(os.listdir(tmpdir))
    assert "Makefile" in os.listdir(tmpdir)
