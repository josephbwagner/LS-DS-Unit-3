# docker build . -t python
FROM debian 

# so logging works w/ Docker
ENV PYTHONUNBUFFERED=1

# Specify commands to `RUN`, usually to install deps
# Update system, then install lambdata-beverast and deps
RUN apt-get update && apt-get upgrade -y && \
  apt-get install python3-pip python-pandas -y && \
  pip3 install -i https://test.pypi.org/simple/ lambdata-beverast && \
  python3 -c "import lambdata_beverast; print('Installation Validated.')" 
