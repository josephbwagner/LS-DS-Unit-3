# lambdata **WIP**
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

A collection of DS project helper functions

# Usage
```
from lambdata_beverast.structurizer import Directory
dir = Directory(target_dir='/home/beverast/projects/')
dir.apply_cookiecutter()
```

```
from lambdata_beverast.structurizer import Codebase
dir = Codebase(target_dir='/home/beverast/projects/new_project')
dir.apply_black()
```

# Tests

Tests can be ran using [pytest](https://docs.pytest.org/en/latest/) from the project 
root directory.

```
user@machine~/lambdata/lambdata_beverast/: pytest
```
