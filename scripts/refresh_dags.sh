#!/usr/bin/env bash
cd /opt/airflow/<your DAG repo name>
git checkout <your PRODUCTION branch>
while true;
do
  echo "Refresh DAGs folder ..."
  git pull
  echo "DAGs folder refreshed. Listing DAG folder: "
  sleep 20
done