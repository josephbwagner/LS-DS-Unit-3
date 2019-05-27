from subprocess import run


x = 2

def increment(number):
  return number + 1

def initialize_directory():
  run('cookiecutter https://github.com/drivendata/cookiecutter-data-science')

