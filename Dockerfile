# This file is mainly derived from the official Airflow 2 Image.

FROM apache/airflow:2.1.0
LABEL maintainer="Song Yikun <syk950527@gmail.com>"


# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# Airflow
ARG AIRFLOW_VERSION=2.1.0

USER root

# system level dep
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
           git gcc linux-libc-dev libc6-dev \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy scripts and give them execution permission
COPY ./scripts /scripts/
RUN chmod +x /scripts/refresh_dags.sh
RUN chmod +x /scripts/entrypoint.sh

# For installation / clone of private repo (including DAGs repo)
RUN mkdir /home/airflow/.ssh
COPY .ssh/id_rsa /home/airflow/.ssh/id_rsa

RUN touch /home/airflow/.ssh/known_hosts

# Add in known hosts here for ssh
#RUN ssh-keyscan -t rsa gitlab.com >> /home/airflow/.ssh/known_hosts
#RUN ssh-keyscan -t rsa github.com >> /home/airflow/.ssh/known_hosts

RUN chmod -R 777 /home/airflow/.ssh
#RUN chown -R "airflow:root" "${AIRFLOW_USER_HOME_DIR}" "${AIRFLOW_HOME}

USER airflow

# install additional dependencies under the Airflow user
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# make dir for DAG folder sync
RUN cd /opt/airflow && git clone <your DAG repo link>
RUN cd <your DAG repo name> && git <your PRODUCTION branch>

COPY airflow.cfg /opt/airflow/airflow.cfg

ENTRYPOINT ["/scripts/entrypoint.sh"]

