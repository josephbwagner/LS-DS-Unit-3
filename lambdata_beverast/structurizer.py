import os
from subprocess import run
from cookiecutter.main import cookiecutter as ck
from cookiecutter.utils import make_sure_path_exists as mspe

class Directory:
  """
  Utility class for initializing a Data Science project directory
  """
  def __init__(self, target_dir):
    self.target_dir = target_dir

  def apply_cookiecutter(self):
    """
    If target_dir doesn't have a cookiecutter template, then apply one.
    """
    exists = mspe(self.target_dir)
    # if os.getcwd() != self.target_dir:
      # os.chdir(self.target_dir)

    if exists:
      print(self.target_dir)
      ck('https://github.com/drivendata/cookiecutter-data-science', no_input=True, output_dir=self.target_dir)
      # cookiecutter('https://github.com/drivendata/cookiecutter-data-science', no-input=True, output_dir=self.target_dir)
    else:
      print('target_dir does not exist')
      return


class Codebase:
	"""
	Utility class for code linting
	"""
	pass
