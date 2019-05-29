FROM python:3.7.3-stretch

# Set working dir and copy current dir into work
WORKDIR /app
COPY . /app

# Required dependencies
RUN pip --no-cache-dir install pandas black cookiecutter
RUN pip install -i https://test.pypi.org/simple/ lambdata-beverast

RUN python -c "import lambdata_beverast; print('Y: ', lambdata_beverast.Y)"