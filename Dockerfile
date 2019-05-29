FROM python:3.7

RUN pip install pandas
RUN pip install black
RUN pip install cookiecutter
RUN pip install -i https://test.pypi.org/simple/ lambdata-beverast

CMD ["python", "-c", "import lambdata_beverast; print('Installation Validated.')"]