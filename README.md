
# mcr-predictor

## Build the container

This will create a container with the necessary packages based on Dockerfile in this repository:
```
docker build -t mcrpred:v1 .
```

## Uncompress the dataset
The dataset is contained in ``raw_dataset.csv``, which can be obtained as follows:
```
tar -zxvf raw_dataset.csv.tar.gz
```

## Start and enter the container
```
docker run -it mcrpred:v1 /bin/bash
```

## Run the scripts for each Research Question

According to the table below, each Research Question has a set of scripts and output files.

| Command                                        |  Output                                      |
| -----------------------------------------------| -------------------------------------------- |
| ``python3 rq1/rq1_participation.py``           |  ``rq1_participation_results.csv``           | 
| ``python3 rq1/rq1_comments.py``                |  ``rq1_comments_results.csv``                | 
| ``python3 rq2/rq2_participation.py``           |  Terminal output                             | 
| ``python3 rq2/rq2_comments.py``                |  Terminal output                             | 
| ``python3 rq2/rq2_comments_without_f2_f3.py``  |  ``rq2_comments_without_f2_f3_results.csv``  | 
| ``python3 rq3/rq3_participation.py``           |  ``rq3_participation_results.csv``           | 
| ``python3 rq3/rq3_comments.py``                |  ``rq3_comments_results.csv``                | 

## Dataset
Due to a non-disclosure agreement, we are allowed to provide code review data from 2018 in ``raw_dataset.csv``.
