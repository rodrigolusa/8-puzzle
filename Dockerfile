FROM continuumio/miniconda3
WORKDIR /ia
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD bash