FROM ubuntu:18.04
COPY dataset /dataset
COPY rq1 /rq1
COPY rq2 /rq2
COPY rq3 /rq3
COPY raw_dataset.csv /raw_dataset.csv
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -e dataset
